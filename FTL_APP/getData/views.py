from django.http import JsonResponse
from .models import User

def returnData(request):	
	try:	
		result = {'ok':True,'members':[]}
		for user in User.objects.all():	
			member = {
				'id':user.id, 
				'real_name':user.real_name,
				'tz': user.tz,
				'activity_periods': [{'start_time':ob['start_time'],'end_time':ob['end_time']} for ob in user.activities_set.values()]
				}
			result['members'].append(member)
	except:	
		result = {'ok':False,'members':[]}
	return JsonResponse(result)
