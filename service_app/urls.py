from django.urls import path
from . import views

urlpatterns = [
    # For clients:
    #     To get a list of workers:
    path('list_of_workers/', views.SpecialistApiView.as_view(), name='list_of_workers'),
    #     To make appoint:
    path('makeappoint/', views.Create_appointment.as_view(), name='makeappoint'),

    # Для специалистов:
    path('list_of_clients/', views.ClientlistApiView.as_view(), name='list_of_clients')
]
