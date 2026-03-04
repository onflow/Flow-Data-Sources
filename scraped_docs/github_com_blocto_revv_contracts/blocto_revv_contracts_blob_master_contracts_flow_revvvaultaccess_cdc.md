# Source: https://github.com/blocto/revv-contracts/blob/master/contracts/flow/REVVVaultAccess.cdc

```
import "FungibleToken"
import "REVV"

// The REVVVaultAccess contract's role is to allow the REVV contract account owner ('REVV owner')
// to grant other accounts ('other account') access to withdraw REVV from the REVV owner's REVV vault
// while imposing the conditions that:
// [+] there is a max withdrawal limit per other account and,
// [+] access to the REVV owner vault can be revoked by the REVV owner.
//
// The other account can in this way independently withdraw REVV from the REVV owner's vault,
// without the need for multi-sig transactions, or REVV owner sending a transfer transaction.
//
// The immediate use case is for the TeleportCustody operator account to be able to withdraw REVV
// from the REVV owner REVV Vault when they need to top up the TeleportCustody contract, without having to ask
// the REVV owner for a transfer.
//
// The VaultProxy and VaultGuard are based on the FUSD contract's MinterProxy and Minter design.
//
// How to use the contract:
// * The REVV vault owner creates a VaultGuard resource with a max amount and an address for the other account that will withdraw the REVV.
// * The other account creates and saves a VaultProxy resource
// * The REVV owner sets the VaultGuard capability on the VaultProxy
// * The other account can now withdraw REVV
// * The REVV owner can revoke access at any time by unlinking the VaultGuard capability
//
access(all) contract REVVVaultAccess {

  access(all) entitlement SetVaultGuard

  // The storage path for the Proxy Vault
  access(all) let VaultProxyStoragePath: StoragePath

  // The public path for the Proxy Vault
  access(all) let VaultProxyPublicPath: PublicPath

  // The storage path for the REVV contract Admin
  access(all) let AdminStoragePath: StoragePath

  // The storage Path for the proxyToGuardMap
  access(all) view fun getProxyToGuardMapStoragePath(): StoragePath {
    return /storage/proxyToGuardMap 
  } 

  // The amount of REVV authorized for all Vault Guards
  access(all) var totalAuthorizedAmount: UFix64

  // UNUSED - replaced by VaultGuardStoragePaths - but can't be removed
  // Dictionary to store a (VaultProxy address) -> (VaultGuard paths) map
  // The registry helps answer which guards match which proxy.
  // 
  access(contract) let proxyToGuardMap: { Address : VaultGuardPaths }

  // Dictionary to store a (VaultGuard paths) -> (VaultProxy Address) map
  // The registry helps answer which proxy owners match which guard
  //
  access(contract) let guardToProxyMap: { StoragePath : Address }

  // UNUSED - replaced by VaultGuardStoragePaths
  // Struct used to store paths for a Vault
  // Should be saved in a dictionary with VaultProxy address as key
  //
  access(all) struct VaultGuardPaths {
    access(all) let storagePath: StoragePath
    access(all) let privatePath: PrivatePath
    init(storagePath: StoragePath, privatePath: PrivatePath) {
      self.storagePath = storagePath
      self.privatePath = privatePath
    }
  }

  // replaces above struct and stored in account storage as a dictionary with VaultProxy address as key 
  access(all) struct VaultGuardStoragePaths {
    access(all) let storagePath: StoragePath
    access(all) let providerStoragePath: StoragePath
    init(storagePath: StoragePath, providerStoragePath: StoragePath) {
      self.storagePath = storagePath
      self.providerStoragePath = providerStoragePath
    }
  }

  // VaultGuard
  //
  // The VaultGuard's role is to be the source of a revokable link to the account's REVV vault.
  //
  access(all) resource VaultGuard {

    // max is the largest total amount that can be withdrawn using the VaultGuard
    //
    access(all) let max: UFix64
    
    // total keeps track of how much has been withdrawn via the VaultGuard
    //
    access(all) var total: UFix64
    
    // A reference to the vault that holds REVV tokens *with withdraw entitlement*
    //
    access(self) let vaultCapability: Capability<auth(FungibleToken.Withdraw) &REVV.Vault>

    // withdraws REVV tokens from the VaultGuard's internal vault reference
    // Will fail if vault reference is nil / revoked, or amount + previously withdrawn exceeds max
    //
    access(FungibleToken.Withdraw) fun withdraw(amount: UFix64): @REVV.Vault {
        pre {
          (amount + self.total) <= self.max : "total of amount + previously withdrawn exceeds max withdrawal."
        }
        self.total = self.total + amount
        let vaultRef: auth(FungibleToken.Withdraw) &REVV.Vault = self.vaultCapability.borrow() as! auth(FungibleToken.Withdraw) &REVV.Vault
        return <- vaultRef.withdraw(amount: amount)
    }

    // constructor - takes a REVV vault reference, and a max withdrawal amount
    //
    init(vaultCapability: Capability<auth(FungibleToken.Withdraw) &REVV.Vault>, max: UFix64) {
      pre {
        vaultCapability != nil : "vaultCapability is nil in REVV.VaultGuard constructor"
      }
      self.vaultCapability = vaultCapability
      self.max = max
      self.total = 0.0
    }
  }

  // createVaultGuard
  //
  // @param adminRef - a reference to a REVVVaultAccess.Admin. Only accessible to contract account
  // @param vaultProxyAddress - the account address where the VaultProxy will be stored
  // @param maxAmount - the max amount of REVV which VaultGuard will allow the VaultProxy to transfer
  // @param guardStoragePath - the storage path in the REVVVaultAccess contract owner account
  // @param guardPrivatePath - the private path linked to the guardStoragePath    /// j00lz ****NO LONGER USED**** 

  // 
  access(all) fun createVaultGuard(adminRef: &Admin, vaultProxyAddress: Address, maxAmount: UFix64, guardStoragePath: StoragePath, guardPrivatePath: PrivatePath, guardWithdrawPath: StoragePath) {
    pre {
      adminRef != nil : "adminRef is nil"
      self.totalAuthorizedAmount + maxAmount <=  REVV.MAX_SUPPLY : "Requested max amount + previously authorized amount exceeds max supply"
      self.guardToProxyMap.containsKey(guardStoragePath) ==  false : "VaultGuard StoragePath already registered"
    }
    let proxyToGuardMap: {Address: REVVVaultAccess.VaultGuardStoragePaths} = REVVVaultAccess.getProxyToGuardMap()
    assert(proxyToGuardMap[vaultProxyAddress] == nil, message: "VaultProxy Address already registered")

    self.totalAuthorizedAmount  = self.totalAuthorizedAmount + maxAmount
   
    // get authorized REVV vault capability
    let vaultWithdrawCap: Capability<auth(FungibleToken.Withdraw) &REVV.Vault> = self.account.storage.load<Capability<auth(FungibleToken.Withdraw) &REVV.Vault>>(from: REVV.getProviderPath())
      ?? panic("Could not load REVV.Vault provider (FungibleToken.Withdraw entitled) capability")
    
    // create a VaultGuard and save it in storage
    let guardVault: @REVVVaultAccess.VaultGuard <- create VaultGuard(vaultCapability: vaultWithdrawCap, max: maxAmount)
    self.account.storage.save(<- guardVault, to: guardStoragePath)

    // issue capability to the VaultGuard **and save to storage**
    let vaultGuardCap: Capability<&REVVVaultAccess.VaultGuard> = self.account.capabilities.storage.issue<&VaultGuard>(guardStoragePath)
    self.account.storage.save(vaultGuardCap, to: guardWithdrawPath)

    // let pathObject: REVVVaultAccess.VaultGuardPaths = VaultGuardPaths(storagePath: guardStoragePath, privatePath: guardPrivatePath)
    
    // self.proxyToGuardMap.insert(key: vaultProxyAddress, pathObject)
    self.guardToProxyMap.insert(key: guardStoragePath, vaultProxyAddress)

    // New VaultGuardStoragePaths object
    let newVaultGuardStoragePaths: REVVVaultAccess.VaultGuardStoragePaths = VaultGuardStoragePaths(storagePath: guardStoragePath, providerStoragePath: guardWithdrawPath)
    proxyToGuardMap[vaultProxyAddress] = newVaultGuardStoragePaths
    REVVVaultAccess.setProxyToGuardMap(proxyToGuardMap)
  }

  // OLD API replaced with new function below
  // getVaultGuardPaths returns storage path and private path for a VaultGuard
  // @param account address of VaultProxy using the VaultGuard
  //
  access(all) fun getVaultGuardPaths(vaultProxyAddress: Address): VaultGuardPaths? {
    return self.proxyToGuardMap[vaultProxyAddress]
  }

  // NEW API. function replaced as we can't change the return type of the function above
  // getVaultGuardStoragePaths returns storage path and provider storage path for a VaultGuard
  // @param account address of VaultProxy using the VaultGuard
  //
  access(all) fun getVaultGuardStoragePaths(vaultProxyAddress: Address): VaultGuardStoragePaths? {
    let proxyToGuardMap: {Address: REVVVaultAccess.VaultGuardStoragePaths} = 
      self.account.storage.load<{Address: VaultGuardStoragePaths}>(from: REVVVaultAccess.getProxyToGuardMapStoragePath())  
      ?? panic("Could not load proxyToGuardMap")
    return proxyToGuardMap[vaultProxyAddress]
  }

  // getVaultProxyAddress returns an address of a VaultProxy
  // @param the storage path of the VaultGuard used by the VaultProxy
  //
  access(all) fun getVaultProxyAddress(guardStoragePath: StoragePath): Address? {
    return self.guardToProxyMap[guardStoragePath]
  }


  // returns all VaultProxy addresses
  //
  access(all) fun getAllVaultProxyAddresses(): [Address] {
    return REVVVaultAccess.getProxyToGuardMap().keys
  }

  // returns all storage paths for VaultGuards
  //
  access(all) fun getAllVaultGuardStoragePaths() : [StoragePath] {
    return self.guardToProxyMap.keys
  }

  // returns max authorized amount of withdrawal for an account address
  //
  access(all) fun getMaxAmountForAccount(vaultProxyAddress: Address): UFix64 {
    // let paths: REVVVaultAccess.VaultGuardPaths = self.proxyToGuardMap[vaultProxyAddress]!
    let paths: {Address: REVVVaultAccess.VaultGuardStoragePaths} = REVVVaultAccess.getProxyToGuardMap()
    let capability: Capability<&REVVVaultAccess.VaultGuard> = self.account.capabilities.get<&REVVVaultAccess.VaultGuard>(REVV.RevvReceiverPublicPath)
    let vaultRef: &REVVVaultAccess.VaultGuard = capability.borrow()!
    return vaultRef.max
  }

  // returns total withdrawn amount for an account address
  //
  access(all) fun getTotalAmountForAccount(vaultProxyAddress: Address): UFix64 {
    let paths: {Address: REVVVaultAccess.VaultGuardStoragePaths} = REVVVaultAccess.getProxyToGuardMap()
    let capability: Capability<&REVVVaultAccess.VaultGuard> = self.account.capabilities.get<&REVVVaultAccess.VaultGuard>(REVV.RevvReceiverPublicPath)
    let vaultRef: &REVVVaultAccess.VaultGuard = capability.borrow()!
    return vaultRef.total
  }

  // revokes withdrawal capability for an account
  //
  access(all) fun revokeVaultGuard(adminRef: &Admin, vaultProxyAddress: Address){
    pre {
      adminRef != nil : "adminRef is nil"
    }
    let paths: REVVVaultAccess.VaultGuardStoragePaths = self.getVaultGuardStoragePaths(vaultProxyAddress: vaultProxyAddress)!

    //remove from maps
    self.proxyToGuardMap.remove(key: vaultProxyAddress)
    self.guardToProxyMap.remove(key: paths.storagePath)
    
    // remove from new map in storage
    let proxyToGuardMap: {Address: REVVVaultAccess.VaultGuardStoragePaths} = REVVVaultAccess.getProxyToGuardMap()
    proxyToGuardMap.remove(key: vaultProxyAddress)
    
    // save updated map to storage
    REVVVaultAccess.setProxyToGuardMap(proxyToGuardMap)

    //delete guards
    let guardVault: @REVVVaultAccess.VaultGuard <- self.account.storage.load<@REVVVaultAccess.VaultGuard>(from: paths.storagePath)!
    self.totalAuthorizedAmount = self.totalAuthorizedAmount - guardVault.max
    destroy guardVault
  }

  // interface which allows setting of VaultGuard capability
  //
  access(all) resource interface VaultProxyPublic {
    access(SetVaultGuard) fun setCapability(cap: Capability<auth(FungibleToken.Withdraw) &REVVVaultAccess.VaultGuard>)
  }

  // VaultProxy is a resource to allow designated other accounts to retrieve REVV from the REVV contract's REVV vault.
  // Any account can call createVaultProxy() to create a VaultProxy, but only if REVV account calls setCapability
  // on the VaultProxy, can REVV be withdrawn
  //
  access(all) resource VaultProxy: VaultProxyPublic {
    access(self) var vaultGuardCap: Capability<auth(FungibleToken.Withdraw) &REVVVaultAccess.VaultGuard>?
    
    // withdraw REVV. ***MUST** be kept private / non-publicly accessible after setCapability has been called
    // Will fail unless REVV contract account has set a capability using setCapability
    //
    access(all) fun withdraw(amount: UFix64): @{FungibleToken.Vault} {
      pre {
        self.vaultGuardCap!.check() == true : "Can't withdraw. vaultGuardCap.check() failed"
      }
      let cap: auth(FungibleToken.Withdraw) &REVVVaultAccess.VaultGuard?= self.vaultGuardCap!.borrow()
      return <- cap!.withdraw(amount: amount)
    }

    // set a REVV.VaultGuard capability, to allow withdrawal.
    // Only the REVV contract account can create a VaultGuard so the method can be publicly accessible.
    // 
    access(SetVaultGuard) fun setCapability(cap: Capability<auth(FungibleToken.Withdraw) &REVVVaultAccess.VaultGuard>) {
      pre {
        cap.check() == true : "Capability<&REVV.VaultGuard> failed check()"
        cap != nil : "Setting Capability<&REVV.VaultGuard> that is nil"
      }
      self.vaultGuardCap = cap
    }

    init() {
      self.vaultGuardCap = nil
    }
    
  }

  // Anyone can create a VaultProxy but it's useless until the Vault Guard capability is set on it.
  // Only the REVVVaultAccess owner can create and set a VaultGuard capability
  //
  access(all) fun createVaultProxy(): @REVVVaultAccess.VaultProxy {
    return <- create VaultProxy()
  }

  // Admin resource
  //
  access(all) resource Admin { }

  // Helper Functions for loading/saving the proxyToGuardMap
   access(contract) fun getProxyToGuardMap(): {Address: REVVVaultAccess.VaultGuardStoragePaths} {
    let proxyToGuardMap: {Address: REVVVaultAccess.VaultGuardStoragePaths} = 
      self.account.storage.load<{Address: VaultGuardStoragePaths}>(from: REVVVaultAccess.getProxyToGuardMapStoragePath())  
      ?? panic("Could not load proxyToGuardMap")
    return proxyToGuardMap
  }

  access(contract) fun setProxyToGuardMap(_ proxyToGuardMap: {Address: REVVVaultAccess.VaultGuardStoragePaths}) {
    self.account.storage.save(proxyToGuardMap, to: REVVVaultAccess.getProxyToGuardMapStoragePath())
  }

  init() {

    self.totalAuthorizedAmount = 0.0

    self.proxyToGuardMap = {}

    self.guardToProxyMap = {}

    REVVVaultAccess.setProxyToGuardMap({})

    self.VaultProxyStoragePath = /storage/revvVaultProxy

    self.VaultProxyPublicPath = /public/revvVaultProxy

    self.AdminStoragePath = /storage/revvVaultAccessAdmin

    // create an Admin and save it in storage
    //
    let admin: @REVVVaultAccess.Admin <- create Admin()
    self.account.storage.save(<- admin, to: self.AdminStoragePath)
  }
}
```