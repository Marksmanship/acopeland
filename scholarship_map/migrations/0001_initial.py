# Generated by Django 2.0.4 on 2018-06-14 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts_app', '0005_auto_20180510_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, max_length=100)),
                ('school_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSports',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('ss_school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ss_school_id', to='scholarship_map.Schools')),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('sports_id', models.AutoField(primary_key=True, serialize=False)),
                ('sports_name', models.IntegerField(choices=[(1, 'Baseball'), (2, 'Basketball'), (3, 'Bowling'), (4, 'Cheerleading'), (5, 'Cross Country'), (6, 'Dance Team'), (7, 'Football'), (8, 'Golf'), (9, 'Gymnastics'), (10, 'Hockey'), (11, 'Soccer'), (12, 'Softball'), (13, 'Swimming'), (14, 'Tennis'), (15, 'Track & Field'), (16, 'Volleyball'), (17, 'Wrestling')], default=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SportStats',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(max_length=40)),
                ('matches_won', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserSchools',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='us_student_id', to=settings.AUTH_USER_MODEL)),
                ('student_school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='us_student_school_id', to='scholarship_map.Schools')),
            ],
        ),
        migrations.CreateModel(
            name='UserSports',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('sports_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersports_sports_id', to='scholarship_map.Sports')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersports_student_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='schoolsports',
            name='ss_sports_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ss_sports_id', to='scholarship_map.Sports'),
        ),
        migrations.AlterUniqueTogether(
            name='usersports',
            unique_together={('student_id', 'sports_id')},
        ),
        migrations.AlterUniqueTogether(
            name='userschools',
            unique_together={('student_id', 'student_school_id')},
        ),
        migrations.AlterUniqueTogether(
            name='schoolsports',
            unique_together={('ss_school_id', 'ss_sports_id')},
        ),
    ]
