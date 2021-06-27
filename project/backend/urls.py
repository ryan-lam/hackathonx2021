from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    ####### REAL URLS ######################
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('explore/', views.explore, name="explore"),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('course/<str:code>/<int:index>', views.course, name="course"),
    path('course/<str:code>', views.course, name="course"),
    path('save', views.save, name='save'),
    path('saved', views.saved, name='saved'),
    path('user-admin', views.user_admin, name='user-admin'),
    path('admin_delete', views.admin_delete, name='admin_delete'),
    path('admin_delete/posts', views.admin_delete_posts, name='admin_delete_posts'),
    path('admin_edit_page', views.admin_edit_page, name='admin_edit_page'),
    path('admin_edit', views.admin_edit, name='admin_edit'),

    path('admin_add_page', views.admin_add_page, name='admin_add_page'),
    path('admin_add', views.admin_add, name='admin_add'),



    path('discussion', views.discussion, name="discussion"),
    path('discussion/<str:item_pk>', views.discussion, name="discussion"),

    path('clear', views.clear, name="clear session"),
    ####### TESTING ######################## 
    path('img/<int:pk>', views.test_image),
    path('test_all_img', views.test_all_img, name="TEST ALL IMG"),
]

if True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
