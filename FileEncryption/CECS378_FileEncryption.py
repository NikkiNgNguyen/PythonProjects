import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import asymmetric 
from cryptography.hazmat.primitives import serialization


def Myencrypt(message, key):
    """ In this method, you will generate a 16 Bytes IV,
    and encrypt the message using the key and IV in 
    CBC mode (AES).  You return an error
    if the len(key) < 32 (i.e., the key has to be 32 bytes= 256 bits)"""
    
    #convert string message to bytes
    if isinstance(message, str):
        message = message.encode('utf-8')
   
    #make sure key is compatible length for AES encryption
    if len(key) != 32 :
        raise ValueError('the key has to be 32 bytes = 256 bits')
        return 
    
    #generate initialization vector
    iv = os.urandom(16)
    
    #pad message so it can be compatible with CBC mode
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message)
    padded_data += padder.finalize()
    
    #encrypt message with AES using CBC mode
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv),backend = backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return ct, iv
    
def Mydecrypt(iv,key,cipherText):
    """inverse of Myencrypt, returns plaintext of ciphertext"""
    
    #decrypt cipher text with AES using CBC mode
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    plainText = decryptor.update(cipherText) + decryptor.finalize()
    

    
    return plainText


def MyfileEncrypt(filepath):
    """ In this method, you'll generate a 32Byte key. You open and 
    read the file as a string. You then call the above method to 
    encrypt your file using the key you generated. You return the cipher
    C, IV, key and the extension of the file (as a string). """
    
    #generate random secret key
    key = os.urandom(32)
    
    #get extension of file
    filename, file_ext = os.path.splitext(filepath)
     
    #create file object using txt file extension
    if file_ext == ".txt":
        file = open(filepath)
        message = file.read()
        file.close()
    
    #create file object using jpg file extension
    if file_ext == ".jpg":
        with open(filepath, "rb") as imageFile:
            message = imageFile.read()
            
    
    #call Myencrypt function
    ciphertext, iv = Myencrypt(message,key)
    
    return ciphertext, iv, key, file_ext
    


def MyfileDecrypt(cipherText, iv, key, file_ext):
    """inverse function of MyfileEncrypt, creates decrypted file"""
    
    #decrypt ciphertext
    plaintext = Mydecrypt(iv,key,cipherText)
    
    #convert plaintext from bytes to string if .txt file
    if file_ext == ".txt":
        plaintext = plaintext.decode("utf-8") 
    
        #create new file 
        filepath = "/Users/jasminagustin/Documents/workspace/CECS378_EncryptionLab/my_decrypted_message" + file_ext
        file = open(filepath, 'w')
    
        #write decrypted plaintext to txt file
        file.write(plaintext)
        file.close()
    
    #write decrypted plaintext to jpg file
    if file_ext == ".jpg":
        filepath = "/Users/jasminagustin/Documents/workspace/CECS378_EncryptionLab/decryptedimage" + file_ext
        
        #create new jpg file and write to it
        with open(filepath, 'wb') as file:
            file.write(plaintext)
            file.close()

    
    print("decrypted file created")


def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
    
    #call to MyfileEncrypt
    cipher, iv, key, file_ext = MyfileEncrypt(filepath)
    
    #load public pem key from RSA_Publickey_filepath
    with open(RSA_Publickey_filepath, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read(),backend=default_backend())
        
    #create rsa public key encryption object and encrypt AES key, generating RSA cipher
    RSAcipher = public_key.encrypt(key,asymmetric.padding.OAEP(mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    
    return RSAcipher, cipher, iv, file_ext


def MyRSAdecrypt(RSAcipher, C, IV, ext, RSA_Privatekey_filepath):
    
    #load private pem key from RSA_Privatekey_filepath
    with open(RSA_Privatekey_filepath, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(),password = None,backend=default_backend())
        
    #create rsa public key decryption object and decrypt RSAcipher, generating AES key
    AESkey = private_key.decrypt(RSAcipher,asymmetric.padding.OAEP(mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    
    
    #decrypt file using AES key
    MyfileDecrypt(C,IV, AESkey, ext)
    
    
def RSA_key_files():
    
    RSA_Publickey_filepath = "/Users/jasminagustin/Documents/workspace/CECS378_EncryptionLab/RSA_publickey.pem"
    RSA_Privatekey_filepath = "/Users/jasminagustin/Documents/workspace/CECS378_EncryptionLab/RSA_privatekey.pem"
    
     # generate RSA key info
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, key_size=2048)
    
    
    # generate private key in PEM format
    Privatekey_pem = key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())
    
    #write private PEM key to Privatekey file
    with open(RSA_Privatekey_filepath, 'wb') as file:
        file.write(Privatekey_pem)
        file.close()
        
    #generate a public key in PEM format
    public = key.public_key()
    Publickey_pem = public.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
    
    #write pub PEM key to Publickey file
    with open(RSA_Publickey_filepath, 'wb') as file:
        file.write(Publickey_pem)
        file.close()
    
    return RSA_Publickey_filepath, RSA_Privatekey_filepath


def main():
    
    #testing Myencrypt and MyDecrypt functions
    #key = os.urandom(32)
    #cipherText, iv = Myencrypt("this is my super secret message",key)
    #plainText = Mydecrypt(iv,key,cipherText)
    #print(plainText)
    
    #testing MyfileEncrypt and MyfileDecrypt functions
    #filepath = "C:\\Users\\ang_f\\Desktop\\dawgs.jpg"
    #cipher, iv, key, file_ext = MyfileEncrypt(filepath)
    #MyfileDecrypt( cipher, iv, key, file_ext)
    
    
    #testing MyRSAencrpyt and MyRSAdecrypt functions
    filepath = "/Users/jasminagustin/Documents/workspace/CECS378_EncryptionLab/jasmin.txt"
    RSA_Publickey_filepath, RSA_Privatekey_filepath = RSA_key_files()
    RSACipher, cipher, IV, ext = MyRSAEncrypt(filepath, RSA_Publickey_filepath)
    MyRSAdecrypt(RSACipher, cipher, IV, ext, RSA_Privatekey_filepath)
    
    
main()
