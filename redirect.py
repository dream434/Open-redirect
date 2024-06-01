import requests
from colorama import Fore, Style
import argparse


def banner ():
     ban='''  ____                   ____           ___                __ 
  / __ \____  ___  ____  / __ \___  ____/ (_)_______  _____/ /_
 / / / / __ \/ _ \/ __ \/ /_/ / _ \/ __  / / ___/ _ \/ ___/ __/
/ /_/ / /_/ /  __/ / / / _, _/  __/ /_/ / / /  /  __/ /__/ /_  
\____/ .___/\___/_/ /_/_/ |_|\___/\__,_/_/_/   \___/\___/\__/  
    /_/                                          Author:jhonson              
                                                 Email:wannaajhonson@gmail.com

'''
     print(Fore.YELLOW + Style.BRIGHT +f'{ban}' + Style.RESET_ALL+'\n\n') 

banner ()
def main(list,url):
   try :
     with open(list, 'r') as file:
       for files in file:
           strip_file=files.strip()
           session= requests.session()
           url_destination=url
           headers =["X-Host","X-Forwarded-Server","X-HTTP-Host-Override","Host","X-Forwarded-For","Referer","Content-Location","Link","Set-Cookie","X-Real-IP","X-Proxy-URL","X-Forwarded-Proto","X-Remote-Addr","X-Forwarded-Host","X-Origin"
           ]

           for i in headers:

               
               data={i:url_destination}
               r=requests.get(strip_file,headers=data,allow_redirects=False,timeout=30)
               
               if r.status_code==301 or r.status_code==301 :
                      if args.url  in r.headers['location']: 
                         print(Fore.GREEN + Style.BRIGHT +f'{strip_file} Vuln Found headers vuln is {i}' + Style.RESET_ALL) 
                      else: 
                         print(Fore.RED + Style.BRIGHT +f'{strip_file} No Vuln Found headers {i}' + Style.RESET_ALL) 
               
               else:
                  print(Fore.RED + Style.BRIGHT +f'{strip_file} No Vuln Found headers {i}' + Style.RESET_ALL) 
    
   except requests.exceptions.MissingSchema:
            print('')
   except requests.exceptions.ConnectionError:
            print(Fore.BLUE + Style.BRIGHT +f'{strip_file} DNS problem or data connexion' + Style.RESET_ALL) 
 
if __name__=='__main__':
     
       parser = argparse.ArgumentParser(description="Openredirect")
       parser.add_argument("-list", "--list", dest="list", help="list urls", required=True)
       parser.add_argument("-url", "--url", dest="url", help="url redirection", required=True)     
       args = parser.parse_args()

       
       main(args.list, args.url)
     


     
     
