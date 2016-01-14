from django.db import models, migrations


# 产品详情
class Products(models.Model):
	name = models.CharField(max_length=100)
	category = models.IntegerField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()


# 产品类别
class PDTCategory(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
