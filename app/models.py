import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Plan(models.Model):
    plan_text = models.CharField(max_length=200)
    goal_text = models.CharField(max_length=200)
    objective_text = models.CharField(max_length=200)
    month_text = models.CharField(max_length=200)
    quarter_text = models.CharField(max_length=200)
    approval = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date created")
def __str__(self):
    return self.plan_text
def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class ManagePlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    progress_text = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
def __str__(self):
    return self.progress_text