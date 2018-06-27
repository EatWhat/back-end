import tornado, json, traceback, datetime
import mysql

class restaurant_status(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def post(self):
    try:
      data = json.loads(self.request.body)
      mysql.set_restaurant_status(data['restaurant_id'], data['status'])
      
      self.res_status['state'] = 200
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['state'] = 403
      self.res_status['detail'] = 'unknown error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))