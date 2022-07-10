from django.db import models
from django.contrib import messages
from django.contrib import admin
from django.core.exceptions import ValidationError


class Location(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class Schedule(models.Model):
    start_appointment = models.DateTimeField()
    end_appointment = models.DateTimeField()

    def __str__(self):
        return f"Время приёма: {self.start_appointment} - {self.end_appointment}"


class Client(models.Model):
    MAN = 'M'
    WOMAN = 'W'
    GENDERS = [
        (MAN, 'Man'),
        (WOMAN, 'Woman')
    ]
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    specialist = models.CharField(max_length=255)
    start_appointment = models.DateTimeField()
    end_appointment = models.DateTimeField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Запись: {self.start_appointment}({self.end_appointment}) Specialist {self.specialist}')


class Specialist(models.Model):
    specialization = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['schedule', 'location'], name='unique')
        ]

    def __str__(self):
        return (
            f'{self.name}({self.specialization}) - Начало приёма({self.schedule.start_appointment}) -- Конец приёма({self.schedule.end_appointment})')

    # из -за этого метода не срабатвают тесты:
    # def save(self):
    #      if not Specialist.objects.filter(schedule__start_appointment__lte=self.schedule.start_appointment, location=self.location) and\
    #         not Specialist.objects.filter(schedule__end_appointment__gte=self.schedule.end_appointment, location=self.location):
    #         super(Specialist,self).save()
    #      else:
    #         #  необходимо вывести ошибку в админ панель!как сделать не знаю)))
    #         raise ValidationError('Вывести ошибку в админ-панель')
    #