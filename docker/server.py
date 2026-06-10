from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		self.wfile.write(b'Backend Grupo 7 funcionando - Puerto 5000')

if __name__=='__main__':
	server = HTTPServer(('0.0.0.0', 5000), Handler)
	print('Backend corriendo en puerto 5000')
	server.serve_forever()
