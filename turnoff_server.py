import os
import sys
import subprocess

output = subprocess.check_output('ps')
text = output.split('\n')

for line in text:
    if "src/server_src/server.py" in line:
        pid = line.split(' ')[1]
        os.system('kill %(pid)s' % {'pid': pid})
        print('process %(pid)s killed' % {'pid': pid})
        sys.exit(0)
print('no active servers')
