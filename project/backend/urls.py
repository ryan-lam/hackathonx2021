from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    ####### REAL URLS ######################
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('explore', views.explore, name="explore"),
    path('load/<str:code>', views.load, name="load"),
    path('load/<str:code>/<int:index>', views.getCourseItem, name="getItem"),

    ####### TESTING ######################## 
    path('img/<int:pk>', views.test_image),
    path('test_all_img', views.test_all_img, name="TEST ALL IMG"),
]

if True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
