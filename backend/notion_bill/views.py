from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def bill(request):
    return JsonResponse({'a': 'ha'})
