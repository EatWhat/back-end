# !/usr/bin/env python3

import tornado, json, traceback, datetime
import mysql

class modify_shopping_list(tornado.web.RequestHandler):

  def initialize(self):
    self.res_status = {}

  def post(self):
    try:
      data = json.loads(self.request.body)
      slist = mysql.get_shopping_list(data['table_No'], data['restaurant_id'])
      if not slist:
        slist = []
      else:
        slist = json.loads(slist)
      slist += data['shopping_list']
      ids = set([x['food_id'] for x in slist])
      tmp_dict = {}
      for each in slist:
        if each['food_id'] not in tmp_dict:
          tmp_dict[each['food_id']] = 0
        tmp_dict[each['food_id']] += each['num']

      slist = []
      for x, y in tmp_dict.items():
        slist.append({'food_id':x, 'num':y})

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