from .models import Appointment
from rest_framework import generics
from .serializers import SpecialistSerializer, AppointmentSerializer
from .get_specialists_set import get_specialists_set
from .get_clients_set import get_clients_set
from .make_appointment import make_appointment


# To get a list of workers with ability to filter:
# Examples of query:
# 1) to take all specialists by specialization
# 'http://127.0.0.1:8080/service/list_of_workers?specialization=massagist'
# 2) to take
# 'http://127.0.0.1:8080/service/list_of_workers/?specialist_name=Prykhodko Mykola Ivanovych&year=2022&month=7&day=5'
class SpecialistApiView(generics.ListAPIView):
    serializer_class = SpecialistSerializer

    def get_queryset(self):
        # to get arguments from search line in browser(for filtration):
        specialization = self.request.query_params.get("specialization")
        specialist_name = self.request.query_params.get("specialist_name")
        year_appoint = self.request.query_params.get("year")
        month_appoint = self.request.query_params.get("month")
        day_appoint = self.request.query_params.get("day")
        hour_appoint = self.request.query_params.get("hour")
        minute_appoint = self.request.query_params.get("min")
        return get_specialists_set(specialization, specialist_name, year_appoint, month_appoint, day_appoint,
                                   hour_appoint, minute_appoint)


# To make appointment:
class Create_appointment(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        return make_appointment(request)


# to get a list of clients with ability to filter
class ClientlistApiView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        # to get arguments from search line in browser(for filtration)
        specialist_name = self.request.query_params.get("specialist_name")
        year_appoint = self.request.query_params.get("year")
        month_appoint = self.request.query_params.get("month")
        day_appoint = self.request.query_params.get("day")
        hour_appoint = self.request.query_params.get("hour")
        minute_appoint = self.request.query_params.get("min")

        return get_clients_set(specialist_name, year_appoint, month_appoint, day_appoint, hour_appoint, minute_appoint)
