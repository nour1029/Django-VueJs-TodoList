from django.urls import path, include
from rest_framework import routers
from .views import todo_list
from .api import TodoAPIViewset


app_name = 'todo'


router = routers.DefaultRouter()
router.register('todo', TodoAPIViewset)



urlpatterns = [
    path('api/', include(router.urls)),
    path('', todo_list),
]
