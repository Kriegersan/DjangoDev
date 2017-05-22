# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.utils import timezone

from .models import Question

import datetime

# Create your tests here.


class QuestionMethodTests(TestCase):

  def test_was_published_recently_with_future_question(self):
    time = timezone.now() + datetime.timedelta(days=30)
    fquest = Question(pub_date=time)
    self.assertIs(fquest.was_published_recently(), False)


def test_was_published_recently_with_old_question(self):
  time = timezone.now() - datetime.timedelta(days=30)
  oquest = Question(pub_date=time)
  self.assertIs(oquest.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
  time = timezone.now() - datetime.timedelta(hours=1)
  rquest = Question(pub_date=time)
  self.assertIs(rquest.was_publsihed_recently(), True)
