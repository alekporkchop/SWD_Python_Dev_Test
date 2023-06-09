from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoList(APIView):
    def get(self, request, format=None):
        toDos = ToDo.objects.all()
        serializer = ToDoSerializer(toDos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ToDoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class ToDoListDetail(APIView):

    def get_object(self, id):
        try:
            return ToDo.objects.get(pk=id)
        except ToDo.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        toDo = self.get_object(id)
        serializer = ToDoSerializer(toDo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, format=None):
        toDo = self.get_object(id)
        serializer = ToDoSerializer(toDo, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        toDo = self.get_object(id)
        toDo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)