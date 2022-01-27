''' holds tests for all views in workouts app '''
from django.test import TestCase
from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import Workout, TypeOfWorkout


class TestViews(TestCase):
    ''' tests for the views in workouts app '''

    # members area
    def test_members_area(self):
        ''' checks for correct stats code and template '''

        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')
        response = self.client.get('/workouts/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/members_area.html')

    # add workout
    def test_add_workout(self):
        ''' checks for correct stats code and template '''

        User.objects.create_superuser(username='test', password='12345')
        self.client.login(username='test', password='12345')
        response = self.client.get('/workouts/add_workout/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/add_workout.html')

    # edit workout
    def test_edit_workouts(self):
        ''' checks for correct stats code and template '''

        User.objects.create_superuser(username='test', password='12345')
        test_type = TypeOfWorkout.objects.create(name='test_type')
        Workout.objects.create(title='test',  type_of_workout=test_type,
                               description='description', date=now(),
                               location='location', duration='test')
        self.client.login(username='test', password='12345')
        response = self.client.get('/workouts/edit_workout/1/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/edit_workout.html')

    # delete workout
    def test_delete_workout(self):
        ''' checks for correct stats code and template'''

        User.objects.create_superuser(username='test', password='12345')
        test_type = TypeOfWorkout.objects.create(name='test_type')
        Workout.objects.create(title='test',  type_of_workout=test_type,
                               description='description', date=now(),
                               location='location', duration='test')
        self.client.login(username='test', password='12345')
        response = self.client.get('/workouts/delete_workout/1/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/delete_workout.html')

    # my workouts
    def test_my_workouts(self):
        ''' checks for correct stats code and template '''

        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')
        response = self.client.get('/workouts/my_workouts/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/my_workouts.html')
