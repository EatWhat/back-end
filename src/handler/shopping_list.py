# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class modify_shopping_list(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def post(self):
    try:
      data = json.loads(self.request.body)
      slist = json.loads(mysql.get_shopping_list(data['table_No'], data['restaurant_id']))
      if not slist:
        slist = []
      slist += data['shopping_list']
      mysql.write_shopping_list(data['restaurant_id'], data['table_No'], slist)

      self.res_status['result'] = json.dumps(slist)
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['state'] = 403
      self.res_status['detail'] = 'unknown error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))