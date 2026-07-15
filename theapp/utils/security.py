from pwdlib import PasswordHash


pswrd_hash = PasswordHash.recommended()


def hash_password (password: str) :
    return pswrd_hash.hash(password)

def check_password (password:str,hashedpaswrd: str) :
    return pswrd_hash.verify(password,hashedpaswrd)


    