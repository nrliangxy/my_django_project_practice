from django.db import models


# Create your models here.


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, db_column='caption', unique=True)
    creat_time = models.DateTimeField(auto_now_add=True, null=True)
    up_time = models.DateTimeField(auto_now=True, null=True)


# cmdb_userinfo
class UserInfo(models.Model):
    # id列，自增，主键
    # 用户名列，字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64, help_text="pwd")
    gender = models.CharField(max_length=5)
    email = models.EmailField(max_length=19, null=True, blank=True)
    url = models.URLField(max_length=19, null=True)
    ip = models.GenericIPAddressField(max_length=19, null=True)
    user_type_choices = (
        (1, 'superuser'),
        (2, 'general_user'),
        (3, 'temp_user')
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=1)
    user_group = models.ForeignKey('UserGroup', to_field='uid', default=1)
