import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backend.utils.ocr_api.ocr import get_text_from_img

REPLACE_DICT = {}

# Create your views here.
@csrf_exempt
def api(request):
    # api for wechat-read book note
    data = json.loads(request.body)
    text = get_text_from_img(**data)

    book_name, content = text.split('\n\n')
    book_name = book_name.replace('\n', '')
    content = content.replace('\n', '').replace('_', '一')
    res = {
        'book_name': book_name,
        'content': content
    }
    return JsonResponse(res)
