from django.urls import path
from .views import (NewsList, NewDetail, PostCreate, PostUpdate, PostDelete, ProfilUpdate, add_subscribe, del_subscribe,
                    subscribe)


urlpatterns = [
   path('', NewsList.as_view(), name='post_list'),
   path('<int:pk>', NewDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('profil/', ProfilUpdate.as_view(), name='profil'),
   path('add_subscribe/<int:pk>/', add_subscribe, name='add_subscribe'),
   path('delete_subscribe/<int:pk>/', del_subscribe, name='delete_subscribe'),
   path('subscribe/<int:pk>/', subscribe, name='subscribe'),

]