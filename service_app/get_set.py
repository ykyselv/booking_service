from .models import Appointment
from .models import Specialist


def get_set(*args):
    model = args[0]
    year_appoint = args[1]
    month_appoint = args[2]
    day_appoint = args[3]
    hour_appoint = args[4]
    minute_appoint = args[5]
    specialist_name = args[6]

    if model == 'Specialist':
        specialization = args[7]

    if model == 'Specialist':
        if not specialist_name and not specialization:
            return Specialist.objects.all()

    elif model == 'Appointment':
        if not specialist_name:
            return (Appointment.objects.all())

    if not year_appoint:
        if model == 'Specialist':
            if specialist_name:
                return (Specialist.objects.filter(name=specialist_name))
            elif specialization:
                return (Specialist.objects.filter(specialization=specialization))
        elif model == 'Appointment':
            return (Appointment.objects.filter(specialist=specialist_name))

    elif year_appoint and not month_appoint:
        if model == 'Specialist':
            if specialist_name:
                return Specialist.objects.filter(name=specialist_name,
                                                 schedule__start_appointment__year=year_appoint).distinct()
            elif specialization:
                return Specialist.objects.filter(specialization=specialization,
                                                 schedule__start_appointment__year=year_appoint).distinct()

        elif model == 'Appointment':
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint))

    elif year_appoint and month_appoint and not day_appoint:
        if model == 'Specialist':
            if specialist_name:
                return Specialist.objects.filter(name=specialist_name,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint).distinct()
            elif specialization:
                return Specialist.objects.filter(specialization=specialization,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint).distinct()
        elif model == 'Appointment':
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint))

    elif year_appoint and month_appoint and day_appoint and not hour_appoint:
        if model == 'Specialist':
            if specialist_name:
                return Specialist.objects.filter(name=specialist_name,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint,
                                                 schedule__start_appointment__day=day_appoint).distinct()

            elif specialization:
                return Specialist.objects.filter(specialization=specialization,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint,
                                                 schedule__start_appointment__day=day_appoint).distinct()

        elif model == 'Appointment':
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint,
                                               start_appointment__day=day_appoint))

    elif year_appoint and month_appoint and day_appoint and hour_appoint and not minute_appoint:
        if model == 'Specialist':
            if specialist_name:
                return Specialist.objects.filter(name=specialist_name,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint,
                                                 schedule__start_appointment__day=day_appoint,
                                                 schedule__start_appointment__hour=hour_appoint).distinct()
            elif specialization:
                return Specialist.objects.filter(specialization=specialization,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint,
                                                 schedule__start_appointment__day=day_appoint,
                                                 schedule__start_appointment__hour=hour_appoint).distinct()
        elif model == 'Appointment':
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint,
                                               start_appointment__day=day_appoint,
                                               start_appointment__hour=hour_appoint))

    elif year_appoint and month_appoint and day_appoint and hour_appoint and minute_appoint:
        if model == 'Specialist':
            if specialist_name:
                return Specialist.objects.filter(name=specialist_name,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint,
                                                 schedule__start_appointment__day=day_appoint,
                                                 schedule__start_appointment__hour=hour_appoint,
                                                 schedule__start_appointment__minute=minute_appoint).distinct()
            elif specialization:
                return Specialist.objects.filter(specialization=specialization,
                                                 schedule__start_appointment__year=year_appoint,
                                                 schedule__start_appointment__month=month_appoint,
                                                 schedule__start_appointment__day=day_appoint,
                                                 schedule__start_appointment__hour=hour_appoint,
                                                 schedule__start_appointment__minute=minute_appoint).distinct()

        elif model == 'Appointment':
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint,
                                               start_appointment__day=day_appoint,
                                               start_appointment__hour=hour_appoint,
                                               start_appointment__minute=minute_appoint))
