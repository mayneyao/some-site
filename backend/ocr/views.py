from PIL import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .core import get_text_from_img

REPLACE_DICT = {}


# Create your views here.
@csrf_exempt
def api(request):
    # api for wechat-read book note

    try:
        d = request.POST
        img_url = d.get('url', None)
        if img_url and img_url != 'false':
            img = img_url
        else:
            image_file = request.FILES['image']
            img = Image.open(image_file.file)

        data = {
            'img': img,
            'lang': d.get('lang')
        }
        res = get_text_from_img(**data)
        return JsonResponse(res)
    except Exception:
        return JsonResponse({'error': ''})
