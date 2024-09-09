import hashlib
import json
from datetime import datetime

class Block():
    def __init__(self,tstamp,name,voter_id,party,prevhash=''):
        
        self.tstamp=tstamp
        self.name=name
        self.voter_id=voter_id
        self.party=party
        self.prevhash=prevhash
        self.hash=self.calcHash()

    def calcHash(self):
        block_string=json.dumps({"tstamp":self.tstamp,"name":self.name,"reason":self.voter_id,"detail":self.party,"prevhash":self.prevhash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        
        string="tstamp: "+str(self.tstamp)+"\n"
        string+="name: "+str(self.name)+"\n"
        string+="voter_id"+str(self.voter_id)+"\n"
        string+="party"+str(self.party)+"\n"
        string+="prevhash: "+str(self.prevhash)+"\n"
        string+="hash: "+str(self.hash)+"\n"
        return string
    def printHashes(self):
        print("prevhash",self.prevhash)
        print("hash",self.hash)

class BlockChain():
    def __init__(self):
        self.chain=[self.generateGenesisBlock(),]
    def generateGenesisBlock(self):
        return Block("gensis name","gensis voter_id","01/01/2024","Gensis Block")
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self,newBlock):
        newBlock.prevhash=self.getLastBlock().hash
        newBlock.hash=newBlock.calcHash()
        self.chain.append(newBlock)