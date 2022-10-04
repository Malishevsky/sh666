from django.urls import path , re_path
from .views import index, CreateAuto, get_mechanical, get_post, UpdateAuto, DeleteAuto,filter_post,get_filter

urlpatterns = [
    path('', index, name='index'),
    path('create/', CreateAuto.as_view() ,name='create'),
    path('post/<slug:slug>/del', DeleteAuto.as_view() ,name='del_auto'),
    path('post/<slug:slug>/edit',UpdateAuto.as_view(),name='edit'),
    path('transmission/<int:id>',get_mechanical,name='get_mechanical'),
    path('post/<slug:post_slug>',get_post,name='poster'),
    path('filter/<slug:engine_slug>/<slug:trans_slug>',filter_post,name='filter'),
    re_path('filter/\D+/\D+/',get_filter)

]
