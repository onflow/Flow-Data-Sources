# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/evm-bridging/test/BridgedTopShotMoments.t.sol

```
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import {Test} from "forge-std/Test.sol";
import "forge-std/console.sol";
import {Upgrades} from "openzeppelin-foundry-upgrades/src/Upgrades.sol";
import {BridgedTopShotMoments} from "../src/BridgedTopShotMoments.sol";
import {ERC721} from "openzeppelin-contracts/contracts/token/ERC721/ERC721.sol";
import {IERC721Errors} from "openzeppelin-contracts/contracts/interfaces/draft-IERC6093.sol";
import {Ownable} from "openzeppelin-contracts/contracts/access/Ownable.sol";
import {Strings} from "openzeppelin-contracts/contracts/utils/Strings.sol";
import {CrossVMBridgeERC721FulfillmentUpgradeable} from "../src/lib/CrossVMBridgeERC721FulfillmentUpgradeable.sol";
import {CrossVMBridgeCallableUpgradeable} from "../src/lib/CrossVMBridgeCallableUpgradeable.sol";

import {IERC721} from "@openzeppelin/contracts/interfaces/IERC721.sol";
import {IERC721Metadata} from "@openzeppelin/contracts/interfaces/IERC721Metadata.sol";
import {IERC721Enumerable} from "@openzeppelin/contracts/interfaces/IERC721Enumerable.sol";
import {ICrossVMBridgeERC721Fulfillment} from "../src/interfaces/ICrossVMBridgeERC721Fulfillment.sol";
import {ICrossVMBridgeCallable} from "../src/interfaces/ICrossVMBridgeCallable.sol";
import {ICrossVM} from "../src/interfaces/ICrossVM.sol";
import {ICreatorToken, ILegacyCreatorToken} from "../src/interfaces/ICreatorToken.sol";
import {IERC165} from "@openzeppelin/contracts/utils/introspection/IERC165.sol";
import {IERC2981} from "@openzeppelin/contracts/interfaces/IERC2981.sol";
import {IBridgePermissions} from "../src/interfaces/IBridgePermissions.sol";

// Add this minimal ERC721 implementation for testing
contract UnderlyingERC721 is ERC721, Ownable {
    constructor(string memory name, string memory symbol) ERC721(name, symbol) Ownable(msg.sender) {}

    function safeMint(address to, uint256 tokenId) public onlyOwner {
        _safeMint(to, tokenId);
    }
}

contract BridgedTopShotMomentsTest is Test {
    address owner;
    address underlyingNftContractOwner;
    address underlyingNftContractAddress;
    address vmBridgeAddress;

    string name;
    string symbol;
    string baseTokenURI;
    string cadenceNFTAddress;
    string cadenceNFTIdentifier;
    string contractURI;
    BridgedTopShotMoments private nftContract;
    UnderlyingERC721 private underlyingNftContract;
    uint256[] nftIDs;

    // Runs before each test
    function setUp() public {
        // Set owner
        owner = msg.sender;

        // Deploy underlying NFT contract and mint underlying NFTs to owner
        underlyingNftContractOwner = address(0x1111);
        nftIDs = [101, 102, 103];
        vm.startPrank(underlyingNftContractOwner);
        underlyingNftContract = new UnderlyingERC721("Underlying NFT", "UNFT");
        for (uint256 i = 0; i < nftIDs.length; i++) {
            underlyingNftContract.safeMint(owner, nftIDs[i]);
        }
        vm.stopPrank();
        assertEq(underlyingNftContract.balanceOf(owner), nftIDs.length);

        // Set NFT contract initialization parameters
        underlyingNftContractAddress = address(underlyingNftContract);
        vmBridgeAddress = address(0x67890);
        name = "name";
        symbol = "symbol";
        baseTokenURI = "https://example.com/";
        cadenceNFTAddress = "cadenceNFTAddress";
        cadenceNFTIdentifier = "cadenceNFTIdentifier";
        contractURI = 'data:application/json;utf8,{"name": "Name of NFT","description":"Description of NFT"}';

        // Deploy NFT contract using UUPS proxy for upgradeability
        address proxyAddr = Upgrades.deployUUPSProxy(
            "BridgedTopShotMoments.sol",
            abi.encodeCall(
                BridgedTopShotMoments.initialize,
                (
                    owner,
                    underlyingNftContractAddress,
                    vmBridgeAddress,
                    name,
                    symbol,
                    baseTokenURI,
                    cadenceNFTAddress,
                    cadenceNFTIdentifier,
                    contractURI
                )
            )
        );

        // Set contract instance
        nftContract = BridgedTopShotMoments(proxyAddr);
    }

    /* Test interface implementations */

    function test_SupportsInterface() public view {
        assertEq(nftContract.supportsInterface(type(IERC165).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(IERC721).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(IERC721Metadata).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(IERC721Enumerable).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(ICrossVM).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(ICreatorToken).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(ILegacyCreatorToken).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(IERC2981).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(ICrossVMBridgeERC721Fulfillment).interfaceId), true);
        assertEq(nftContract.supportsInterface(type(IBridgePermissions).interfaceId), true);
    }

    /* Test contract initialization */

    function test_GetContractInfo() public view {
        assertEq(nftContract.owner(), owner);
        assertEq(nftContract.name(), name);
        assertEq(nftContract.symbol(), symbol);
        assertEq(nftContract.getCadenceAddress(), cadenceNFTAddress);
        assertEq(nftContract.getCadenceIdentifier(), cadenceNFTIdentifier);
        assertEq(nftContract.contractURI(), contractURI);
        assertEq(address(nftContract.underlying()), underlyingNftContractAddress);
        assertEq(nftContract.vmBridgeAddress(), vmBridgeAddress);
        assertEq(nftContract.getTransferValidator(), address(0));
        assertEq(nftContract.royaltyAddress(), address(0));
        assertEq(nftContract.royaltyBasisPoints(), 0);
    }


    /* Test wrapping operations */

    function test_WrapNFTs() public {
        // Approve and wrap NFTs
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();
        assertEq(nftContract.balanceOf(owner), nftIDs.length);
        assertEq(underlyingNftContract.balanceOf(owner), 0);
        for (uint256 i = 0; i < nftIDs.length; i++) {
            assertEq(nftContract.ownerOf(nftIDs[i]), owner);
        }
    }

    function test_RevertWrapNFTsNotApproved() public {
        vm.startPrank(owner);
        vm.expectRevert();
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();
    }

    function test_RevertWrapNFTsZeroAddress() public {
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        vm.expectRevert();
        nftContract.depositFor(address(0), nftIDs);
        vm.stopPrank();
    }

    function test_UnwrapNFTs() public {
        // Approve and wrap NFTs
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();

        // Unwrap NFTs
        vm.startPrank(owner);
        nftContract.withdrawTo(owner, nftIDs);
        vm.stopPrank();
        assertEq(underlyingNftContract.balanceOf(owner), nftIDs.length);
        assertEq(underlyingNftContract.balanceOf(address(nftContract)), 0);
        for (uint256 i = 0; i < nftIDs.length; i++) {
            assertEq(underlyingNftContract.ownerOf(nftIDs[i]), owner);
        }
    }

    /* Test bridge fulfillment */

    function test_FulfillToEVM() public {
        uint256 nftID = 104;
        vm.startPrank(vmBridgeAddress);
        nftContract.fulfillToEVM(owner, nftID, "");
        vm.stopPrank();
        assertEq(nftContract.ownerOf(nftID), owner);
    }

    function test_RevertFulfillToEVMNotEscrowed() public {
        uint256 nftID = 104;
        vm.startPrank(vmBridgeAddress);
        nftContract.fulfillToEVM(owner, nftID, "");
        vm.stopPrank();

        // Fail to fulfill NFT to EVM
        vm.startPrank(vmBridgeAddress);
        vm.expectRevert(abi.encodeWithSelector(ICrossVMBridgeERC721Fulfillment.FulfillmentFailedTokenNotEscrowed.selector, nftID, vmBridgeAddress));
        nftContract.fulfillToEVM(owner, nftID, "");
        vm.stopPrank();
    }

    function test_RevertFulfillToEVMNotBridge() public {
        uint256 nftID = 104;
        vm.startPrank(owner);
        vm.expectRevert(abi.encodeWithSelector(ICrossVMBridgeCallable.CrossVMBridgeCallableUnauthorizedAccount.selector, owner));
        nftContract.fulfillToEVM(owner, nftID, "");
        vm.stopPrank();
    }

    /* Test core ERC721 operations */

    function test_TransferNFT() public {
        address recipient = address(27);

        // Approve and wrap NFT
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();

        // Transfer NFT from account1 to account2 and check balances
        vm.startPrank(owner);
        nftContract.safeTransferFrom(owner, recipient, nftIDs[0]);
        vm.stopPrank();
        assertEq(nftContract.balanceOf(owner), nftIDs.length - 1);
        assertEq(nftContract.balanceOf(recipient), 1);
        assertEq(nftContract.ownerOf(nftIDs[0]), recipient);
    }

    function test_ApproveNFT() public {
        address operator = address(28);

        // Approve and wrap NFT
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();

        // Approve operator for NFT and check approval
        vm.startPrank(owner);
        nftContract.approve(operator, nftIDs[0]);
        vm.stopPrank();
        assertEq(nftContract.getApproved(nftIDs[0]), operator);
    }

    function test_BurnNFT() public {
        // Approve and wrap NFT
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();

        // Burn NFT and check balance
        vm.startPrank(owner);
        nftContract.burn(nftIDs[0]);
        vm.stopPrank();
        assertFalse(nftContract.exists(nftIDs[0]));
        assertEq(nftContract.balanceOf(owner), nftIDs.length - 1);
    }

    /* Test admin operations */

    function test_SetBaseTokenURI() public {
        string memory newBaseTokenURI = "NEW_BASE_URI";

        // Approve and wrap NFT
        vm.startPrank(owner);
        underlyingNftContract.setApprovalForAll(address(nftContract), true);
        nftContract.depositFor(owner, nftIDs);
        vm.stopPrank();
        assertEq(nftContract.tokenURI(nftIDs[0]), string(abi.encodePacked(baseTokenURI, Strings.toString(nftIDs[0]))));

        // Update tokenURI and check newURI
        vm.startPrank(owner);
        nftContract.setBaseTokenURI(newBaseTokenURI);
        vm.stopPrank();
        assertEq(nftContract.tokenURI(nftIDs[0]), string(abi.encodePacked(newBaseTokenURI, Strings.toString(nftIDs[0]))));
    }

    function test_SetERC721Symbol() public {
        // Check initial symbol
        string memory initialSymbol = nftContract.symbol();
        assertEq(initialSymbol, symbol);

        // Update symbol and check new symbol
        string memory newSymbol = "NEW_SYMBOL";
        vm.startPrank(owner);
        nftContract.setSymbol(newSymbol);
        vm.stopPrank();
        assertEq(nftContract.symbol(), newSymbol);
    }

    function test_TransferContractOwnership() public {
        address newOwner = address(27);
        vm.startPrank(owner);
        nftContract.transferOwnership(newOwner);
        vm.stopPrank();
        assertEq(nftContract.owner(), newOwner);
    }

    function test_RevertTransferContractOwnershipToZeroAddress() public {
        address newOwner = address(0);
        vm.startPrank(owner);
        vm.expectRevert();
        nftContract.transferOwnership(newOwner);
        vm.stopPrank();
    }

    /* Test Creator Token operations */

    function test_SetTransferValidator() public {
        // Check initial transfer validator
        assertEq(nftContract.getTransferValidator(), address(0));

        // Set transfer validator and check new validator
        address transferValidator = address(27);
        vm.startPrank(owner);
        nftContract.setTransferValidator(transferValidator);
        vm.stopPrank();
        assertEq(nftContract.getTransferValidator(), transferValidator);
    }

    function test_SetRoyaltyInfo() public {
        // Check initial royalty info
        assertEq(nftContract.royaltyAddress(), address(0));

        // Set royalty info and check new info
        uint96 royaltyBps = 500;
        vm.startPrank(owner);
        nftContract.setRoyaltyInfo(
            BridgedTopShotMoments.RoyaltyInfo({
                royaltyAddress: owner,
                royaltyBps: royaltyBps
            })
        );
        vm.stopPrank();
        assertEq(nftContract.royaltyAddress(), owner);
        assertEq(nftContract.royaltyBasisPoints(), royaltyBps);

        address newRoyaltyAddress = address(28);
        uint96 newRoyaltyBps = 1000;
        // Set royalty info again and check new info
        vm.startPrank(owner);
        nftContract.setRoyaltyInfo(
            BridgedTopShotMoments.RoyaltyInfo({
                royaltyAddress: newRoyaltyAddress,
                royaltyBps: newRoyaltyBps
            })
        );
        vm.stopPrank();
        assertEq(nftContract.royaltyAddress(), newRoyaltyAddress);
        assertEq(nftContract.royaltyBasisPoints(), newRoyaltyBps);
    }
}

```