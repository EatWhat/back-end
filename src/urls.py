# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from handler.get_name import get_customer_name, get_restaurant_name
from handler.order import order
from handler.table_order import enter_page_table
from handler.takeout_order import enter_page_takeout
from handler.shopping_list import modify_shopping_list
from handler.login import restaurant_login
from handler.restaurant_status import restaurant_status

url_patterns = [
  (r"/customer_name=(\w+)", get_customer_name),
  (r"/restaurant_name=(\w+)", get_restaurant_name),
  (r"/order", order),
  (r"/table_order", enter_page_table),
  (r"/takeout_order", enter_page_takeout),
  (r"/shopping_list", modify_shopping_list),
  (r"/restaurant_login", restaurant_login),
  (r"/restaurant_status", restaurant_status)
]