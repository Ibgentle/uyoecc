from django.urls import path
from . import views


app_name = 'staff'


urlpatterns = [
        path('', views.index, name='index'),
        path('agents/', views.agent_list, name='agent_list'),
        path('<int:id>/', views.agent_detail, name='agent_detail'),
        path('management', views.management_list, name='management_list'),
        path('<int:id>/', views.management_detail, name='management_detail'),
        path('others/', views.other_list, name='other_list'),
        path('<int:id>/', views.other_detail, name='other_detail'),
        path('timetable-generator/', views.timetable_generator,
            name='timetable_generator'),
        ]
