#RSA encrypt and decrypt

import sys


BLOCKSIZE=128
BYTESIZE=256

def main():
    mode=input("encrypt(E) or decrypt(D)?")
    
    if mode=='E':
        f=open('message.txt','r')
        message=f.read()
     #   message="fjaslghagkgklahagad"
        cipherfilename='cipher.txt'
        keyfilename='pubkey.txt'
        print('Encrypting and writing...')
        EncryptedText=EncryptAndWriteToFile(cipherfilename,keyfilename,message)
        print('cipher:',EncryptedText)
        
    elif mode=='D':
        
        print('reading and decrypting...')
        DecryptedText=ReadFromFileAndDecrypt('cipher.txt','privatekey.txt')
        print('Decrypted Text',DecryptedText)
def GetBlocksFromText(message):
    messagebytes=(message.encode('ascii'))

    blockints=[]
    for blockstart in range(0,len(messagebytes),BLOCKSIZE):
        blockint=0
        for i in range(blockstart,min(blockstart+BLOCKSIZE,len(messagebytes))):
            blockint+=(messagebytes[i])*(BYTESIZE**(i%BLOCKSIZE))
        blockints.append(blockint)
    return blockints
def GetTextFromBlocks(blockints,messagelenth,):
    message=[]
    for blockint in blockints:
        blockmessage=[]
        for i in range(BLOCKSIZE-1,-1,-1):
            if len(message)+i<messagelenth:
                ascii=blockint//(BYTESIZE**i)
                blockint=blockint%(BYTESIZE**i)
                blockmessage.insert(0,chr(ascii))
        message.extend(blockmessage)
    return ' '.join(message)
def EncryptMessage(message,key):
    cipher=[]
    n,e=key

    for block in GetBlocksFromText(message):
        cipher.append(pow(block,e,n))
    return cipher


def DecryptCipher(encryptedblocks,messagelenth,key):
    decryptedblocks=[]
    n,d=key
    for block in encryptedblocks:
        decryptedblocks.append(pow(block,d,n))
    return GetTextFromBlocks(decryptedblocks,messagelenth)


def ReadKeyFile(keyfilename):
    fo=open(keyfilename)
    content=fo.read()
    fo.close()
    keysize,n,EorD=content.split(',')
    return (int(keysize),int(n),int(EorD))


def EncryptAndWriteToFile(cipherfile,keyfile,message):
            
    keysize,n,e=ReadKeyFile(keyfile)
    
    #check if keysize is greater than blocksize
    if keysize<BLOCKSIZE*8:
        sys.exit('error:the blocksize need to be equal to or less than the keysize')
    #encrypt
    encryptedblocks=EncryptMessage(message,(n,e))

    #convert int value to string
    for i in range(len(encryptedblocks)):
       encryptedblocks[i]=str(encryptedblocks[i])
   # encryptedblocks=str(encryptedblocks)
    cipher=','.join(encryptedblocks)
    cipher='%s_%s_%s'%(len(message),BLOCKSIZE,cipher)

    fo=open(cipherfile,'w')
    fo.write(cipher)
    fo.close()

    return cipher


def ReadFromFileAndDecrypt(cipherfilename,keyfilename):
    keysize,n,d=ReadKeyFile(keyfilename)

    fo=open(cipherfilename)
    content=fo.read()
    messagelenth,blocksize,cipher=content.split('_')
    messagelenth=int(messagelenth)
    blocksize=int(blocksize)

    #check if keysize is greater than blocksize
    if keysize<BLOCKSIZE*8:
        sys.exit('error:the blocksize need to be equal to or less than the keysize')

    encryptedblocks=[]
    for block in cipher.split(','):
        encryptedblocks.append(int(block))


    return DecryptCipher(encryptedblocks,messagelenth,(n,d))
    
if __name__=='__main__':
    main()

