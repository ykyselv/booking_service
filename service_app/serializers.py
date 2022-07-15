from datetime import datetime, timedelta
from rest_framework import serializers
from .models import Specialist, Client, Schedule, Appointment, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Schedule
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SpecialistSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True)

    class Meta:
        model = Specialist
        fields = ['name', 'specialization', 'schedule']


class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Appointment
        fields = ['start_appointment', 'end_appointment', 'specialist', 'client']

    def create(self, validated_data):
        specialist = validated_data['specialist']
        start_appointment = validated_data['start_appointment']
        end_appointment = validated_data['end_appointment']
        client_gender = validated_data['client']['gender']
        client_name = validated_data['client']['name']


        if not Specialist.objects.filter(name=specialist):
            raise serializers.ValidationError ("Специалист с данным именем отсутствует")

        elif (start_appointment >= end_appointment):
            raise serializers.ValidationError ("Время для записи введено некорректно")

        elif (start_appointment < (datetime.now() + timedelta(hours=3))):
            raise serializers.ValidationError ("К сожалению, записаться на это время невозможно")


        elif not Specialist.objects.filter(schedule__start_appointment__lte=start_appointment,
                                                schedule__end_appointment__gte=end_appointment,name=specialist):

            raise serializers.ValidationError("К сожалению, в это время специалист не принимает")


        elif (Appointment.objects.filter(start_appointment=start_appointment,
                                         end_appointment=end_appointment,
                                         specialist=specialist)):
            raise serializers.ValidationError("К сожалению, это время уже занято")

        elif (Appointment.objects.filter(start_appointment__gte=start_appointment,
                                         start_appointment__lt=end_appointment,
                                         specialist=specialist)):
            raise serializers.ValidationError("К сожалению, это время уже занято")

        elif (Appointment.objects.filter(start_appointment__lte=start_appointment,
                                         end_appointment__gte=end_appointment,
                                         specialist=specialist)):
            raise serializers.ValidationError("К сожалению, это время уже занято")

        elif (Appointment.objects.filter(start_appointment__lt=start_appointment,
                                         end_appointment__gt=start_appointment,
                                         specialist=specialist)):

            raise serializers.ValidationError("К сожалению, это время уже занято")


        else:
            new_appoint = Appointment.objects.create(
                start_appointment=start_appointment,
                end_appointment=end_appointment,
                specialist=specialist,
                client=Client.objects.create(gender=client_gender, name=client_name)
            )

        return new_appoint

