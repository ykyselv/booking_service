from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Client, Specialist, Schedule, Location, Appointment
from datetime import datetime


class ClientlistTest(APITestCase):

    def setUp(self):
        Location.objects.create(address='Kyiv, Lomonosova street, 8, block 2')
        Location.objects.create(address='Kyiv, Staronavodnytska street, 87, block 1')
        Location.objects.create(address='Kyiv, Kyivska street, 12, block 3')

        # 1st instance of Schedule
        start_schedule_1 = datetime(2022, 7, 7, 9, 0)
        end_schedule_1 = datetime(2022, 7, 7, 18, 0, 0)
        sched1 = Schedule.objects.create(start_appointment=start_schedule_1, end_appointment=end_schedule_1, location_id=1)

        # 2nd instance of Schedule
        start_schedule_2 = datetime(2022, 7, 6, 12, 0, 0)
        end_schedule_2 = datetime(2022, 7, 6, 19, 0, 0)
        sched2 = Schedule.objects.create(start_appointment=start_schedule_2, end_appointment=end_schedule_2, location_id=2)

        # 3rd instance of Schedule
        start_schedule_3 = datetime(2022, 7, 7, 9, 0, 0)
        end_schedule_3 = datetime(2022, 7, 7, 15, 0, 0)
        sched3 = Schedule.objects.create(start_appointment=start_schedule_3, end_appointment=end_schedule_3, location_id=3)

        # 1st instance of Client
        Client.objects.create(id=1, gender='M', name='Ivan Kiselov')
        # 2nd instance of Client
        Client.objects.create(id=2, gender='M', name='Alexander Sizov')
        # 3nd instance of Client
        Client.objects.create(id=3, gender='W', name='Galyna Ivanova')

        start_appointment_1 = datetime(2022, 7, 7, 10, 0, 0)
        end_appointment_1 = datetime(2022, 7, 7, 12, 0, 0)

        start_appointment_2 = datetime(2022, 7, 6, 12, 0, 0)
        end_appointment_2 = datetime(2022, 7, 6, 13, 0, 0)

        start_appointment_3 = datetime(2022, 7, 7, 11, 0, 0)
        end_appointment_3 = datetime(2022, 7, 7, 12, 0, 0)

        Appointment.objects.create(specialist='Prykhodko Mykola Ivanovych', start_appointment=start_appointment_1,
                                   end_appointment=end_appointment_1, client_id=1)

        Appointment.objects.create(specialist='Vakulenko Mykola Stepanovych', start_appointment=start_appointment_2,
                                   end_appointment=end_appointment_2, client_id=2)

        Appointment.objects.create(specialist='Vakulenko Olga Ivanivna', start_appointment=start_appointment_3,
                                   end_appointment=end_appointment_3, client_id=3)



        spec1 = Specialist.objects.create(specialization='massagist', name='Prykhodko Mykola Ivanovych')

        spec1.schedule.add(sched1)


        spec2 = Specialist.objects.create(specialization='endocrynologist', name='Vakulenko Mykola Stepanovych')
        spec2.schedule.add(sched2)

        spec3 = Specialist.objects.create(specialization='dentist', name='Vakulenko Olga Ivanivna')
        spec3.schedule.add(sched3)


    def test_workers_list(self):
        response = self.client.get(reverse('list_of_workers'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual('Prykhodko Mykola Ivanovych', response.json()[0].get('name'))
        self.assertEqual('Vakulenko Mykola Stepanovych', response.json()[1].get('name'))
        self.assertEqual('Vakulenko Olga Ivanivna', response.json()[2].get('name'))
        self.assertEqual('massagist', response.json()[0].get('specialization'))
        self.assertEqual('endocrynologist', response.json()[1].get('specialization'))
        self.assertEqual('dentist', response.json()[2].get('specialization'))

    def test_client_list(self):
        response = self.client.get(reverse('list_of_clients'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual('Ivan Kiselov', response.json()[0].get('client').get('name'))
        self.assertEqual('Alexander Sizov', response.json()[1].get('client').get('name'))
        self.assertEqual('Galyna Ivanova', response.json()[2].get('client').get('name'))
        self.assertEqual('M', response.json()[0].get('client').get('gender'))
        self.assertEqual('M', response.json()[1].get('client').get('gender'))
        self.assertEqual('W', response.json()[2].get('client').get('gender'))
    #

    def test_list_appointment(self):
        response = self.client.get(reverse('makeappoint'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.json())
        self.assertEqual('Prykhodko Mykola Ivanovych', response.json()[0].get('specialist'))
        self.assertEqual('Vakulenko Mykola Stepanovych', response.json()[1].get('specialist'))
        self.assertEqual('Vakulenko Olga Ivanivna', response.json()[2].get('specialist'))
        self.assertEqual('Ivan Kiselov', response.json()[0].get('client').get('name'))
        self.assertEqual('Alexander Sizov', response.json()[1].get('client').get('name'))
        self.assertEqual('Galyna Ivanova', response.json()[2].get('client').get('name'))

    #
    # # IF YOU WANT TO RUN THIS TEST, YOU SHOULD CHANGE:
    # # 1) start_appointment_1  and  end_appointment_1  to actual date(for example current day or another future date)
    # # 2) change time- parameters in Schedule of worker(in SET UP)
    #
    # # def test_create_appointment_valid(self):
    # #     start_appointment_1 = datetime(2022, 7, 7, 17, 0, 0).strftime("%Y-%m-%dT%H:%M")
    # #     end_appointment_1 = datetime(2022, 7, 7, 18, 0, 0).strftime("%Y-%m-%dT%H:%M")
    # #     gender = 'M'
    # #     name = 'Alexander Orlov'
    # #     data = {'start_appointment': start_appointment_1,
    # #             'end_appointment': end_appointment_1,
    # #             'specialist': 'Prykhodko Mykola Ivanovych',
    # #             'client.gender': gender,
    # #             'client.name': name}
    # #     response = self.client.post(reverse('makeappoint'), data=data)
    # #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test for make appointment for a time that has already passed
    def test_create_appointment_invalid_1(self):
        start_appointment_1 = datetime(2022, 7, 7, 17, 0, 0).strftime("%Y-%m-%dT%H:%M")
        end_appointment_1 = datetime(2022, 7, 7, 18, 0, 0).strftime("%Y-%m-%dT%H:%M")
        gender = 'M'
        name = 'Vadym Ivanov'

        data = {'start_appointment': start_appointment_1,
                'end_appointment': end_appointment_1,
                'specialist': 'Prykhodko Mykola Ivanovych',
                "client.gender": gender,
                "client.name": name
                }
        response = self.client.post(reverse('makeappoint'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual('К сожалению, записаться на это время невозможно', response.data[0])

    # test for make appointment to a specialist that does not exist
    def test_create_appointment_invalid_2(self):
        start_appointment_1 = datetime(2022, 7, 7, 17, 0, 0).strftime("%Y-%m-%dT%H:%M")
        end_appointment_1 = datetime(2022, 7, 7, 18, 0, 0).strftime("%Y-%m-%dT%H:%M")
        gender = 'M'
        name = 'Vadym Ivanov'
        data = {'start_appointment': start_appointment_1,
                'end_appointment': end_appointment_1,
                'specialist': 'Cymonenko Ivan Vasyliovych',
                'client.gender': gender,
                'client.name': name}
        response = self.client.post(reverse('makeappoint'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual('Специалист с данным именем отсутствует', response.data[0])

