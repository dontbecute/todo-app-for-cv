from django.urls import include , path
from .views import TodoAPIList, TodoAPIDetalis

urlpatterns = [
    path('<int:pk>/', TodoAPIDetalis.as_view(), name='todo_list'),
    path('' , TodoAPIList.as_view() , name="todo_list")
]