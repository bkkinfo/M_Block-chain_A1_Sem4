# M_Block-chain_A1_Sem4
Consider the following scenario: you and your friends are transferring money from one account to another. You go to your bank and request that a particular amount be transferred from your account to your friend's account. This is recorded on the bank's internal servers. This record must be updated on both the receiver's and sender's accounts.
There are few issues which may generates in banking system are: 

● Intermediation. 

● Failure of centralized server. 

● Transaction alteration. 

● Fake entry in the transactions. 

To solve these problems you need to implement blockchain technology by satisfying following criteria: 

● Create at least 10 nodes as miners who are connected to each other. Each miner is connected to at least 2 usres. 

● Create a wallet which contains private and public keys. 

● Use the hash of the public key as the address of each user’s wallet. 

● Using digital signatures verify the sender and receiver.

● The header of a block in the blockchain should contain: block index, timestamp, previous block hash, and merkle root. 

● The body of the block should contain the hash of each transaction.

● Store the transactions in UTXO format ( w.r.t. Bitcoin wallet). 

