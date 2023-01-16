"account urls.py"
from django.urls import path
from .views import RegisterUserView, DeleteUserView, UserListView, UserRetrieveView


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('delete/', DeleteUserView.as_view()),
    path('user/', UserListView.as_view(),),
    path('retrieve/<int:pk>/', UserRetrieveView.as_view()),
]
