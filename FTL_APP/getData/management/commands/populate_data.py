from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from faker import Faker
import datetime
import random
from FTL_APP.getData.models import *

class Command(BaseCommand):	
	help = 'Populate dummy data'

	def handle(self, *args, **kwargs):	
		for i in range(random.randint(1,10)):	
			user = User(id=get_random_string(length=6),real_name=Faker().name(),tz=Faker().timezone())
			user.save()
			for i in range(random.randint(1,5)):	
				start = datetime.datetime.now()
				end = start + datetime.timedelta(minutes=random.randint(1,15))
				user.activities_set.create(start_time=start,end_time=end)
		self.stdout.write("Data Populated")
