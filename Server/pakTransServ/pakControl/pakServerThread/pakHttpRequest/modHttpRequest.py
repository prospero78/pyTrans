# -*- coding: utf8 -*-
"""
Модуль предоставляет обраточик Http-запросов.
"""

import cgi
from http.server import BaseHTTPRequestHandler

a="""
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        Привет !
    </body>
</html>

"""
class clsHttpRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        print('client adress=', self.client_address,  self.requestline)
        self.send_response(200)
        self.send_header('Сontent-type'.encode('utf8'), 'text/html'.encode('utf8'))
        self.end_headers()
        
        self.wfile.write(a.encode('utf8'))
    
    def do_POST(self):
        """
        При использовании модуля cgi -- происходит разбор параметров запроса.
        """
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
            if ctype == "multipart/form-data":
                query = cgi.parse_multipart(self.rfile, pdict)

            self.send_response(200)
            self.end_headers()
            #upfile = query.get("file")
            params = " np output.exe"
            p = query.get("encryption")
            if p[0] == "aes":
                params += " sf 1"
            elif p[0] == "rc5":
                params += " sf 2"
            elif p[0] == "xor":
                params += " sf 3"
            else:
                params += " sf 0"
            p = query.get("hw_bind")
            if p[0] == "yes":
                p = query.get("hw_bind_serial")
                assert len(p[0]) == 8
                params += " sn " + p[0]
            else:
                params += " sn 0"
            p = query.get("passwd")
            assert len(p[0]) > 0
            params += " pass " + p[0]
            p = query.get("pack")

            if p[0] == "yes":
                params += " pack 1"
            else:
                params += " pack 0"
            self.wfile.write('Download results.')
        except Exception:
            pass
