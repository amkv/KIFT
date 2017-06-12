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
            pid = line.split(' ')[1]
            os.system('kill %(pid)s' % {'pid': pid})
            print('process %(pid)s killed' % {'pid': pid})
            found = True
    if not found:
        print('no active servers')

if __name__ == "__main__":
    main()
