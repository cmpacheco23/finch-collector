from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('dogs/', views.dog_index, name='dog-index'),
  path('dogs/<int:dog_id>', views.dog_detail, name='dog-detail'),
  path('dogs/create/', views.DogCreate.as_view(), name='dog-create'),
  path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dog-update'),
  path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dog-delete'),
  path('dogs/<int:dog_id>/add-walk/', views.add_walk, name='add-walk'),
  path('bowls/create/', views.BowlCreate.as_view(), name='bowl-create'),
  path('bowls/<int:pk>/', views.BowlDetail.as_view(), name='bowl-detail'),
  path('bowls/', views.BowlList.as_view(), name='bowl-index'),
  path('bowls/<int:pk>/update/', views.BowlUpdate.as_view(), name='bowl-update'),
  path('bowls/<int:pk>/delete/', views.BowlDelete.as_view(), name='bowl-delete'),
  path('dogs/<int:dog_id>/assoc-bowl/<int:bowl_id>/', views.assoc_bowl, name='assoc-bowl'),
  path('accounts/signup/', views.signup, name='signup')
]