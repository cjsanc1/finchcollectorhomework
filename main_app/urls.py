from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_details, name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='create_restaurant'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurant_update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurant_delete'),
    path('restaurants/<int:restaurant_id>/add_order/', views.add_order, name='add_order'),
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='create_tag'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
    path('restaurants/<int:restaurant_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('restaurants/<int:restaurant_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),

]
