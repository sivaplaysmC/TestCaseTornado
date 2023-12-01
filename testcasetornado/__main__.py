import http.server as http
import multipart

import io



class HttpHandler(http.BaseHTTPRequestHandler):
    def do_GET(self) :
        self.send_response(200)
        self.send_header("Hi", "There")
        self.end_headers()
        self.wfile.write(b"Hi There nigga\n")


    def do_POST(self) :

        self.send_response(200);
        self.end_headers();
        self.wfile.write(b"")

        def on_file(file):
            fh :io.BytesIO = file.file_object
            fh.seek(0, 0);
            print(f"file.in_memory {file.in_memory}")
            print("file Contents ::" )
            print(fh.read(file.size).decode())

        on_field = lambda field : ...

        multipart.parse_form(self.headers, self.rfile, on_file=on_file, on_field= on_field)



address = ("0.0.0.0", 8081)

server = http.HTTPServer(address, HttpHandler );

try :
    server.serve_forever()
except KeyboardInterrupt :
    print("\nShutting Down server ._.")
finally :
    server.server_close()


