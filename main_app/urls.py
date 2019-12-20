from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('resolutions/', views.ResolutionIndex.as_view(), name='index'),
   path('resolutions/<int:pk>/', views.ResolutionDetail.as_view(), name='detail'),
   path('users/<int:user_id>/resolutions/', views.user_resolutions, name='user_resolutions'),
   path('resolutions/create/', views.ResolutionCreate.as_view(), name='create'),
   path('resolutions/<int:resolution_id>/add_comment/', views.add_comment, name='add_comment'),
   path('resolutions/<int:comment_id>/delete_comment/', views.delete_comment, name='delete_comment'),
   path('resolutions/<int:pk>/update/', views.ResolutionUpdate.as_view(), name="update"),
   path('resolutions/<int:pk>/delete/', views.ResolutionDelete.as_view(), name="delete"),
   path('accounts/signup/', views.signup, name='signup'),
]