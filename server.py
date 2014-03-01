import BaseHTTPServer

class handler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-Type', 'text/html')
		self.end_headers()
		self.wfile.write( open('index.html').read() )

def run(server_class=BaseHTTPServer.HTTPServer,
		handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
		addr = ('', 3000)
		httpd = server_class(addr, handler_class)
		httpd.serve_forever()
		
if __name__ == "__main__":
	run(handler_class=handler)