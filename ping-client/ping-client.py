import sys
import socket

ECHO_SERVER_PORT = 7


def ping(ip_address):
    '''
    Ping an ip address.

    Args:
        ip_address (string): IP Address

    Returns:
        bool: True for success, False otherwise.
    '''

    MESSAGE = "ping"
    BUFFER_SIZE = 1024

    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the IP address and port
        sock.connect((ip_address, ECHO_SERVER_PORT))

        # Send echo message
        sock.sendall(MESSAGE)

        # Wait for the response
        response = sock.recv(BUFFER_SIZE)

        return True
    except:
        return False
    finally:
        sock.close()

def get_ip_address(host):
    '''
    Resolve IP address of a host

    Args:
        host (string): Host name
    Returns
        string bool: IP address on success, False otherwise.
    '''

    try:
        addr_info = socket.getaddrinfo(host, ECHO_SERVER_PORT)

        if len(addr_info) == 0:
            return False

        return addr_info[0][4][0]
    except:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: ping-client destination"
        sys.exit()

    host = sys.argv[1]
    ip_address = get_ip_address(host)

    if ping(ip_address) == True:
        print host + " is alive"
    else:
        print host + " is unreachable"
