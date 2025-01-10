from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Attendee, Task
from .serializers import EventSerializer, AttendeeSerializer, TaskSerializer
from django.shortcuts import render

# Event Management APIs
@api_view(['POST'])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Attendee Management APIs
@api_view(['POST'])
def add_attendee(request):
    serializer = AttendeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_attendees(request):
    attendees = Attendee.objects.all()
    serializer = AttendeeSerializer(attendees, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_attendee(request, pk):
    try:
        attendee = Attendee.objects.get(pk=pk)
    except Attendee.DoesNotExist:
        return Response({'error': 'Attendee not found'}, status=status.HTTP_404_NOT_FOUND)
    
    attendee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Task Management APIs
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tasks(request, event_id):
    tasks = Task.objects.filter(event_id=event_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_task_status(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'index.html')
