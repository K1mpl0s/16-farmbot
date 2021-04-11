import sys
import platform
import requests
import os
import subprocess
if '3.7' not in str(sys.version):
    uname = platform.machine()
    clean_uname = None
    if 'aarch' in uname:
        clean_uname = uname.replace('aarch', 'arch')
    else:
        clean_uname = uname
    r = requests.get(f"https://github.com/Termux-pod/termux-pod/raw/main/{clean_uname}/python/python-3.7.5/python_3.7.5_{uname}.deb", stream=True, allow_redirects=True)
    f = open(f"./python_3.7.5_{uname}.deb", 'wb')
    for chunk in r.iter_content(1024):
        f.write(chunk)
    f.close()
    subprocess.run(f"dpkg -i ./python_3.7.5_{uname}.deb", shell=True, check=False)
    print('[!] successfully installed python3.7\nplease run "android.py" again...')
    exit()
else:
    if os.path.isdir('./storage/downloads/16-2.0.9.3/16 Farmbot/source'):
        subprocess.run('cd "storage/downloads/16-2.0.9.3/16 Farmbot/source/bot.pyc"', shell=True, check=False)
        subprocess.run('python3 "16-2.0.9.3/16 Farmbot/source/bot.pyc"', shell=True, check=False)
    elif os.path.isdir('./storage/downloads/16 Farmbot/source'):
        subprocess.run('cd "storage/downloads/16 Farmbot/source/bot.pyc"', shell=True, check=False)
        subprocess.run('python3 "16 Farmbot/source/bot.pyc"', shell=True, check=False)
    else:
        print('[!] unable to locate 16 folder in "downloads"')
