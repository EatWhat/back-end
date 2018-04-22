# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class get_customer_name(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def get(self, customer_name):
    try:
      data = mysql.get_customer(customer_name)
      self.res_status['result'] = data
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['result'] = 'error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))

class get_restaurant_name(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def get(self, restaurant_name):
    try:
      data = mysql.get_restaurant(restaurant_name)
      self.res_status['result'] = data
      self.write(json.dumps(self.res_status))
      self.finish()

    except Exception as e:
      self.res_status['result'] = 'error'
      self.write(json.dumps(self.res_status))
      self.set_status(403)
      self.finish()
      print(traceback.format_exc(e))