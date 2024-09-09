import hashlib
import json

class Block():
    def __init__(self,tstamp,name,voterid,party,prevhash=''):
        
        self.tstamp=tstamp
        self.name=name
        self.voterid=voterid
        self.party=party
        self.prevhash=prevhash
        self.hash=self.calcHash()

    def calcHash(self):
        block_string=json.dumps({"tstamp":self.tstamp,"name":self.name,"voterid":self.voterid,"party":self.party,"prevhash":self.prevhash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        
        string="tstamp: "+str(self.tstamp)+"\n"
        string+="name: "+str(self.name)+"\n"
        string+="voterid"+str(self.voterid)+"\n"
        string+="party"+str(self.party)+"\n"
        string+="prevhash: "+str(self.prevhash)+"\n"
        string+="hash: "+str(self.hash)+"\n"
        return string

class BlockChain():
    def __init__(self):
        self.chain=[self.generateGenesisBlock(),]
    def generateGenesisBlock(self):
        return Block("01/01/2024","gensis name","gensis reason","Gensis Block")
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self,newBlock):
        newBlock.prevhash=self.getLastBlock().hash
        newBlock.hash=newBlock.calcHash()
        self.chain.append(newBlock)