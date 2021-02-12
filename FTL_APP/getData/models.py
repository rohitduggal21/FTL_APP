from django.db import models

class User(models.Model):	
	id = models.CharField(primary_key=True,max_length=6)
	real_name = models.CharField(max_length=30)
	tz = models.CharField(max_length=30)

class Activities(models.Model):	
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
