# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class modify_shopping_list(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def post(self):
    try:
      data = json.loads(self.request.body)
      mysql.write_customer_shopping_list(data['shopping_list'], data['table_No'], data['restaurant_id'], data['customer_id'])

      slist = mysql.get_table_shopping_list(data['table_No'], data['restaurant_id'])
      # all individual shopping lists of this desk
      # [[{'food_id':1, 'num':1}], [{'food_id':2, 'num':1}]]

      slist = [json.loads(_[0]) for _ in slist]
      tmp_dict = {}
      for each in slist:
        for ee in each:
          if ee['food_id'] not in tmp_dict:
            tmp_dict[ee['food_id']] = 0
          tmp_dict[ee['food_id']] += ee['num']

      slist = []
      for x, y in tmp_dict.items():
        slist.append({'food_id': x, 'num': y})

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