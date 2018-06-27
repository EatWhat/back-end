# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class enter_page_table(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def get(self):
    try:
      customer_id = self.get_argument("customer_id")
      restaurant_id = self.get_argument("restaurant_id")
      table_No = self.get_argument("table_No")

      food = mysql.get_shopping_list(table_No, restaurant_id)
      data = mysql.get_restaurant(restaurant_id)
      data['shopping_list'] = food

      self.res_status['result'] = data
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['result'] = 'error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))

  def post(self):
    try:
      data = json.loads(self.request.body)
      if mysql.get_restaurant_status(data['restaurant_id']):
        mysql.write_table_order(data)
        self.res_status['state'] = 200
        self.res_status['detail'] = '下单成功'
      else:
        self.res_status['state'] = 202
        self.res_status['detail'] = '商家打烊'
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['state'] = 403
      self.res_status['detail'] = 'unknown error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))