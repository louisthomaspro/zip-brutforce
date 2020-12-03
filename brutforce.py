# zip -er secrets.zip secrets.txt

from tqdm import tqdm

from itertools import product
import zipfile
import sys


def brutforce(zip_name, worlist_name):
    print("===================================")
    print("Brutforce lauching...")

    # Open file and remove `\n`
    wordlist_aray=[]
    with open(worlist_name) as wordlist:
        wordlist_aray = wordlist.readlines()
    wordlist_aray = [x.strip() for x in wordlist_aray]

    # Initialize the Zip File object
    zip_file = zipfile.ZipFile(zip_name)
    
    # Calcul number of possibilities
    possibilities=0
    n_words = len(wordlist_aray)
    for i in range(1, len(wordlist_aray) + 1):
        possibilities=possibilities + (n_words ** i)
    print("Total passwords to test:", possibilities)
    pbar = tqdm(total=possibilities)

    # Go go go
    for i in range(1, len(wordlist_aray)+1):
        for attempt in product(wordlist_aray, repeat=i):
            value = ''.join(attempt)
            pbar.update()
            try:
                zip_file.extractall(pwd=bytes(value,'utf-8'))
            except:
                continue
            else:
                print("[+] Password found:", value)
                pbar.close()
                return
    
    print("[!] Password not found, try other wordlist.")
    pbar.close()
    return

brutforce(sys.argv[1], sys.argv[2])