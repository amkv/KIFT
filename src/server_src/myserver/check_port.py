import socket
import sys

def set_port(argv):
    """convert argument, check number in range, return port"""
    port = int(argv)
    if port <= 100 or port >= 65535:
        print_usage()
    else:
        return port

def check_port_is_open(host, port):
    """Check is socket port opened"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print "Port %(port)s is already opened." % {'port': port}
        sys.exit(1)
