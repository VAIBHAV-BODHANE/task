from django.shortcuts import render
from info.models import Student

from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk, *args, **kwargs):
        qs = Student.objects.get(pk=pk)
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, *args, **kwargs):
        qs = Student.objects.get(pk=pk)
        qs.delete()
        return Response('Record has been deleted!')