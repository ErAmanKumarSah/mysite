from django.db import models
from datetime import timedelta
from django.utils import timezone 
import datetime
# Create your models here.
class Aboutus(models.Model):
	"""docstring for about_us"""
	texting=models.CharField(max_length=500, null=True)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Question(models.Model):
	question_text = models.CharField(max_length=200, null=True)
	pub_date = models.DateTimeField('date published')
	
	def was_published_recently(self):
    #   		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #	was_published_recently.admin_order_field = 'pub_date'
	#was_published_recently.boolean = True
	#was_published_recently.short_description = 'Published recently?'	
		now = timezone.now()
		return now - datetime.timedelta(days = 1) <= self.pub_date <= now

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	
