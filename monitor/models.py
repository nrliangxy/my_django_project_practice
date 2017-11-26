from django.db import models


# Create your models here.


class Buseiness(models.Model):
    caption = models.CharField(max_length=32)
    english_name = models.CharField(max_length=32, null=True)


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)  # 加上索引db_index查询会更快
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey("Buseiness", to_field="id")

#自动创建多对多关系表
class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField('Host')
#自定义关系表
# class HostToApp(models.Model):
#     h_obj = models.ForeignKey(to='Host', to_field='nid')
#     a_obj = models.ForeignKey(to='Application', to_field='id')
    