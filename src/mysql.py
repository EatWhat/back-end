# !/usr/bin/env python3
# -*- coding: utf-8 -*- 

import pymysql, traceback, datetime, json
from settings import settings

def query(sql, *args):
  try:
    db = pymysql.connect(host = settings['db_host'], 
                     user = settings['db_user'], 
                     passwd = settings['db_password'], 
                     db = settings['db_database'],
                     charset='utf8')
    cursor = db.cursor()
    if len(args) != 0:
      cursor.execute(sql, args)
    else:
      cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
  except Exception as e:
    print(traceback.format_exc(e))

def insert_update(sql, *args):
  try:
    db = pymysql.connect(host = settings['db_host'], 
                     user = settings['db_user'], 
                     passwd = settings['db_password'], 
                     db = settings['db_database'],
                     charset='utf8')
    cursor = db.cursor()
    if len(args) != 0:
      cursor.execute(sql, args)
    else:
      cursor.execute(sql)
    db.commit()
    db.close()
  except Exception as e:
    print(traceback.format_exc(e))


def get_customer(customer_id):
  sql = 'select customer_id, phone, address from customer where customer_id = %s'
  data = query(sql, customer_id)[0]
  return {'customer_id': data[0], 'phone': data[1], 'address': data[2]}

def get_restaurant(restaurant_id):
  sql = 'select restaurant_id, restaurant_name, phone, food from restaurant where restaurant_id = %s'
  data =  list(query(sql, restaurant_id)[0])
  return {'restaurant_id': data[0], 'restaurant_name': data[1], 'phone': data[2], 'food': json.loads(data[3])}

def write_order(data, price):
  sql = 'insert into orders (customer_id, restaurant_id, date, price, food) values (%s, %s, %s, %s, %s)'
  insert_update(sql, data['customer_id'], data['restaurant_id'], data['date'], price, json.dumps(data['food']))

def count_price(restaurant_id, food_list):
  sql = 'select food from restaurant where restaurant_id = %s'
  food_price = json.loads(query(sql, restaurant_id)[0][0])
  price = 0
  for food in food_list:
    for each in food_price:
      if food['food_id'] == each['food_id']:
        price += each['price'] * food['num']
        break
  return price

def get_shopping_list(table_No, restaurant_id):
  # return: table status, food
  sql = 'select food from shopping_list where table_No = %s and restaurant_id = %s'
  data =  list(query(sql, table_No, restaurant_id))
  if len(data) == 0:   # haven't created this shopping_list
    sql = 'insert into shopping_list (table_No, restaurant_id) values (%s, %s)'
    insert_update(sql, table_No, restaurant_id)
    return None

  return data[0][0]
  
if __name__ == '__main__':
  food = [{'food_id':1,'num':2},{'food_id':2,'num':1}]
  print(count_price('zyf', food))