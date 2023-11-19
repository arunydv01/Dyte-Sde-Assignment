from logs.models import LogModel, LogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class LogList(APIView):

    def get(self, request, format=None):
        logs = LogModel.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HTMXLogsList(generics.ListAPIView):
    queryset = LogModel.objects.all()
    serializer_class = LogSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        'level',
        # 'message',
        'resourceId',
        'timestamp',
        'traceId',
        'spanId',
        'commit',
        'metadata__parentResourceId',
    ]
    search_fields = [
        'level',
        'message',
        'resourceId',
        'timestamp',
        'traceId',
        'spanId',
        'commit',
        'metadata__parentResourceId',
    ]


class LogsListView(generics.ListAPIView):
    queryset = LogModel.objects.all()
    serializer_class = LogSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = [
        'level',
        # 'message',
        'resourceId',
        'timestamp',
        'traceId',
        'spanId',
        'commit',
        'metadata__parentResourceId',
    ]
    search_fields = [
        'level',
        'message',
        'resourceId',
        'timestamp',
        'traceId',
        'spanId',
        'commit',
        'metadata__parentResourceId',
    ]
