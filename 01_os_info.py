
import platform
import sys

info = 'OS info is \n{} \n\nPython version is {} {}'.format(platform.uname(), sys.version, platform.architecture())
print(info)
print('it is work!!!!')

with open('os_info.txt', 'w') as ff:
    ff.write(info)