from django.urls import path
from . import views

urlpatterns = [
    # Event Management
    path('', views.index, name='index'),
    path('events/', views.get_events, name='get_events'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:pk>/update/', views.update_event, name='update_event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete_event'),
    
    # Attendee Management
    path('attendees/', views.get_attendees, name='get_attendees'),
    path('attendees/add/', views.add_attendee, name='add_attendee'),
    path('attendees/<int:pk>/delete/', views.delete_attendee, name='delete_attendee'),

    # Task Management
    path('tasks/<int:event_id>/', views.get_tasks, name='get_tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/update/', views.update_task_status, name='update_task_status'),
]
