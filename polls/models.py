import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_text = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text
    
    def was_recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_text <= timezone.now()

class Choice(models.Model):
    question_text = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text