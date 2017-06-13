import os
import sys
import subprocess

def main():
    server = "src/server_src/server.py"
    found = False
    output = subprocess.check_output('ps')
    text = output.split('\n')
    for line in text:
        if server in line:
            text = line.split(' ')
            for i in text:
                try:
                    pid = int(i)
                    os.system('kill %(pid)s' % {'pid': pid})
                    print('process %(pid)s killed' % {'pid': pid})
                    found = True
                    break
                except:
                    continue
    if not found:
        print('no active servers')

if __name__ == "__main__":
    main()
