import os
import sys
import webbrowser
import time

SRC = 'src/'
SERVER_PATH = SRC + 'server_src/'
SERVER = 'server.py'
URL = 'http://127.0.0.1'

def set_port(argv):
    """convert argument, check number in range, return port"""
    port = int(argv)
    if port <= 100 or port >= 65535:
        print_usage()
    else:
        return port

def print_usage():
    """show usage and exit"""
    print ('usage: runner.py <port number>')
    sys.exit(0)

def main(argv):
    global SRC
    global SERVER_PATH
    global SERVER
    global URL
    if len(argv) != 2:
        print_usage()
    port = set_port(argv[1])
    os.system('make re')
    os.system('python %(server)s %(num)s &' % {'server': SERVER_PATH + SERVER, 'num': port})
    time.sleep(2)
    webbrowser.open_new_tab(str(URL) + ':' + str(port))

if __name__ == "__main__":
    main(sys.argv)
