# Generated by Django 4.2 on 2023-05-08 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_text', models.CharField(max_length=200)),
                ('goal_text', models.CharField(max_length=200)),
                ('objective_text', models.CharField(max_length=200)),
                ('month_text', models.CharField(max_length=200)),
                ('quarter_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
                ('approval', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ManagePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_text', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.plan')),
            ],
        ),
    ]