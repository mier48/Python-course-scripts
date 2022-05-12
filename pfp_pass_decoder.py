#pip3 install pikepdf tqdm

import pikepdf
from tqdm import tqdm

#load password list
passwords = [line.strip() for line in open("pass.txt")]

#iterate over passwords
for passwords in tqdm(passwords, "Decrypting PDF"):
    try:
        #open pdf file
        with pikepdf.open("doc.pdf", password = password) as pdf:
            #password decrypted succesfully, break out of the loop
            print("[+] Password found: ", password)
        break
    except pikepdf._qpdf.PasswordError as e
        #wrong password, just continue in the loop
        continue
