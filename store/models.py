from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class bijou(models.Model):
	name=models.CharField(max_length=250)
	color=models.CharField(max_length=20)
	price=models.IntegerField()
	image_link=models.CharField(max_length=750)

	def get_absolute_url(self):
		return reverse('store:bijou_details',kwargs={'name':self.name})

	def __str__(self):
		return self.name + "-" + self.color

class sub_bijou(models.Model):
	bijouType = models.ForeignKey(bijou, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	quantity = models.IntegerField()
	favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.name + " from " + self.bijouType.name