from django.db import models


# Create your models here.

class GifTemplateTag(models.Model):
    name = models.CharField(max_length=16, verbose_name='标签名称')


class GifTemplate(models.Model):
    img_url = models.URLField(verbose_name='图片URL')
    # json parse
    caption_template = models.TextField(verbose_name='字幕模板')
    tags = models.ManyToManyField(to=GifTemplateTag, verbose_name='标签', null=True, blank=True)
