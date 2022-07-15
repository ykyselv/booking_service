from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Appointment
from rest_framework import generics
from .serializers import SpecialistSerializer, AppointmentSerializer
from .get_set import get_set


# To get a list of workers with ability to filter:
# Examples of query:
# 1) to take all specialists by specialization
# 'http://127.0.0.1:8000/service/list_of_workers?specialization=massagist'
# 2) to take specialists by name
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
        return get_set("Specialist", year_appoint, month_appoint, day_appoint,
                                   hour_appoint, minute_appoint, specialist_name, specialization)


# To make appointment:
class Create_appointment(APIView):
    def get(self, request):
        appoint=Appointment.objects.all()
        return Response (AppointmentSerializer(appoint, many=True).data)

    def post(self,request):
        serializer=AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})



# to get a list of clients with ability to filter

# query example with all params:
# http://127.0.0.1:8000/service/list_of_clients/?specialist_name=Prykhodko%20Mykola%20Ivanovych&year=2022&month=7&day=14&hour=9&min=0
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

        return get_set("Appointment", year_appoint, month_appoint, day_appoint, hour_appoint, minute_appoint, specialist_name)






