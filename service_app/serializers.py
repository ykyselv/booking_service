from rest_framework import serializers
from .models import Specialist, Client, Schedule, Appointment, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['start_appointment', 'end_appointment']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SpecialistSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer()
    location = LocationSerializer()

    class Meta:
        model = Specialist
        fields = ['name', 'specialization', 'schedule', 'location']


class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Appointment
        fields = ['start_appointment', 'end_appointment', 'specialist', 'client']
