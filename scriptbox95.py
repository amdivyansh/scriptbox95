#!/usr/bin/env python3
from colorama import Fore
import os
import time
os.system('cls||clear')
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
version = str(3)
con= f'\n{blue}Scriptbox95 con>>{white} '
go = f"""
{green}                              $$\            $$\     $$\                                  $$$$$$\  $$$$$$$\  
                              \__|           $$ |    $$ |                                $$  __$$\ $$  ____| 
 $$$$$$$\  $$$$$$$\  $$$$$$\  $$\  $$$$$$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$\   $$\       $$ /  $$ |$$ |      
$$  _____|$$  _____|$$  __$$\ $$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ \$$\ $$  |      \$$$$$$$ |$$$$$$$\  
\$$$$$$\  $$ /      $$ |  \__|$$ |$$ /  $$ | $$ |    $$ |  $$ |$$ /  $$ | \$$$$  /        \____$$ |\_____$$\ 
 \____$$\ $$ |      $$ |      $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |  $$ | $$  $$<        $$\   $$ |$$\   $$ |
$$$$$$$  |\$$$$$$$\ $$ |      $$ |$$$$$$$  | \$$$$  |$$$$$$$  |\$$$$$$  |$$  /\$$\       \$$$$$$  |\$$$$$$  |
\_______/  \_______|\__|      \__|$$  ____/   \____/ \_______/  \______/ \__/  \__|       \______/  \______/ 
                                  $$ |                                                                       
                                  $$ |                                                                       
                                  \__|                                        [{blue}console{yellow}]                 
{yellow}                                                                              {cyan}[{blue}\x42\x79 {green}amdivyansh{cyan}]
{white}


"""
print(go)
time.sleep(2)
print(con+"Setting up..")
import requests
import zipfile
import io
import re
import os
from update import download_latest_release_repository
def setup():
    os.system('cls||clear')
    print(go)
    time.sleep(2)
    print(con+"Chacking For Updates..")
    from main.dta import version, getdata
    response2 = requests.get('https://api.github.com/repos/amdivyansh/scriptbox95_source_data/releases/latest')
    release_info2 = response2.json()
    ver = release_info2['tag_name']
    print(con+"Current version is ["+version+']')
    if ver > version or getdata == 1:
        print(con + "Update available..")
        print(con+"New version is ["+ver+']')
        print(con + "Updating..")
        download_latest_release_repository()
        print(con + "Successfully Updated")
        print(con + "please restart...")
    else:
        print(con+"Updated..")
        os.chdir('./main')
        os.system('python3 main.py')
        #exec(open('main.py').read())

setup()
#download_latest_release_repository('amdivyansh', 'scriptbox95_source_data', 'main')
