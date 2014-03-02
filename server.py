import SimpleHTTPServer
import SocketServer
import re

PORT = 3000
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		class_path = re.compile(r'/classify*')
		if class_path.match(self.path) or self.path == '/login':
			self.path = '/'
			
		f = self.send_head()
		if f:
			self.copyfile(f, self.wfile)
			f.close()

httpd = SocketServer.TCPServer(("",PORT), MyHandler)

		
if __name__ == "__main__":
	print "Serving at port: ", PORT
	httpd.serve_forever()