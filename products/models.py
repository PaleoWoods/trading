from django.db import models, migrations


# 产品详情
class Product(models.Model):
	name = models.CharField(max_length=100)
