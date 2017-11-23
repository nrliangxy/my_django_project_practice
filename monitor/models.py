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
