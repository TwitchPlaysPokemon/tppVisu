'''
Created on 11.05.2015

@author: Felk
'''

import json
import re
import socket

from tppVisu.api import buildDictMatch
from tppVisu.move import Move
from tppVisu.pokemon import Pokemon
from tppVisu.util import Stats, Environment


def handleRequest(data, sock):
    match = re.match(b'GET /visu/([0-9,]+)/([0-9,]+)\sHTTP/1', data)
    if match:
        blueIDs = [int(ID) for ID in match.group(1).split(b',')]
        redIDs = [int(ID) for ID in match.group(2).split(b',')]
        # TODO replace these 2 lines with the actual pokemon data retrieved from the IDs
        # They need to be packed into the visualizer's own Pokemon objects
        blues = [Pokemon(1, 'A', 'fire', None, Stats(50, 60, 70, 80, 90, 100), [Move('Tackle', '', 'normal', 1, 70, 10, 90)], 0, '')]
        reds = [Pokemon(2, 'B', 'water', None, Stats(50, 60, 70, 80, 90, 100), [Move('Tackle', '', 'normal', 1, 70, 10, 90)], 0, '')]
        result = buildDictMatch(blues, reds, Environment(weather='none'))
        sock.sendall(b"""HTTP/1.1 200 OK
Cache-Control: no-cache, must-revalidate
Expires: Mon, 26 Jul 1997 05:00:00 GMT
Access-Control-Allow-Origin: *
Connection: close
Content-Type: application/json

""" + json.dumps(result, indent=4).encode('ascii'))  # For Python3: indent='    ' or something.
    else:
        sock.sendall(b"""HTTP/1.1 404 Not Found
Connection: close

""")

def main(host='localhost', port=8080):
    # create a server socket.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP (2-way) connection
    sock.bind((host, port))  # occupy the port this socket shall be listening to
    sock.listen(1)  # don't queue up any requests
    print('Started simple HTTP server for /visu API requests')
    
    # Loop forever, listening for requests:
    while True:
        csock, _ = sock.accept()  # This function blocks, until there actually is an incoming connection. Returns the socket for it
        data = csock.recv(1024)  # This function blocks, until the data from the request has arrived.
        handleRequest(data, csock)  # make someone handle this request
        csock.close()  # close the connection again. this was a temporary, disposable connection.
    
if __name__ == '__main__':
    main()
