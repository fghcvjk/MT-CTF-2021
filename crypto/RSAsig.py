import signal
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import Crypto.Util.number
from secret import flag
from base64 import *
from Crypto import Random
from proof_of_work import proof_of_work
banner = '''
 ____                             ____  _                   _
/ ___|  ___  ___ _   _ _ __ ___  / ___|(_) __ _ _ __   __ _| |_ _   _ _ __ ___
\___ \ / _ \/ __| | | | '__/ _ \ \___ \| |/ _` | '_ \ / _` | __| | | | '__/ _ \
 ___) |  __/ (__| |_| | | |  __/  ___) | | (_| | | | | (_| | |_| |_| | | |  __/
|____/ \___|\___|\__,_|_|  \___| |____/|_|\__, |_| |_|\__,_|\__|\__,_|_|  \___|
                                          |___/

'''

def dosend(m):
    sys.stdout.flush()
    print(m)
    sys.stdout.flush()

def dorecv():
    sys.stdout.flush()
    return sys.stdin.readline().strip()

def gen():
    random_generator = Random.new().read
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa
    return private_pem

def main():
    rsakey = gen()
    a = RSA._RSAobj(None, rsakey)
    modBits = Crypto.Util.number.size(rsakey.n)
    k = ceil_div(modBits,8)

    while (True):
        dosend("Welcome to this secure cryptosystem:")
        dosend("1.Get flag.\n2.Have my signature.\n3.Exit.\n4.Get my key.")
        dosend("What is your choice?")

        try:
            option = int(dorecv().strip())
            if option == 1:
                cipher = rsakey.encrypt(flag, k)
                dosend(b64encode(cipher[0]))
            elif option == 2:
                dosend("What message to sign?")
                m = int(dorecv().strip())
                sign = a.sign(m, k)
                dosend(str(sign[0][0]))
            elif option == 3:
                dosend("Bye~")
                exit()
            elif option == 4:
                dosend(str(rsakey.n))
                dosend(str(rsakey.e))
            else:
                dosend("Invalid choice!")
        except:
            exit()
if  proof_of_work():
    exit()
#signal.alarm(20)
main()
