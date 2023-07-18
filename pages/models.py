from django.db import models

# Create your models here. 

class Page(models.Model):
	"""docstring for Page"""
	title=models.CharField(max_length=60)
	permalink=models.CharField(max_length=12, unique=True)
	update_date=models.DateTimeField('Last Updated')
	bodytext=models.TextField('Page Content', blank=True)

	def __str__(self):
		return self.title


class Books(models.Model):
	title=models.CharField(max_length=100)
	linktoamazon=models.URLField(max_length=200)
	mycomments=models.TextField(blank=True)
