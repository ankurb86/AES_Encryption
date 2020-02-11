from Crypto.Cipher import AES
import timeit


def ecbEncrypt():
    #Start Time for monitoring run time
    startTime = timeit.default_timer()

    #Get the key
    fKey = open("../data/key.txt", "r")
    key = fKey.read()
    fKey.close()
    print("Secret Key: ", key)
    key = bytes.fromhex(key)

    #Get the plaintext
    fPlainText = open("../data/plaintext.txt", "r")
    plainTextString = fPlainText.read().encode("latin-1")
    fPlainText.close()
    print("PlaintText String: ", plainTextString)
    plainTextString = plainTextString + ((16 - len(plainTextString) % 16) * '~').encode("latin-1")

    #Encrypt with ECB Mode and save the Ciphertext
    cipher = AES.new(key, 1) #Mode ECB=1, CBC=2
    cipherText = (cipher.encrypt(plainTextString)).hex()
    print("ciphertext: ", cipherText)
    fCipherText = open("../data/ciphertext.txt", "w")
    fCipherText.write(cipherText)
    fCipherText.close()

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time of the Encryption Function for ECB Mode is: ", stopTime - startTime)

    #Save Stats
    fstats = open("../data/runstats","a+")
    fstats.write("Mode: ECB")
    fstats.write(" Task: Encryption")
    fstats.write(" Runtime: ")
    fstats.write(str(stopTime - startTime))
    fstats.write(" Ciphertext Generated: ")
    fstats.write(cipherText)
    fstats.write("\n")
    fstats.close()