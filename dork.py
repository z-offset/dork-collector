# simple dorking script.
# author: Ismail Aatif @CyberLiberty.

from googlesearch import search
from random import randint
from time import sleep
from datetime import datetime
import argparse, time, sys, os, platform, re

# Banner:
banner = """
Author: Ismail Aatif @CyberLiberty \t\t\tversion: 1.0
 _______                ______   _______  _        _______  _______ 
(  ____ )|\     /|     (  __  \ (  ___  )| \    /\(  ____ \(  ____ )
| (    )|( \   / )     | (  \  )| (   ) ||  \  / /| (    \/| (    )|
| (____)| \ (_) /_____ | |   ) || |   | ||  (_/ / | (__    | (____)|
|  _____)  \   /(_____)| |   | || |   | ||   _ (  |  __)   |     __)
| (         ) (        | |   ) || |   | ||  ( \ \ | (      | (\ (   
| )         | |        | (__/  )| (___) ||  /  \ \| (____/\| ) \ \__
|/          \_/        (______/ (_______)|_/    \/(_______/|/   \__/
"""
print("\n")
print(banner)


# handle arguments:
parser = argparse.ArgumentParser()
parser.add_argument("-d", dest="dork", help="Dork to use for search.")
parser.add_argument("-l", dest="limit", help="Number of search results.")
parser.add_argument("-o", dest="file", help="Save ouput results to file.")
args = parser.parse_args()


# clean terminal:
def clean():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# main function:
def main(dork, limit=10, save2file=False):
    clean()
    print(banner)
    try:
        print(
            "\nSearch Started @ {}".format(
                datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            )
        )
        print("=" * 36)
        z = 0
        for title in search(dork, stop=limit, user_agent=None, country="", pause=2.0):
            z += 1
            print("[{:02d}] Found: {}".format(z, title))
            if save2file:
                out = open(args.file, "a")
                out.write(title + "\n")
                out.close()
            sleep(0.5)
    except Exception as e:
        print("[-] Problem Detected.")
        check_for_ban = re.search(r"429", str(e))
        if check_for_ban:
            print("[-] Google Has Banned us For Sending Too Many Requests.")
        sys.exit(0)


if __name__ == "__main__":
    try:
        if args.dork is None:
            print("\ndork.py -h (For help on usage.)")
            sys.exit(0)
        else:
            limitNumber = int(args.limit) if (args.limit != None) else 10
            saveOutput = True if (args.file != None) else False
            main(dork=args.dork, limit=limitNumber, save2file=saveOutput)
    except KeyboardInterrupt:
        print("[CTRL-C] Detected, Terminating.")
        sys.exit(0)
