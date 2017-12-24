from django.template import Library


register = Library()


# 创建过滤器
# 注册过滤器（方式二）
@register.filter('create_image_name')
def create_image_name(index):
    return 'images/banner0' + str(index) +'.jpg'
# 注册过滤器（方式一）
# register.filter('create_image_name',create_image_name)


# 创建model_id 过滤器
@register.filter('create_model_id')
def create_model_id(index):
    return 'model0'+ str(index)

# 创建字符串转换int型
@register.filter('convert_str_to_int')
def convert_str_to_int(my_str):
    return int(my_str)