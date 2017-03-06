from django.db import models
from datetime import date
from datetime import datetime
from django.utils import timezone

class Course(models.Model):
    course_title = models.CharField(max_length=255, blank=True) 
    course_subtitle = models.CharField(max_length=255, blank=True) 

class Webpage(models.Model):
    webpage_title = models.CharField(max_length=255, blank=True) 
    webpage_description = models.TextField(blank=True)
    webpage_content = models.TextField(blank=True) 

class Video(models.Model):
    video_title = models.CharField(max_length=255, blank=True) 
    video_embed = models.TextField(blank=True)

class AudioSlide(models.Model): 
    audio_slide_title = models.CharField(max_length=255, blank=True) 

class FileDownload(models.Model):
    file_download_title = models.CharField(max_length=255, blank=True)

class Question(models.Model):
    question_title = models.CharField(max_length=255, blank=True) 

class VideoConference(models.Model):
    videoconference_title = models.CharField(max_length=255, blank=True) 
    start_date = models.DateTimeField(default=timezone.now) 
    end_date = models.DateTimeField(default=timezone.now)

CORRECTNESS_OF_ANSWER_CHOICES = (
    ('YES', 'YES'),
    ('NO', 'NO'),
)

class AnswerToQuestion(models.Model):
    answer_text = models.TextField(max_length=255, blank=True) 
    question = models.ForeignKey(Question, null=True, blank=True)
    correct = models.CharField(max_length=10, choices=CORRECTNESS_OF_ANSWER_CHOICES, null=True, blank=True)

class Lesson(models.Model):
    lesson_title = models.CharField(max_length=255, blank=True) 
    webpage = models.ManyToManyField(Webpage, through='Activity')
    video = models.ManyToManyField(Video, through='Activity')
    audioslide = models.ManyToManyField(AudioSlide, through='Activity')
    filedownload = models.ManyToManyField(FileDownload, through='Activity') 
    question = models.ManyToManyField(Question, through='Activity') 
    videoconference = models.ManyToManyField(VideoConference, through='Activity') 

class ActivityType(models.Model):
    activity_type_name = models.CharField(max_length=255, blank=True)

class Activity(models.Model):
    activity_order_number = models.PositiveSmallIntegerField(null=True, blank=True)
    activity_title = models.CharField(max_length=255, blank=True) 
    activity_type = models.ForeignKey(ActivityType, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, null=True, blank=True) 
    webpage = models.ForeignKey(Webpage, null=True, blank=True)
    video = models.ForeignKey(Video, null=True, blank=True)
    audioslide = models.ForeignKey(AudioSlide, null=True, blank=True)
    filedownload = models.ForeignKey(FileDownload, null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True)
    videoconference = models.ForeignKey(VideoConference, null=True, blank=True)

class Client(models.Model): 
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    course = models.ManyToManyField(Course, through='CourseMembership')

class CourseMembershipRole(models.Model):
    role_name = models.CharField(max_length=255)
    role_description = models.CharField(max_length=255, blank=True)

class CourseMembership(models.Model):
    client = models.ForeignKey(Client)
    course = models.ForeignKey(Course)
    role = models.ForeignKey(CourseMembershipRole)
    


