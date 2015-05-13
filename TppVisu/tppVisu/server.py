'''
Created on 11.05.2015

@author: Felk
'''

import socket
import re
from tppVisu.api import buildDictMatch
from tppVisu.pokemon import Pokemon
from tppVisu.move import Move
from tppVisu.util import Stats, Environment
import json

def main():
    host = '127.0.0.1'
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1) # don't queue up any requests
    print('Started simple HTTP server for /visu API requests')
    
    # Loop forever, listening for requests:
    while True:
        csock, _ = sock.accept()
        req = csock.recv(1024)
        match = re.match(b'GET /visu/([0-9,]+)/([0-9,]+)\sHTTP/1', req)
        if match:
            blueIDs = [int(ID) for ID in match.group(1).split(b',')]
            redIDs = [int(ID) for ID in match.group(2).split(b',')]
            # TODO replace these 2 lines with the actual pokemon data retrieved from the IDs
            # They need to be packed into the visualizer's own Pokemon objects
            blues = [Pokemon(1, 'A', 'fire', None, Stats(50,60,70,80,90,100), [Move('Tackle', '', 'normal', 1, 70, 10, 90)], 0, '')]
            reds = [Pokemon(2, 'B', 'water', None, Stats(50,60,70,80,90,100), [Move('Tackle', '', 'normal', 1, 70, 10, 90)], 0, '')]
            result = buildDictMatch(blues, reds, Environment(weather='none'))
            csock.sendall(b"""HTTP/1.1 200 OK
Cache-Control: no-cache, must-revalidate
Expires: Mon, 26 Jul 1997 05:00:00 GMT
Access-Control-Allow-Origin: *
Connection: close
Content-Type: application/json

"""+json.dumps(result, indent='    ').encode('ascii'))
        else:
            csock.sendall(b"""HTTP/1.1 404 Not Found
Connection: close

""")
        csock.close()
    
if __name__ == '__main__':
    main()