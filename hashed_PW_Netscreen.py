import binascii

b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def reversetomd5(knownhash): 

    # strip out nrcstn fixed characters 

    clean="" 

    for i in [1,2,3,4,5,7,8,9,10,11,13,14,15,16,18,19,20,21,22,24,25,26,27,28]: 

        clean+=knownhash[i] 

   

    # create blocks 

    block=[] 

    for i in xrange(2,24,3): 

        p1 = b64.index(clean[i-2]) 

        p2 = b64.index(clean[i-1]) 

        p3 = b64.index(clean[i]) 

        block.append(p1 << 12 | p2 << 6 | p3) 

   

    # split block into half and find out character for each decimal 

    md5hash="" 

    for i in block: 

        n1 = i >> 8 

        n2 = i & 0xff 

        md5hash+=chr(n1)+chr(n2) 

    return binascii.hexlify(md5hash)

 

knownhash = "nFLvHSrMMFfCcs6LOsYMbLPt4AKJ+n:netscreen" 

print reversetomd5(knownhash)
