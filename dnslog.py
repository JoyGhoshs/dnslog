import requests
from colorama import Fore, Back, Style
import argparse

print(f"""
   ___           __                  
  / _ \___  ___ / /__  ___ _ _______ 
 / // / _ \(_-</ / _ \/ _ `// __/ _ |
/____/_//_/___/_/\___/\_, (_)__/_//_/ [ {Fore.RED}DNSLOG.CN{Style.RESET_ALL} ]
                     /___/           
    System00 security bangladesh
""")

def dns_log_domain():
    session = requests.Session()
    domain = session.get('http://www.dnslog.cn/getdomain.php')
    global cookies,d
    d = domain.cookies['PHPSESSID']
    cookies = {'PHPSESSID': domain.cookies['PHPSESSID']}
    print(f'[ {Fore.RED}Subdomain{Style.RESET_ALL} ] {Style.BRIGHT}{domain.text}{Style.RESET_ALL}')
def dns_log_log():
    session = requests.Session()
    log = session.get('http://www.dnslog.cn/getrecords.php', cookies=cookies)
    return log.text
def loop():
    if (len(dns_log_log()) == 2):
        loop()
    else:
        logs = list(eval(dns_log_log()))
        for log in logs:
            print(f'[ {Fore.RED}LOG{Style.RESET_ALL} ] {Fore.GREEN}{log[1]}{Fore.RESET}  - {log[2]}')

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wait", help="how many hit it should wait for ex: -w 2/--wait 2", type=int, default=1)
    args = parser.parse_args()
    print(f'[ {Fore.YELLOW}info{Style.RESET_ALL} ] {Fore.GREEN}Generating Subdomain{Fore.RESET}')
    dns_log_domain()
    print(f'[ {Fore.YELLOW}PHPESSID{Style.RESET_ALL} ] {d} {Fore.RESET}')
    for hit in range(args.wait):
        print(f'[ {Fore.YELLOW}info{Style.RESET_ALL} ] Waiting For Hit {hit+1}/{args.wait}{Fore.RESET}')
        print('')
        loop()
except KeyboardInterrupt:
    print(f'[ {Fore.RED}Exit{Style.RESET_ALL} ]')
    exit()
except Exception as e:
    print(f'[ {Fore.RED}Error{Style.RESET_ALL} ] {Fore.YELLOW}{e}{Fore.RESET}')
    exit()