from rest_framework.response import Response
from .models import Specialist, Client, Appointment
from django.forms import model_to_dict
from datetime import datetime, timedelta


def make_appointment(request):
    if not Specialist.objects.filter(name=request.data['specialist']):
        return Response({'post': "Специалист с данным именем отсутствует"})

    elif (datetime.strptime(request.data['start_appointment'], "%Y-%m-%dT%H:%M") >= datetime.strptime(
            request.data['end_appointment'], "%Y-%m-%dT%H:%M")):
        return Response({'post': "Время для записи введено некорректно"})

    elif (datetime.strptime(request.data['start_appointment'], "%Y-%m-%dT%H:%M") < (
            datetime.now() + timedelta(hours=3))):
        return Response({'post': "К сожалению, записаться на это время невозможно"})

    elif (Specialist.objects.filter(schedule__start_appointment__gt=request.data['start_appointment'],
                                    name=request.data['specialist']) or
          Specialist.objects.filter(schedule__end_appointment__lt=request.data['end_appointment'],
                                    name=request.data['specialist'])):
        return Response({'post': "К сожалению, в это время специалист не принимает"})

    elif (Appointment.objects.filter(start_appointment=request.data['start_appointment'],
                                     end_appointment=request.data['end_appointment'],
                                     specialist=request.data['specialist'])):
        return Response({'post': "К сожалению, это время уже занято"})

    elif (Appointment.objects.filter(start_appointment__gte=request.data['start_appointment'],
                                     start_appointment__lt=request.data['end_appointment'],
                                     specialist=request.data['specialist'])):
        return Response({'post': "К сожалению, это время уже занято"})


    elif (Appointment.objects.filter(start_appointment__lte=request.data['start_appointment'],
                                     end_appointment__gte=request.data['end_appointment'],
                                     specialist=request.data['specialist'])):
        return Response({'post': "К сожалению, это время уже занято"})

    elif (Appointment.objects.filter(start_appointment__lt=request.data['start_appointment'],
                                     end_appointment__gt=request.data['start_appointment'],
                                     specialist=request.data['specialist'])):
        return Response({'post': "К сожалению, это время уже занято"})
    else:
        new_appoint = Appointment.objects.create(
            start_appointment=request.data['start_appointment'],
            end_appointment=request.data['end_appointment'],
            specialist=request.data['specialist'],
            client=Client.objects.create(gender=request.data['client.gender'], name=request.data['client.name'])
        )

    return Response({'post': model_to_dict(new_appoint)})






