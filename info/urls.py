from django.urls import path
from . import views

urlpatterns = [
    path('student-list/', views.TestView.as_view(), name='studentlist'),
    path('student-list/<int:pk>', views.TestView.as_view(), name='studentlist'),
]