from .models import Specialist


def get_specialists_set(*args):
    specialization = args[0]
    specialist_name = args[1]
    year_appoint = args[2]
    month_appoint = args[3]
    day_appoint = args[4]
    hour_appoint = args[5]
    minute_appoint = args[6]

    # To get a list of workers by specialization
    if specialization:
        if year_appoint and not month_appoint:
            return (Specialist.objects.filter(specialization=specialization,
                                              schedule__start_appointment__year=year_appoint))

        elif year_appoint and month_appoint and not day_appoint:
            return (
                Specialist.objects.filter(specialization=specialization, schedule__start_appointment__year=year_appoint,
                                          schedule__start_appointment__month=month_appoint))

        elif year_appoint and month_appoint and day_appoint and not hour_appoint:
            return (
                Specialist.objects.filter(specialization=specialization, schedule__start_appointment__year=year_appoint,
                                          schedule__start_appointment__month=month_appoint,
                                          schedule__start_appointment__day=day_appoint))

        elif year_appoint and month_appoint and day_appoint and hour_appoint and not minute_appoint:
            return (
                Specialist.objects.filter(specialization=specialization, schedule__start_appointment__year=year_appoint,
                                          schedule__start_appointment__month=month_appoint,
                                          schedule__start_appointment__day=day_appoint,
                                          schedule__start_appointment__hour=hour_appoint))


        elif year_appoint and month_appoint and day_appoint and hour_appoint and minute_appoint:
            return (
                Specialist.objects.filter(specialization=specialization, schedule__start_appointment__year=year_appoint,
                                          schedule__start_appointment__month=month_appoint,
                                          schedule__start_appointment__day=day_appoint,
                                          schedule__start_appointment__hour=hour_appoint,
                                          schedule__start_appointment__minute=minute_appoint))

        else:
            return (Specialist.objects.filter(specialization=specialization))

    # To get a list of workers by specialist name
    elif specialist_name:

        if year_appoint and not month_appoint:
            return (Specialist.objects.filter(name=specialist_name, schedule__start_appointment__year=year_appoint))

        elif year_appoint and month_appoint and not day_appoint:
            return (Specialist.objects.filter(name=specialist_name, schedule__start_appointment__year=year_appoint,
                                              schedule__start_appointment__month=month_appoint))

        elif year_appoint and month_appoint and day_appoint and not hour_appoint:
            return (Specialist.objects.filter(name=specialist_name, schedule__start_appointment__year=year_appoint,
                                              schedule__start_appointment__month=month_appoint,
                                              schedule__start_appointment__day=day_appoint))

        elif year_appoint and month_appoint and day_appoint and hour_appoint and not minute_appoint:
            return (Specialist.objects.filter(name=specialist_name, schedule__start_appointment__year=year_appoint,
                                              schedule__start_appointment__month=month_appoint,
                                              schedule__start_appointment__day=day_appoint,
                                              schedule__start_appointment__hour=hour_appoint))


        elif year_appoint and month_appoint and day_appoint and hour_appoint and minute_appoint:
            return (Specialist.objects.filter(name=specialist_name, schedule__start_appointment__year=year_appoint,
                                              schedule__start_appointment__month=month_appoint,
                                              schedule__start_appointment__day=day_appoint,
                                              schedule__start_appointment__hour=hour_appoint,
                                              schedule__start_appointment__minute=minute_appoint))

        else:
            return (Specialist.objects.filter(name=specialist_name))

    # To get a list of all workers
    else:
        return Specialist.objects.all()
