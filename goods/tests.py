from django.test import TestCase
from .models import *
import random

# cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']
# for cag in cags:
#     c = Category()
#     c.cag_name = cag
#     c.save()
#
# units = ['500克', '1kg', '2个', '3条', '1包', '5支', '1头', '2瓶']
#
# # 创建商品测试数据
# with open('E:\\PycharmProjects\\Django\\ttsx\\data.txt', 'r', encoding='utf-8') as f:
#
#     for goods_name in f:
#         # 创建商品对象
#         goods = GoodsInfo()
#         goods.goods_name = goods_name[:-1]
#         goods.goods_short = '此物极好，鲜嫩有品，值得购买'
#         goods.goods_desc = '此处就是商品的简介处，商品当日产出，当日销售，味美鲜美。'
#         goods.goods_cag_id = random.randint(1, len(cags))
#         goods.goods_image = 'goods/' + str(random.randint(1, 18)) + '.jpg'
#         goods.goods_price = random.randint(1, 999)
#         goods.goods_unit = units[random.randint(0, len(units) - 1)]
#
#         # 保存商品
#         goods.save()

# 创建广告数据
for index in range(1, 5):
    ad = Advertise()
    ad.ad_name = '广告'
    ad.ad_image = 'goods/ad/' + 'slide0' + str(index) + '.jpg'
    ad.ad_link = '#'
    ad.save()

for index in range(1, 3):
    ad = Advertise()
    ad.ad_name = '广告'
    ad.ad_image = 'goods/ad/' + 'adv0' + str(index) + '.jpg'
    ad.ad_link = '#'
    ad.save()