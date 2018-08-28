import json
import subprocess

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    data = json.loads(request.body)
    repository = data['repository']['name']
    if repository == 'blog':
        subprocess.check_output('git', '-C', '/root/blog', 'pull')
    return JsonResponse(data)
