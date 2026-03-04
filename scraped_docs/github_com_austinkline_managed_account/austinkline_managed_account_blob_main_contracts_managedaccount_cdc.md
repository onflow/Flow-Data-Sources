# Source: https://github.com/austinkline/managed-account/blob/main/contracts/ManagedAccount.cdc

```
// ManagedAccount (aka CAM) is a contract to bring multi-sig management
// and execution of work on-chain instead of using flow's built-in key-based approach
access(all) contract ManagedAccount {
    // Allows participating in a vote, if a Voter resource owner is marked as an owner
    access(all) entitlement Vote
    // Allows proposing a new executable to a manager from a Voter resource
    access(all) entitlement Propose

    access(all) let ManagerStoragePath: StoragePath
    access(all) let ManagerPublicPath: PublicPath
    access(all) let VoterStoragePath: StoragePath

    // Universal events, these are executed in the lifecycle of a Manager/Proposal/Vote regardless of the executable
    access(all) event ManagerCreated(managerAddress: Address, uuid: UInt64, voters: {Address: UFix64})
    access(all) event ProposalAdded(uuid: UInt64, proposer: Address, title: String, description: String, executableType: String)
    access(all) event VoteCast(managerAddress: Address, proposalId: UInt64, voterAddress: Address, weight: UFix64, approved: Bool)
    access(all) event ProposalRun(managerAddress: Address, proposalId: UInt64, approvals: {Address: UFix64}, rejections: {Address: UFix64}, title: String, description: String, done: Bool)

    // Executable-specific events. These are related to the built-in definitions of Executables that are needed to bootstrap
    // newly made managers
    access(all) event ChangeApprovedTypeExecutableCreated(uuid: UInt64, executableType: String, approved: Bool)
    access(all) event ChangeApprovedTypeExecutableRun(uuid: UInt64, executableType: String, approved: Bool)
    access(all) event ChangeVotersExecutableCreated(uuid: UInt64, voters: {Address: UFix64})
    access(all) event ChangeVotersExecutableRun(uuid: UInt64, voters: {Address: UFix64})

    // The building block of arbitrary code execution. If enough votes are cast in favor of
    // a proposal, then its executable is able to be run. When run, an executable will get
    // the fully entitled account which corresponds which the manager is in control of.
    access(all) resource interface Executable {
        // Run the executable if it is able to be run
        // Returns true if the executable is done, and false if it should be run again for its next step.
        access(contract) fun run(acct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account): Bool
        // Returns an arbitary struct with details about this executable
        access(all) view fun describe(): AnyStruct
    }

    // An executable definition which changes whether a given executable type can be used in a proposal made by a voter.
    // If approve is set to true, the executable will be able to be used in new proposals.
    // If approve is set to false, the executable will no longer be permitted in new and existing proposals
    access(all) resource ChangeApprovedTypeExecutable: Executable {
        access(all) let executableType: Type
        access(all) let approved: Bool

        access(contract) fun run(acct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account): Bool {
            let manager = acct.storage.borrow<&Manager>(from: ManagedAccount.ManagerStoragePath)
                ?? panic("failed to borrow manager")
            manager.setExecutableTypeApproval(type: self.executableType, approved: self.approved)

            emit ChangeApprovedTypeExecutableRun(uuid: self.uuid, executableType: self.executableType.identifier, approved: self.approved)

            return true
        }

        access(all) view fun describe(): AnyStruct {
            return {
                "executableType": self.executableType.identifier,
                "approved": self.approved
            }
        }

        init(executableType: Type, approved: Bool) {
            self.executableType = executableType
            self.approved = approved

            emit ChangeApprovedTypeExecutableCreated(uuid: self.uuid, executableType: self.executableType.identifier, approved: self.approved)
        }
    }

    // Alters the addresses which are permitted to vote on proposals hosted on a manager
    // If a voter has a weight of 0, it will be removed from the list of allowed voters
    access(all) resource ChangeVotersExecutable: Executable {
        access(all) let voters: {Address: UFix64}

        access(contract) fun run(acct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account): Bool {
            let manager = acct.storage.borrow<&Manager>(from: ManagedAccount.ManagerStoragePath)
                ?? panic("failed to borrow manager")

            manager.updateVoters(voters: self.voters)

            emit ChangeVotersExecutableRun(uuid: self.uuid, voters: self.voters)

            return true 
        }

        access(all) view fun describe(): AnyStruct {
            return {
                "voters": self.voters
            }
        }

        init(voters: {Address: UFix64}) {
            self.voters = voters

            emit ChangeVotersExecutableCreated(uuid: self.uuid, voters: self.voters)
        }
    }

    // Summary details about a proposal.
    access(all) struct ProposalDetails {
        access(all) let createdOnTimestamp: UFix64
        access(all) let createdBlockHeight: UInt64
        
        access(all) let proposedBy: Address
        access(all) let title: String
        access(all) let description: String

        // The type of the executable that this proposal is for
        access(all) let executableType: Type

        init(proposedBy: Address, title: String, description: String, executableType: Type) {
            let block = getCurrentBlock()
            self.createdBlockHeight = block.height
            self.createdOnTimestamp = block.timestamp

            self.proposedBy = proposedBy
            self.title = title
            self.description = description
            self.executableType = executableType
        }
    }

    // A wrapper resource around an Executable. A Proposal contains an executable,
    // as well as vote results and details about the executable which could be run if
    // enough approals are given.
    access(all) resource Proposal {
        access(self) let executable: @{Executable}
        access(all) let approvals: {Address: UFix64}
        access(all) let rejections: {Address: UFix64}

        access(all) let details: ProposalDetails
        access(all) var done: Bool

        // sum the total current total approval weight for this proposal
        access(all) view fun getApprovalWeight(): UFix64 {
            var approvalWeight = 0.0
            for v in self.approvals.values {
                approvalWeight = approvalWeight + v
            }

            return approvalWeight
        }

        access(all) view fun getApprovals(): {Address: UFix64} {
            return self.approvals
        }

        access(all) view fun getRejections(): {Address: UFix64} {
            return self.rejections
        }

        access(all) view fun getDetails(): ProposalDetails {
            return self.details
        }

        // Record a vote. Can only be done once. This could be changed, but is currently restricted
        // to only once so that a voter cannot manipulate others by switching their response later.
        // A new proposal with the same executable can be made if a new vote is needed.
        access(contract) fun recordVote(addr: Address, weight: UFix64, approved: Bool) {
            pre {
                self.approvals[addr] == nil && self.rejections[addr] == nil: "vote for this address has already been recorded. address: ".concat(addr.toString())
            }

            if approved {
                 self.approvals[addr] = weight
            } else {
                self.rejections[addr] = weight
            }
        }

        // Run this proposal, can only be done if:
        //  1. the proposal has not already been run
        //  2. the sum total of weights is >= 1000.0 (just like a transaction on Flow)
        access(contract) fun run(acct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account): Bool {
            pre {
                !self.done: "proposal is already finished"
            }

            let approvalWeight = self.getApprovalWeight()
            assert(approvalWeight >= 1000.0, message: "canot run, minimum approval weight not met. Need 1000.0 or greater, got: ".concat(approvalWeight.toString()))

            self.done = self.executable.run(acct: acct)
            return self.done
        }

        init(executable: @{Executable}, details: ProposalDetails) {
            self.executable <- executable

            self.approvals = {}
            self.rejections = {}
            self.done = false
            self.details = details
        }
    }

    // A Voter is a resource owned by an address. It is a proxy to vote or propose executables to a Manager since most
    // methods on a manager are set to access(contract). A voter MUST have an owning account address, otherwise it is not possible to tell
    // who a vote came from.
    access(all) resource Voter {
        // Records a vote for a given proposal owned by the referenced Manager.
        // If approved is true, this voter's weight will be added to the proposer's
        // approvals. If false, it will be added to rejections.
        access(Vote) fun vote(manager: &Manager, proposalId: UInt64, approved: Bool) {
            pre {
                self.owner?.address != nil: "Voter resource must be owned by an account to be used."
            }

            let ref: auth(Vote) &Voter = &self
            manager.vote(voter: ref, proposalId: proposalId, approved: approved)
        }

        // Adds a new proposal to the referenced manager. This can only be done if the proposer is a valid voter on the manager
        // NOTE: Proposing does not mean that it has been approved by the proposing Voter. These are done separately so that the 
        // proposer has a chance to review a submission before approving it.
        access(Propose) fun proposeExecutable(manager: &Manager, executable: @{Executable}, title: String, description: String): UInt64 {
            return manager.createProposal(proposer: &self as auth(Propose) &Voter, executable: <-executable, title: title, description: description)
        }
    }

    // A resource that wraps access around a fully entitled account capability.
    // Managers also include active proposals and a dictionary of allowed executable types
    // Executable types must be added explicitly so that a voter cannot attempt to trick others
    // into approving an unrecognized Executable.
    //
    // By default, two Executable types are added when a Manager is created:
    // - ChangeApprovedTypeExecutable -> Allows adding/removing executable types from the approved list
    // - ChangeVotersExecutable -> Merges the existing set of voters with a new set
    access(all) resource Manager {
        access(self) let acct: Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>

        access(self) let proposals: @{UInt64: Proposal}
        access(self) let approvedExecutableTypes: {Type: Bool}

        // What addresses can vote, and with what weight?
        access(self) let voters: {Address: UFix64}

        access(all) view fun borrowProposal(proposalId: UInt64): &Proposal? {
            return &self.proposals[proposalId]
        }

        access(all) view fun getApprovedExecutableTypes(): {Type: Bool} {
            return self.approvedExecutableTypes
        }

        access(all) fun run(proposalId: UInt64) {
            let acct = self.acct.borrow() ?? panic("unable to borrow account capability")
            let proposal = (&self.proposals[proposalId] as &Proposal?) ?? panic("proposal not found. id: ".concat(proposalId.toString()))
            let details = proposal.getDetails()

            assert(self.approvedExecutableTypes[proposal.details.executableType] == true, message: "executable type is not permitted")

            // The proposal resource checks whether it is runnable or not
            let done = proposal.run(acct: acct)
            
            emit ProposalRun(managerAddress: self.acct.address, proposalId: proposalId, approvals: proposal.getApprovals(), rejections: proposal.getRejections(), title: details.title, description: details.description, done: done)
        }

        // Internal callback method used by the ChangeApprovedTypeExecutable resource when it is run
        access(contract) fun setExecutableTypeApproval(type: Type, approved: Bool) {
            if approved {
                self.approvedExecutableTypes[type] = true
            } else {
                self.approvedExecutableTypes.remove(key: type)
            }
        }

        // Internal callback used by the ChangeVotersExecutable resource when it is run
        access(contract) fun updateVoters(voters: {Address: UFix64}) {
            for k in voters.keys {
                if voters[k] == 0.0 {
                    self.voters.remove(key: k)
                } else {
                    self.voters[k] = voters[k]!
                }
            }
        }

        // Internal resource to record a vote. Can only be done if the given voter is owned by an address in this manager's list of voters
        access(contract) fun vote(voter: auth(Vote) &Voter, proposalId: UInt64, approved: Bool) {
            let proposal = (&self.proposals[proposalId] as &Proposal?) ?? panic("proposal not found. id: ".concat(proposalId.toString()))
            let voterAddress = voter.owner?.address ?? panic("voter resource must be owned by an address")
            let voterWeight = self.voters[voterAddress] ?? panic("owner of voter resource is not a valid voter. address: ".concat(voterAddress.toString()))

            proposal.recordVote(addr: voterAddress, weight: voterWeight, approved: approved)

            emit VoteCast(managerAddress: self.acct.address, proposalId: proposalId, voterAddress: voterAddress, weight: voterWeight, approved: approved)
        }

        // Internal method used by the Voter resource to add a new proposal to this manager
        access(contract) fun createProposal(proposer: auth(Propose) &Voter, executable: @{Executable}, title: String, description: String): UInt64 {
            pre {
                proposer.owner?.address != nil: "proposer must have an owning address"
                self.voters[proposer.owner!.address] != nil: "proposer is not a valid voter"
            }

            let details = ProposalDetails(proposedBy: proposer.owner!.address, title: title, description: description, executableType: executable.getType())
            let proposal <- create Proposal(executable: <-executable, details: details)

            let uuid = proposal.uuid

            destroy self.proposals.insert(key: proposal.uuid, <-proposal)

            emit ProposalAdded(uuid: uuid, proposer: proposer.owner!.address, title: title, description: description, executableType: details.executableType.identifier)
            return uuid
        }

        init(acct: Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>, voters: {Address: UFix64}) {
            pre {
                acct.check(): "acct capability must be valid"
            }

            self.acct = acct
            self.proposals <- {}
            self.approvedExecutableTypes = {
                // This executable type must be approved so that others can be added
                Type<@ChangeApprovedTypeExecutable>(): true,
                // This executable type must be approved so that voters can be altered
                Type<@ChangeVotersExecutable>(): true
            }
            self.voters = voters

            emit ManagerCreated(managerAddress: acct.address, uuid: self.uuid, voters: voters)
        }
    }

    access(all) fun createManager(acct: Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>, voters: {Address: UFix64}): @Manager {
        return <- create Manager(acct: acct, voters: voters)
    }

    access(all) fun createVoter(): @Voter {
        return <- create Voter()
    }

    access(all) fun createChangeApprovedTypeExecutable(executableType: Type, approved: Bool): @ChangeApprovedTypeExecutable {
        return <- create ChangeApprovedTypeExecutable(executableType: executableType, approved: approved)
    }

    access(all) fun createChangeVotersExecutable(voters: {Address: UFix64}): @ChangeVotersExecutable {
        return <- create ChangeVotersExecutable(voters: voters)
    }

    init() {
        self.ManagerStoragePath = /storage/cam_manager
        self.ManagerPublicPath = /public/cam_manager

        self.VoterStoragePath = /storage/cam_voter
    }
}
```