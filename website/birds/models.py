from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200,unique= True)
    group = models.CharField(max_length=200)

    def __repr__(self):
        return self.question_text
 

  #  def __str__(self):
   #     return self.question_text
#    pub_date = models.DateTimeField('date published')
    #choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    ans = models.BooleanField(default=False)

    def __repr__(self):
        return self.choice_text


class Questiongramm(models.Model):
    question_text = models.CharField(max_length=200,unique= True)
    group = models.CharField(max_length=200)

    def __repr__(self):
        return self.question_text
 

  #  def __str__(self):
   #     return self.question_text
#    pub_date = models.DateTimeField('date published')
    #choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

class Choicegramm(models.Model):
    question = models.ForeignKey(Questiongramm, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    ans = models.BooleanField(default=False)

    def __repr__(self):
        return self.choice_text
  #  def __str__(self):
  #      return self.choice_text
 #   votes = models.IntegerField(default=0)
