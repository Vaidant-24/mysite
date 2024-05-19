from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.

class QuestionModelTest(TestCase):

    def test_was_recently_published_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_text = time)
        self.assertIs(future_question.was_recently_published(), False)

    def test_was_recently_published_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_text = time)
        self.assertIs(old_question.was_recently_published(),False)

    def  test_was_recently_published_with_recent_question(self):

        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_text = time)
        self.assertIs(recent_question.was_recently_published(), True)