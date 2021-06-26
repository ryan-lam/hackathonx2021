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
    path('course/<str:code>/<int:index>', views.course, name="course"),
    path('course/<str:code>', views.course, name="course"),

    path('discussion/<str:item_pk>', views.discussion, name="discussion"),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),

    ####### TESTING ######################## 
    path('img/<int:pk>', views.test_image),
    path('test_all_img', views.test_all_img, name="TEST ALL IMG"),
]

if True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
