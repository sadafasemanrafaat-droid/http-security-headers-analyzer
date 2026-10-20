from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(b"<h1>Test Server</h1>")


server = HTTPServer(("127.0.0.1", 9001), Handler)

print("Server running on port 9001")

server.serve_forever()