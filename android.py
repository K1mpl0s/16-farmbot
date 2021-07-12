import sys
import platform
import requests
import os
import subprocess

if '3.7' not in str(sys.version):
    uname = platform.machine()
    clean_uname = None
    print(uname)
    if 'aarch' in uname:
        clean_uname = uname.replace('aarch', 'arch')
    elif 'arm' in uname:
        uname = uname.replace(uname, 'arm')
        clean_uname = uname
    else:
        clean_uname = uname
    r = requests.get(f"https://github.com/Termux-pod/termux-pod/raw/main/{clean_uname}/python/python-3.7.5/python_3.7.5_{uname}.deb", stream=True, allow_redirects=True)
    f = open(f"./python_3.7.5_{uname}.deb", 'wb')
    for chunk in r.iter_content(1024):
        f.write(chunk)
    f.close()
    subprocess.run(f"dpkg -i ./python_3.7.5_{uname}.deb", shell=True, check=False)
    print('\n\n')
    subprocess.run(f"pip3 install six colorama requests pyCryptodomex==3.9.9 lxml bs4 werkzeug", shell=True, check=False)
    print('\n\n')
    print('[!] successfully installed python3.7')
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
folder_found = False
if os.path.isdir('./storage/'):
    if os.path.isdir('./storage/downloads/'):
        folders = sorted((f for f in os.listdir('./storage/downloads/')), key=lambda f : os.path.getmtime(os.path.join('./storage/downloads/', f)), reverse=True)
        for i in folders:
            if i == '16 Farmbot':
                os.chdir(f"./storage/downloads/16 Farmbot/")
                if os.path.isdir('./source/'):
                    folder_found = True
                    wd = os.getcwd()
                    os.chdir(f"./storage/downloads/16 Farmbot/source/")
                    subprocess.run(f"python3 bot.pyc", shell=True, check=False)
                else:
                    print('[!] unable to locate source in "16 Farmbot"')
                break
            elif '16-' in i and os.path.isdir('./storage/downloads/{i}'):
                os.chdir(f"./storage/downloads/{i}/")
                if os.path.isdir(f"./16 Farmbot/"):
                    if os.path.isdir('./storage/downloads/{i}/16 Farmbot/source/'):
                        folder_found = True
                        wd = os.getcwd()
                        os.chdir(f"./storage/downloads/{i}/16 Farmbot/source/")
                        subprocess.run(f"python3 bot.pyc", shell=True, check=False)
                    else:
                        print('[!] unable to locate "source" folder in "16 Farmbot"')
                else:
                    print('[!] unable to locate "16 Farmbot" folder in 16 Folder')
                break
        if not folder_found:
            print('[!] unable to locate 16 Folder in "downloads"')
    else:
        print('[!] unable to locate "downloads"')
else:
    print('[!] unable to locate "storage"\n...make sure you ran "termux-setup-storage"')
