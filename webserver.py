# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        bootstrap = """<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">"""
        self.wfile.write(bytes("<html><head><title>Test Web Server ini</title>"+bootstrap+"</head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>Web Server Python</h1><table class=\"table\">", "utf-8"))
        self.wfile.write(bytes("<tr><th>id</th><th>suhu</th><th>kelembaban</th></tr>", "utf-8"))
        import mysql.connector
        mydb = mysql.connector.connect(
          host="localhost",
          user="mpi",
          password="mpi",
          database="mpitest"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tabelnum")
        myresult = mycursor.fetchall()
        for x in myresult:
            row = "<tr><td>"+str(x[0])+"</td><td>"+str(x[1])+"</td><td>"+str(x[2])+"</td></tr>"
            self.wfile.write(bytes(row, "utf-8"))
        self.wfile.write(bytes("</table></body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Klik link ini : http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")