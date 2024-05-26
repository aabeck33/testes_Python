import re
import os
import json
import base64
import sqlite3
import win32crypt
import shutil
import string
import time
from itertools import combinations_with_replacement
from random import random, choice
from Cryptodome.Cipher import AES
from datetime import timezone, datetime, timedelta
from colorama import Fore

MINCHAR = 10
MAXCHAR = 32
SIMBOLS =  "@$!%*#?&(){}<>^~+=|/,.;:?´`¨_\'\"-" #[]\
MINSIMBOLS = "@$!%*#?&"



def criatepasswd():
    values = string.ascii_letters + string.digits + string.punctuation
    passwd = ""
    for i in range(MAXCHAR):
        passwd += choice(values)

    return passwd


def testpasswd(values, size):
    result = {}
    passwd = ''
    ini_t = time.time()
    comb = combinations_with_replacement(values, size)
    fin_t = time.time()
    elapsedtime = fin_t - ini_t
    result = {"Quantidade: ": len(list(comb)), "Tempo:": elapsedtime}

    return result


def checkpwd(passwd: str, minchar: int, maxchar: int, simbols: str) -> dict:
    """
    Verifies if a passwd is string or weak. The rules are:
        Deve ter pelo menos um número;
        Deve ter pelo menos um caractere maiúsculo e um minúsculo;
        Deve ter pelo menos um símbolo especial -> @$!%*#?&;
        Deve ter entre minchar a maxchar caracteres.

    Args:
        passwd (str): passwd to be verified
        minchar (int): Minimum character quantity
        maxchar (int): Maximum character quantity
    """
    result = {}
    reg = f"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[{simbols}])[A-Za-z\\d{simbols}]{{{minchar},{maxchar}}}$"
    pat = re.compile(reg)
    mat = re.search(pat, passwd)
    if mat:
        if re.search(r'(.)\1\1\1', passwd):
            result = {"isok":False, "msg":'Password is invalid: Same character repeats three or more times in a row.'}
        elif passwd == "\n" or passwd == " ":
            result = {"isok":False, "msg":'Password cannot be a newline or a single space.'}
        elif re.search(r'(..)(.*?)\1', passwd):
            result = {"isok":False, "msg":'Password is invalid: Same string pattern repetition.'}
        else:
            result = {"isok":True, "msg":'Password is valid.'}
    else:
        result = {"isok":False, "msg":'Password is invalid.'}

    return result

def chrome_date_and_time(chrome_date):
    """
    Chrome_date format is 'year-month-day
    hr:mins:seconds.milliseconds
    This will return datetime.datetime Object

    Args:
        chrome_date (datetime): data a ser convertida

    Returns:
        datetime: data convertida
    """
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_date)

def fetching_encryption_key():
    """
    Local_computer_directory_path will look like this below
        C: => Users => <Your_Name> => AppData => Local => Google => Chrome => User Data => Local State

    Returns:
        _type_: decrypted key
    """
    local_computer_directory_path = os.path.join(
      os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
      
    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)
  
    # decoding the encryption key using base64
    encryption_key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])
      
    # remove Windows Data Protection API (DPAPI) str
    encryption_key = encryption_key[5:]

    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]

def password_decryption(password, encryption_key):
    """
    Decriptor of password

    Args:
        password (_type_): password to decrypt
        encryption_key (_type_): the key

    Returns:
        string: _description_
    """
    try:
        iv = password[3:15]
        password = password[15:]
          
        # generate cipher
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
          
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"

def chrome_passwd():
    key = fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)

    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()

    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")

    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]

        if user_name or decrypted_password:
            print(f"Main URL: {main_url}")
            print(f"Login URL: {login_page_url}")
            print(f"User name: {user_name}")
            print(f"Decrypted Password: {decrypted_password}")
            print(checkpwd(decrypted_password, MINCHAR, MAXCHAR, SIMBOLS))
        else:
            continue

        if date_of_creation != 86400000000 and date_of_creation:
            print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}")
          
        if last_usuage != 86400000000 and last_usuage:
            print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
        print("=" * 100)
    cursor.close()
    db.close()

    try:
        # trying to remove the copied db file as well from local computer
        os.remove(filename)
    except:
        pass


if __name__ == '__main__':
    print(Fore.RED + '')
    print(checkpwd("Geekfc$5vfdc", MINCHAR, MAXCHAR, SIMBOLS))
    print(Fore.WHITE + '\n')
    #chrome_passwd()
    #print(criatepasswd())
    #vals = string.ascii_letters + string.digits #+ string.punctuation
    #print(testpasswd(vals, 6))