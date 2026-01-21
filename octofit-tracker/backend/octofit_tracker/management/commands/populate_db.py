from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Assume collections are empty; only insert test data

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create workouts
        run = Workout.objects.create(name='Running', description='Run 5km')
        swim = Workout.objects.create(name='Swimming', description='Swim 1km')
        lift = Workout.objects.create(name='Weight Lifting', description='Lift weights for 30 minutes')

        # Create activities
        Activity.objects.create(user=tony, workout=run, date=timezone.now().date(), duration_minutes=30, points=50)
        Activity.objects.create(user=steve, workout=swim, date=timezone.now().date(), duration_minutes=40, points=60)
        Activity.objects.create(user=bruce, workout=lift, date=timezone.now().date(), duration_minutes=45, points=70)
        Activity.objects.create(user=clark, workout=run, date=timezone.now().date(), duration_minutes=25, points=40)

        # Calculate leaderboard
        marvel_points = sum(a.points for a in Activity.objects.filter(user__team=marvel))
        dc_points = sum(a.points for a in Activity.objects.filter(user__team=dc))
        Leaderboard.objects.create(team=marvel, total_points=marvel_points)
        Leaderboard.objects.create(team=dc, total_points=dc_points)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
