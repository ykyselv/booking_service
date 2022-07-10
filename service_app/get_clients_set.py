from .models import Appointment


def get_clients_set(*args):
    specialist_name = args[0]
    year_appoint = args[1]
    month_appoint = args[2]
    day_appoint = args[3]
    hour_appoint = args[4]
    minute_appoint = args[5]

    # To get list of clients by specialist name
    if specialist_name:
        if not year_appoint:
            return (Appointment.objects.filter(specialist=specialist_name))

        elif year_appoint and not month_appoint:
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint))

        elif year_appoint and month_appoint and not day_appoint:
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint))

        elif year_appoint and month_appoint and day_appoint and not hour_appoint:
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint,
                                               start_appointment__day=day_appoint))

        elif year_appoint and month_appoint and day_appoint and hour_appoint and not minute_appoint:
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint,
                                               start_appointment__day=day_appoint,
                                               start_appointment__hour=hour_appoint))

        elif year_appoint and month_appoint and day_appoint and hour_appoint and minute_appoint:
            return (Appointment.objects.filter(specialist=specialist_name, start_appointment__year=year_appoint,
                                               start_appointment__month=month_appoint,
                                               start_appointment__day=day_appoint, start_appointment__hour=hour_appoint,
                                               start_appointment__minute=minute_appoint))

    else:
        # To get general list of clients
        return (Appointment.objects.all())
