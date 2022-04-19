from cmd import IDENTCHARS
from web3 import Web3,HTTPProvider
import sys


w3 = Web3(HTTPProvider('http://127.0.0.1:7545'))
address='0x17E6386Db5B1f9149B769F387b3A43bca4aeBb4E'
#Remember to check deployed address and connection
#In our test and presentation, we will use ganache's environment,so the function of connection is localhost with port7545
#Rembmber to check up "listen on network" in the remix terminal to surveillance transaction from web3.py


abi=[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			}
		],
		"name": "CompanyWithdrawMoney",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			}
		],
		"name": "ContinueAvailable",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "CustomSafeTransferFrom",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			}
		],
		"name": "DeleteActivities",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "OwnerWithdraw",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			}
		],
		"name": "ReturnVerifiedGasToUser",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			}
		],
		"name": "safeMint",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "_data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_CompanyAddress",
				"type": "address"
			},
			{
				"internalType": "int256",
				"name": "_TicketNum",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "_TicketPrice",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "decimal",
				"type": "uint256"
			}
		],
		"name": "SetActivity",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			}
		],
		"name": "StopAvailable",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenID",
				"type": "uint256"
			}
		],
		"name": "WebUserVerify",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "Activities",
		"outputs": [
			{
				"internalType": "address",
				"name": "OwnerCompany",
				"type": "address"
			},
			{
				"internalType": "int256",
				"name": "OriginalTicket",
				"type": "int256"
			},
			{
				"internalType": "int256",
				"name": "RemainTicket",
				"type": "int256"
			},
			{
				"internalType": "uint256",
				"name": "Price",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "Available",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "isValue",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "Companys",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "NumberofAct",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "AvailableAct",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "DeadAct",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "Customers",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "TotalCost",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			}
		],
		"name": "GetActivity",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "OwnerCompany",
						"type": "address"
					},
					{
						"internalType": "int256",
						"name": "OriginalTicket",
						"type": "int256"
					},
					{
						"internalType": "int256",
						"name": "RemainTicket",
						"type": "int256"
					},
					{
						"internalType": "uint256",
						"name": "Price",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "Available",
						"type": "bool"
					},
					{
						"internalType": "bool",
						"name": "isValue",
						"type": "bool"
					},
					{
						"internalType": "uint256[]",
						"name": "TicketToken",
						"type": "uint256[]"
					}
				],
				"internalType": "struct MyToken.Activity",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "QueryAddress",
				"type": "address"
			}
		],
		"name": "GetCustomer",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "TotalCost",
						"type": "uint256"
					},
					{
						"internalType": "int256[]",
						"name": "OwnToken",
						"type": "int256[]"
					}
				],
				"internalType": "struct MyToken.Information",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ActID",
				"type": "string"
			}
		],
		"name": "GetSellSituation",
		"outputs": [
			{
				"internalType": "int256",
				"name": "",
				"type": "int256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "instructorAccts",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "OwnerBonus",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "QueryContractBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "QueryOwnerBonus",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "VerifyData",
		"outputs": [
			{
				"internalType": "address",
				"name": "TokenOwner",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "Verified",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "isValue",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
#Remember to change abi's content if the code of smartcontract have any change
"""
List of subroutines: (● represent that subroutines are done)
    ●CompanyWithdraw(Company withdraw the revenue from selling ticket)
    ●ContinueAvailable(Owner's privilege to continue(or recovery) specific ticket to sell)
    ●Approve(Seller approve specific address account can buy his ticket, the token need to be pointed out)
    ●CustomSafetransFrom(Buyer pay ticket price and receive his ticket )
    ●Safemint(Customer buy activity ticket from smart contract)
    ●SetActivity(Owner receive the request of setting activity from company and use this function to input activity data to smartcontract)
    ●SetApproveForAll(Token owner approve all his ticket token to specific account)
    ●StopAvailable(Owner's privilede to suspend specific ticket to sell)
    ●TransferOwnership(Transfer smartcontract's owner to another account)
    ●GetActivity(Custom subroutine to query activities data, and this one can return successfully the array of ticket token)
    ●Activity(Same as above but build-in contract)
    ●balanceOf(Customer query the number of tokens they have)
    ●getApproved(Query token number to know which account have right to transfer from it)
    ●name(Return NFT's name)
    ●owner(Return the owner of smartcontract)
    ●ownerof(Query token owner by inputing token number)
    ●QueryContractBalance(Owner's previlege to query the contract balance)
    ●symbol(Return NFT's symbol)
    ●tokenURI(Return specific token's URI)
	●GetSellSituation(Return the number of tickets which have been selled, ActID need to be pointed out)
	●GetCustomer(Return the tokenIDs and current totalcost in smartcontract that the customer have)
	●DeleteActivity(Owner's privilege to delete activity. tickey money will refund to activity's tickey buyer and the ticket token will be burn out)
	●Web3WebUserVerify(The function to make sure token's owner and the gas will return to msg.sender)
	Latest revised by Limindog at 2022/04/06 22:50

The process of transfer Token(Use A to B for example):
	First: A call approve function to endow B with the right to receive specific token which A have
	Next : B call SafeTransferFrom function to receive the token from A, the smartcontract will refund ticket price to A and receive ticket price from B
	With above process, the Token's owner has been changed, A receive his money, and B need to pay the ticket money

Memo:
	return sys.exc_info()[1](Get error message)
	tx_receipt['status']='1'(meaning the transaction is successful)
	There is no float type in solidity, all of unit of money need to be 'wei' to avoid float type number input to the contract, 1 eth = 10^18 wei.

"""

deployed_contract = w3.eth.contract(address=address, abi=abi)
Owner=w3.eth.accounts[0]#We assume that the first one account is the owner of this contract.
Company=w3.eth.accounts[1]#The second account is the owner of Activity
CustomerA=w3.eth.accounts[2]
CustomerB=w3.eth.accounts[3]
CustomerC=w3.eth.accounts[4]


def Web3Name():
    return deployed_contract.functions.name().call({'from':Owner})

def Web3Owner():
	return deployed_contract.functions.owner().call({'from':Owner})

def Web3Symbol():
    return deployed_contract.functions.symbol().call({'from':Owner})

def Web3SetActivity(ActID,Address,TicketNum,TicketPrice):
    decimal=0
    try:
        while True:
            if TicketPrice==int(TicketPrice):
                break
            else:
                TicketPrice*=10
                decimal+=1
        tx_hash=deployed_contract.functions.SetActivity(ActID,Address,TicketNum,int(TicketPrice),decimal).transact({'from':Owner})
        tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
        block_number=tx_receipt["blockNumber"]
        if tx_receipt['status']==1:
            return ["活動{} 已建立成功，張數{}張、價格{}eth BlockNumber:{}".format(ActID,TicketNum,TicketPrice/(10**decimal),block_number),block_number]
        return tx_receipt
    except:
        e=sys.exc_info()[1]
        dir(sys.exc_info()[1])
        return sys.exc_info()[1]

        #Get error message
def Web3GetActivity(ActID):
	try:
		content=deployed_contract.functions.GetActivity(ActID).call({'from':Owner})
		contentDict={'OwnerCompany':content[0],'OriginalTicketNumber':content[1],'RemainTicket':content[2],
               'Price':content[3]/(10**18),'Available':content[4],'ActOwnToken':content[6]}
		return contentDict

	except:
		return sys.exc_info()[1]

def Web3StopAvailable(ActID):
    try:
        tx_hash=deployed_contract.functions.StopAvailable(ActID).transact({'from':Owner})
        tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt['status']==1:
            return "活動{}已停止販賣".format(ActID)
        return tx_receipt
    except:
        return sys.exc_info()[1]#Get error message

def Web3ContinueAvailable(ActID):
    try:
        tx_hash=deployed_contract.functions.ContinueAvailable(ActID).transact({'from':Owner})
        tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt['status']==1:
            return "活動{}已恢復販賣".format(ActID)
        return tx_receipt
    except:
        return sys.exc_info()[1]#Get error message

def Web3safeMint(ActID,MintAddress,CallerAddress,Money):
    try:
        tx_hash=deployed_contract.functions.safeMint(ActID,MintAddress).transact({'from':CallerAddress,'value': w3.toWei('{:.8f}'.format(Money*1.03),"ether")})
        tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
        block_number=tx_receipt["blockNumber"]
        print(tx_receipt)
        if tx_receipt['status']==1:
            TokenID=int(tx_receipt['logs'][0]['topics'][3].hex(),16)
            return(["Address {} 已購買活動{}成功 TokenID:{} BlockNumber:{}".format(MintAddress,ActID,TokenID,block_number),TokenID,block_number])
        return tx_receipt
    except:
        e=sys.exc_info()[1]
        dir(sys.exc_info()[1])
        return e.args[0]['message']

def Web3ownerOf(Token):
	try:
		Add=deployed_contract.functions.ownerOf(Token).call({'from':Owner})
		return ["TokenID {} 的擁有錢包:{}".format(Token,Add),Add]
	except:
		return sys.exc_info()[1]

def Web3QueryContractBalance():
	try:
		return deployed_contract.functions.QueryContractBalance().call({'from':Owner})/(10**18)
	except:
		return sys.exc_info()[1]

def Web3tokenURI(Token):
	try:
		return deployed_contract.functions.tokenURI(Token).call({'from':Owner})
	except:
		return sys.exc_info()[1]

def Web3Approve(toAddress,Token,CallerAddress):
	try:
		tx_hash=deployed_contract.functions.approve(toAddress,Token).transact({'from':CallerAddress})
		tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
		if tx_receipt['status']==1:
			return "{} 已賦予 {} 購買TokenID {} 的權力".format(CallerAddress,toAddress,Token)
		return tx_receipt
	except:
		return sys.exc_info()[1]

def Web3getApproved(Token):
	try:
		return deployed_contract.functions.getApproved(Token).call({'from':Owner})
	except:
		return sys.exc_info()[1]

def Web3balanceOf(QueryAddress):
	try:
		num=deployed_contract.functions.balanceOf(QueryAddress).call({'from':Owner})
		return ["{} 目前擁有的Token數量為{}".format(QueryAddress,num),num]
	except:
		return sys.exc_info()[1]

def Web3transferOwnership(toAddress):
	try:
		tx_hash=deployed_contract.functions.transferOwnership(toAddress).transact({'from':Owner})
		tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
		return tx_receipt
	except:
		return sys.exc_info()[1]

def Web3CustomSafeTransferFrom(ActID,fromAddress,toAddress,Token,Money,CallerAddress):
	try:
		tx_hash=deployed_contract.functions.CustomSafeTransferFrom(ActID,fromAddress,toAddress,Token).transact({'from':CallerAddress,'value':w3.toWei(Money,"ether")})
		tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
		block_number=tx_receipt["blockNumber"]
		if tx_receipt['status']==1:return["{} 已成功購買來自{} 的Token:{} BlockNumber:{}".format(toAddress,fromAddress,Token,block_number),block_number]
		return tx_receipt
	except:
		e=sys.exc_info()[1]
		dir(sys.exc_info()[1])
		return sys.exc_info()[1]
def Web3SetApprovalForAll(approvedAddress,Approved,CallerAddress):
	try:
		tx_hash=deployed_contract.functions.setApprovalForAll(approvedAddress,Approved).transact({'from':CallerAddress})
		tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
		return tx_receipt
	except:
		e=sys.exc_info()[1]
		dir(sys.exc_info()[1])
		return e.args[0]['message']

def Web3CompanyWithdrawMoney(ActID):
	try:
		tx_hash=deployed_contract.functions.CompanyWithdrawMoney(ActID).transact({'from':Owner})
		tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
		if tx_receipt['status']==1:
			return "公司已成功領取活動{} 的收益".format(ActID)
	except:
		e=sys.exc_info()[1]
		dir(sys.exc_info()[1])
		return e.args[0]['message']

def Web3GetSellSituation (ActID):
	try:
		num=deployed_contract.functions.GetSellSituation(ActID).call({'from':Owner})
		return ["活動{} 銷售的票數為{}".format(ActID,num),num]
	except:
		return sys.exc_info()[1]

def Web3DeleteActivity(ActID):
	try:
		tx_hash=deployed_contract.functions.DeleteActivities(ActID).transact({'from':Owner})
		tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
		return tx_receipt
	except:
		e=sys.exc_info()[1]
		dir(sys.exc_info()[1])
		return e.args[0]['message']
def Web3QueryOwnerBonus():
    try:
        return "SmartContract擁有者目前的收益是{} eth".format(deployed_contract.functions.QueryOwnerBonus().call({'from':Owner})/(10**18))
    except:
        return sys.exc_info()[1]

def Web3OwnerWithdraw():
    try:
        tx_hash=deployed_contract.functions.OwnerWithdraw().transact({'from':Owner})
        tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt['status']==1:
            return "SmartContractOwner已成功領取收益"
        return tx_receipt
    except:
        return sys.exc_info()[1]

def Web3GetCustomer(QueryAddress):
	try:
		content=deployed_contract.functions.GetCustomer(QueryAddress).call({'from':Owner})
		try:
			while True:content[1].remove(-1)
		except:
			pass
		return{'Customer':QueryAddress,'TotalCostInSmartContract':content[0]/(10**18),"CurrentOwnToken":content[1]}
	except:
		return sys.exc_info()[1]
def Web3GetCompanyActNumber(QueryAddress):
	try:
		content=deployed_contract.functions.Companys(QueryAddress).call({'from':Owner})
		return ["公司address: {} 擁有的活動數量為: {} 進行中的數量為: {} 已結束的數量為 {}".format(QueryAddress,content[0],content[1],content[2]),content[0],content[1],content[2]]
	except:
		return sys.exc_info()[1]

def Web3WebUserVerify(tokenID,CallerAddress):
	try:
		tx_hash=deployed_contract.functions.WebUserVerify(tokenID).transact({'from':CallerAddress})
		tx_receipt=w3.eth.waitForTransactionReceipt(tx_hash)
		block_number=tx_receipt["blockNumber"]
		est_gas=int(tx_receipt['gasUsed'])+150000
		tx_hash=deployed_contract.functions.ReturnVerifiedGasToUser(est_gas,CallerAddress).transact({'from':Owner})
		return ['WalletID{} 已成功驗證 TokenID：{}的使用，並已反退其花費的gas BlockNumber:{}'.format(CallerAddress,tokenID,block_number),True,block_number]
	except:
		return [sys.exc_info()[1],False]

def Web3GetVerityData(tokenID,CallerAddress):
	try:
		tx_hash=deployed_contract.functions.VerifyData(tokenID).call({'from':CallerAddress})
		return ['TokenID:{} 的驗證狀態目前為{}'.format(tokenID,tx_hash[1]),tx_hash[1]]
	except:
		return [sys.exc_info()[1],False]

