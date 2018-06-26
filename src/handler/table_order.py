# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class enter_page(tornado.web.RequestHandler):

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