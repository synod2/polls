import os
import sys

if sys.argv < 2: 
    print("input commit's name plz")
    sys.exit(1)
else :
    os.system("git add .")
    os.system("git commit -m \""+sys.argv[1]+"\"")
    os.system("git push -u origin master")