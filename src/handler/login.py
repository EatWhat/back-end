import tornado, json, traceback, datetime
import mysql

class restaurant_login(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def post(self):
    try:
      data = json.loads(self.request.body)
      res = mysql.check_restaurant(data['restaurant_id'], data['password'])
      if res:
        self.res_status['state'] = 200
      else:
        self.res_status['state'] = 201

      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['state'] = 403
      self.res_status['detail'] = 'unknown error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))