from django.urls import path, include
from rest_framework import routers
from .api import TodoAPIViewset


app_name = 'todo'


router = routers.DefaultRouter()
router.register('todo', TodoAPIViewset)



urlpatterns = [
    path('', include(router.urls))
]
