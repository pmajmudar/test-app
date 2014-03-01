import SimpleHTTPServer
import SocketServer

PORT = 3000
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/search':
			self.path = '/'
			
		f = self.send_head()
		if f:
			self.copyfile(f, self.wfile)
			f.close()

httpd = SocketServer.TCPServer(("",PORT), MyHandler)

		
if __name__ == "__main__":
	print "Serving at port: ", PORT
	httpd.serve_forever()