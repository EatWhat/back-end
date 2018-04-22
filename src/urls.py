# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from handler.get_name import get_customer_name, get_restaurant_name
from handler.order import order

url_patterns = [
  (r"/customer_name=(\w+)", get_customer_name),
  (r"/restaurant_name=(\w+)", get_restaurant_name),
  (r"/", order),
]