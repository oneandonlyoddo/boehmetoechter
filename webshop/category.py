from django.db import models
from shop_categories.models.defaults.category.base import ProductCategoryBase

class Category(ProductCategoryBase):
	catname = models.CharField(verbose_name='Kategoriename', max_length=255)
	class Meta:
		abstract = False
		app_label = 'app'
