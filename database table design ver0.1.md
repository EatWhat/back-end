# database table design ver0.1

---
## dinners
|字段|类型|说明|
|:--:|:--:|:--:|
|d_id|int unsigned not null auto_increment|主键，用餐者id|
|username|varchar(32) not null|用户名。通常就是微信号|
|phone|varchar(16) not null|电话|
|address|json|送餐地址。ex.{{'address_id':1,'place':'肾六楼下'},{'address_id':1,'place':'公教楼'}}|

**注：看需求要不要加点额外信息。比如红包啥的**

## sellers
|字段|类型|说明|
|:--:|:--:|:--:|
|s_id|int unsigned not null auto_increment|主键，商家id|
|username|varchar(32) not null|用户名。不必是微信号|
|food|json|出售中食物。ex. {{'food_id':1, 'food_name': '麻辣香锅', 'food_price': 25, 'num':1}, {'food_id':2, 'food_name': '台湾卤肉饭', 'food_price': 13, 'num':1}}|

**注：商家的注册信息，营业执照等信息不放在数据库里**

## orders
|字段|类型|说明|
|:--:|:--:|:--:|
|o_id|int unsigned not null auto_increment|主键，订单id|
|d_id|int unsigned not null|外键，用餐者id|
|s_id|int unsigned not null|外键，商家id|
|date|varchar(32) not null|下单时间|
|price|int unsigned|订单金额|
|food|json|具体食物。ex.{{'food_id':1, 'food_name': '麻辣香锅', 'food_price': 25, 'num':1},{'food_id':3, 'food_name': '白饭', 'food_price': 2, 'num':1}}|
|comment|json|用户评价。ex.{'star':5, 'text': '我永远喜欢冬阴功', 'hide_name':True}|

## cookies
|字段|类型|说明|
|:--:|:--:|:--:|
|c_id|int unsigned not null auto_increment|主键，id|
|d_id|int unsigned not null|外键，用餐者id|
|s_id|int unsigned not null|外键，商家id|
|food|json|购物车里的东西。ex.{{'food_id':1, 'food_name': '麻辣香锅', 'food_price': 25, 'num':1},{'food_id':3, 'food_name': '白饭', 'food_price': 2, 'num':1}}|

by two2er.