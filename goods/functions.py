from utils.common import *
from users.models import *
from carts.models import *


# 更新用户记录
def update_user_browse_record(request):

    # 判断用户是否登录
    if not user_is_login(request):
        return

    # 如果用户登录
    # 记录最大条数
    limit = 5

    # 1. 如果商品存在，则只更新商品浏览记录的update_time
    # 获得商品ID
    goods_id = get(request,'id')
    user_id = get_session(request, 'uid')
    try:
        record = RecordBrowse.objects.get(browse_goods_id=goods_id, browse_user_id=user_id)
        record.save()

    # 2.如果商品不存在
    except RecordBrowse.DoesNotExist:

        record = RecordBrowse.objects.filter(browse_user_id=user_id).order_by('update_time')
        # 2.1 判断用户浏览记录数据条数是否达到5条，如果没有达到，则插入新记录
        if record.count() < limit:

            rb = RecordBrowse()
            rb.browse_goods_id = goods_id
            rb.browse_user_id = user_id
            rb.save()

        else:
            rb = record[0]
            rb.browse_goods_id = goods_id
            rb.save()

# 获得商品总数量
def get_total_cart_num(view_func):

   def wrapper(request, *args, **kwargs):
       total = 0
       if user_is_login(request):
           carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))
           for cart in carts:
               total += cart.cart_amount

       request.total = total

       return view_func(request, *args, **kwargs)

   return wrapper