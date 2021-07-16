from django.urls import include, path,re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('index/',views.ImageView.as_view(), name='images'),
    path('rotate/', views.RotateView.as_view(), name='rotate')
]