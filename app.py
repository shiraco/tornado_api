import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        u_id = self.get_argument("u_id")
        q_seq = int(self.get_argument("q_seq"))

        qas = [
            {
                "q_seq": 1,
                "qa": {
                    "question": ("Q1", "げんきですか?"),
                    "answers": [("Q1A1", "はい"), ("Q1A2", "いいえ")],
                }
            },
            {
                "q_seq": 2,
                "qa": {
                    "question": ("Q2", "旅行好きですか?"),
                    "answers": [("Q2A1", "もちろん"), ("Q2A2", "どうかな")],
                }
            },
        ]

        obj = [qa for qa in qas if qa["q_seq"] == q_seq][0]

        my_json = json.dumps(obj, ensure_ascii=False)
        self.write(my_json)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()