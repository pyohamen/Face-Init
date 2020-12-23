from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
app_name = 'blog'

urlpatterns= [

    path('group/',views.user_list),#blog/api/v1/  get post사용
    path('group/<int:article_pk>',views.user_detail),# get put delete
    path('v1/',views.access_detail_v1),#한개씩 받아오는것
    path('v2/<int:article_pk>', views.access_detail_v2),#10개씩 받아오는것
    path('docs/',get_swagger_view(title="API문서"),name="swagger"),
    path('camera/<int:article_pk>',views.camera_on),
]