import http.server
import json
import requests
from urllib.parse import urlparse

APP_KEY = '10093b49014c8ea6beffa0c267583e56'
MESSAGE_TEMPLATE = 2982

access_token = ''

def SendMessage(access_token, code, message):
    args = {'${SUBJECT}' : code, '${MESSAGE}' : message}
    args = json.dumps(args)
    headers = {'Authorization' : 'Bearer ' + access_token}
    r = requests.post('https://kapi.kakao.com/v1/api/talk/memo/send',
                      data = {'template_id' : MESSAGE_TEMPLATE,
                              'args' : args},
                      headers = headers)

#This class will handles any incoming request from
#the browser
class httpHandler(http.server.BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        parsed_path = urlparse(self.path)
        code = format(parsed_path.query).split('=')[1]

        r = requests.post('https://kauth.kakao.com/oauth/token',
                          data = {'grant_type' : 'authorization_code',
                                  'client_id' : APP_KEY,
                                  'redirect_uri' : 'http://localhost:8080/oauth',
                                  'code' : code})

        text = json.loads(r.text)
        access_token = text['access_token']
        print(access_token + '\n')

        SendMessage(access_token, '01111', 'this is message')

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(('Hello World !').encode('utf-8'))

        server.socket.close()
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = http.server.HTTPServer(('', 8080), httpHandler)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
