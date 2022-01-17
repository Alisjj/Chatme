from . import views

from django.urls import path, re_path

app_name = 'chat'

urlpatterns = [
    path('', views.ChatListView.as_view()),
    path('create/', views.ChatCreatetView.as_view()),
    path('<pk>', views.ChatDetialView.as_view()),
    path('<pk>/update/', views.ChatUpdateView.as_view()),
    path('<pk>/delete/', views.ChatDestroyView.as_view()),
]
