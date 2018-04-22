# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class order(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def post(self):
    try:
      print(self.request.body)
      data = json.loads(self.request.body)
      print(data)
      price = mysql.count_price(data['restaurant_id'], data['food'])
      print(price)
      mysql.write_order(data, price)
      self.res_status['state'] = 200
      self.res_status['detail'] = '下单成功'
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['state'] = 403
      self.res_status['detail'] = 'unknown error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))