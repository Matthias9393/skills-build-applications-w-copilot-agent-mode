from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=self.team)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength workout')
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_email(self):
        self.assertEqual(self.user.email, 'tony@stark.com')

    def test_team_name(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_activity_type(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_workout_name(self):
        self.assertEqual(self.workout.name, 'Super Strength')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)
