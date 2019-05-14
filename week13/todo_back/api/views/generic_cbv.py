from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import TaskList, Task
from api.serializers import TaskListSerializer2, TaskSerializer
from django.contrib.auth.models import User


class Tasklist2(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    http_method_names = ['get']

class TasklistList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)
        # return TaskList.objects.all()

    def get_serializer_class(self):
        return TaskListSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TasklistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


class TaskListTasks(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        # tasklist = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        # return tasklist.task_set.filter(task_list__owner=self.request.user)
        return Task.objects.all()
