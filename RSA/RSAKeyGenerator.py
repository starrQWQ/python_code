# RSA Key Generator


import random,sys,os
import Functions

def main():
    print('Making key file...')
    MakeKeyFiles(1024)
    print('files made.')


#keys are keysize bits in size
def GenerateKey(keysize):
    
    #step 1:create 2 large prime number p and q,n=p*q
    print('Generating p prime...')
    p=Functions.GeneratorLargePrime(keysize)
    print('Generating q prime...')
    q=Functions.GeneratorLargePrime(keysize)
    n=p*q

    #step 2:to generate e,a key
    print('Generating e that is prime to LCM(p-1,q-1)...')
    while True:
        e=random.randrange(2**(keysize-1),2**(keysize))
        if Functions.GCD(e,(p-1)*(q-1))==1:
            break

    #step 3:generate d,the mod inverse of e
    print('calculating d...')
    d=Functions.FindModInverse(e,(p-1)*(q-1))

    PublicKey=(n,e)
    PrivateKey=(n,d)

    print('PublicKey:',PublicKey)
    print('PrivateKey:',PrivateKey)
    
    return (PublicKey,PrivateKey)


# write the keys in 2 files
def MakeKeyFiles(keysize):
    #prevent overwriting
    if os.path.exists('pubkey.txt') or os.path.exists('privkey.txt'):
        sys.exit('the file(s) already exists')

    publickey,privatekey=GenerateKey(keysize)
                                                      # line 50
    print()
    print('writing publickey to its file...')
    fo=open('pubkey.txt','w')
    fo.write('%s,%s,%s'%(keysize,publickey[0],publickey[1]))
    fo.close()

    print()
    print('writing privatekey to its file...')
    fo=open('privatekey.txt','w')
    fo.write('%s,%s,%s'%(keysize,privatekey[0],privatekey[1]))
    fo.close()



if __name__=='__main__':
    main()



    

