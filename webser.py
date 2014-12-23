import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.websocket
import logging

from tornado.options import define, options

define('port', default=8888,help='run on the given port',type=int)
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
		
class PoemHandler(tornado.web.RequestHandler):
	def get(self):
		name = self.get_argument('text',default='word')
		self.write("Hello, %s!" % name)
	
	def post(self):
		data = {'name':'zuoyuan','content':'Hello word!'}
		self.set_header('Content-Type','text/plain')
		self.render('poem.html',data=data)
	def write_error(self, status_code, **kwargs):
		self.write(str(status_code) + ':Not found!USB')
class WsHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True
	def open(self):
		pass
	def on_close(self):
		pass
	def on_message(self, message):
		logging.info("got message %r", message)
		self.write_message('{"msg":"%s"}' % message)
		
def main():
	tornado.options.parse_command_line()
	application = tornado.web.Application([
		(r"/", IndexHandler),
		(r"/poem", PoemHandler),
		(r"/ws",WsHandler)
	],
	template_path='./tpl')
	httpd = tornado.httpserver.HTTPServer(application)
	httpd.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
	