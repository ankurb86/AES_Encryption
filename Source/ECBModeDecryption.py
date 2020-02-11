from Crypto.Cipher import AES
import timeit

def ecbDecrypt():
    # Start Time for monitoring run time
    startTime = timeit.default_timer()

    #Get Ciphertext
    fcipher = open("../data/ciphertext.txt", "r")
    ciphertext = fcipher.read()
    fcipher.close()
    print("Ciphertext: ", ciphertext)
    ciphertext = bytes.fromhex(ciphertext)

    #Get Key
    fKey = open("../data/key.txt", "r")
    key = fKey.read()
    fKey.close()
    print("Secret Key: ", key)
    key = bytes.fromhex(key)

    #Decipher using AES with ECB Mode
    cipher = AES.new(key, 1) #Mode ECB=1, CBC=2
    decText = cipher.decrypt(ciphertext).decode('utf-8')
    paddedText = decText.count('~')
    decText=decText[:len(decText)-paddedText]
    print("Decrypted Message: ", decText)
    fdecText = open("../data/result.txt","w")
    fdecText.write(decText)
    fdecText.close()

    # Check Execution time using the startTime variable
    stopTime = timeit.default_timer()
    print("\nThe run Time of the Decryption Function for ECB Mode is: ", stopTime - startTime)

    # Save Stats
    fstats = open("../data/runstats", "a+")
    fstats.write("Mode: ECB")
    fstats.write(" Task: Decryption")
    fstats.write(" Runtime: ")
    fstats.write(str(stopTime - startTime))
    fstats.write("\n")
    fstats.close()