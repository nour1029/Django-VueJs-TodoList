from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets



class TodoAPIViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


