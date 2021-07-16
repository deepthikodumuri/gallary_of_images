from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, viewsets
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from .models import Image,Tag
from rest_framework.decorators import action
from .serializers import TagSerializer, ImageSerializer
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image as image_module


class RotateView(APIView):
    def post(self, request):
        print(request.POST)
        id = request.POST.get('id')
        direction = request.POST.get('direction')
        print(direction)
        img = Image.objects.get(id=id)
        original_photo = BytesIO(img.name.read())
        rotated_photo = BytesIO()
        image = image_module.open(original_photo)
        print(image.format)
        format = image.format
        if direction == 'left':
            image = image.rotate(-90)
        else:
            image=image.rotate(90)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(rotated_photo,format)
        print(img.name.path)
        img.name.save(img.name.name, ContentFile(rotated_photo.getvalue()))
        img.save()
        return HttpResponseRedirect('/index')

class ImageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    serializer_class = ImageSerializer
    
    @action(detail=True)
    def get(self, request):
        queryset = Image.objects.all()
        tags = Tag.objects.all()
        return Response({'images': queryset,'tags':tags})
    
    # @action(methods=['post'], detail=True)
    def post(self,request):
        img = request.FILES['img']
        tag_ids = request.POST.getlist('tags[]')
        tags_list = Tag.objects.filter(pk__in=tag_ids)
        new_image = Image.objects.create(name=img)
        new_image.tag.set(tags_list)
        new_image.save()
        return HttpResponseRedirect(self.request.path_info)