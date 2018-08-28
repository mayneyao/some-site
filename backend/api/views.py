from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def webhook(request):
    data = json.loads(request.body)
    return JsonResponse(data)