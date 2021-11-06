import os
import sys
import time
flag=0x00
for x in range(1,4):
    if os.system("pip install requests uuid time selenium os colorama sys") == 0:
        flag=flag | 0x03
        break
if flag==0x03:
    print("\nNow the installation is successful.")
else:
    print ("\nSome libraries have not been installed yet. Please run setup.py again")