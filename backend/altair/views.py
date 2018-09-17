from rest_framework import serializers, viewsets

from .models import GifTemplate, GifTemplateTag


# Create your views here.


class GifTemplateTagSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GifTemplateTag
        fields = '__all__'


class GifTemplateSerializers(serializers.ModelSerializer):
    class Meta:
        model = GifTemplate
        fields = '__all__'


class GifTemplateViewsets(viewsets.ModelViewSet):
    queryset = GifTemplate.objects.all()
    serializer_class = GifTemplateSerializers
