import string

def signatureVerification(n,e):
    signature = 51
    d = 115

    print('The signature is {0}'.format(signature))

    sigencrypt = modexp(signature,d,n)
    
    print('the encrypted signature is {0}'.format(sigencrypt))

    verification = modexp(sigencrypt,e,n)

    if signature == verification:
        print('Verified')
    else:
        print('Not Verified')

def modexp(m,d,n):
    if d == 0:
        return 1

    z = modexp(m,(d/2),n)

    if (d%2) == 0:
        return ((z*z)%n)
    else:
        return (m * (z*z) %n)


def main():
    c = modexp(4,3539,8051)
    a = modexp(6,3539,8051)
    s = modexp(8,3539,8051)

    print("{0}, {1}, {2}".format(c,a,s))
    
    isVerified = signatureVerification(437,31)


if __name__=='__main__':
    main()

