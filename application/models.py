from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class JobOpenings(models.Model):
	title = models.CharField(max_length=300)
	pretext = models.TextField(max_length=300)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title	

		
STATUS = (
	('Yes', 'Yes'),
	('No', 'No'),
)

DISLIKES = (
	('Igbos', 'Igbos'),
	('Yorubas', 'Yorubas'),
	('Northerners', 'Northerners'),
	('Southerners', 'Southerners'),
	('None', 'None'),
)

GENDER = (
	('Men', 'Men'),
	('Women', 'Women'),
	('All', 'All'),
)


FINANCE = (
	('Investment Banking - 5 years and above', 'Investment Banking - 5 years and above'),
	('Mergers and Acquisitions and Stock Trading - 5 years and above', 'Mergers and Acquisitions and Stock Trading - 5 years and above'),
	('Previous CFO Position - 3 years and above', 'Previous CFO Position - 3 years and above'),
	('Previous CEO Position - 3 years and above', 'Previous CEO Position - 3 years and above'),
	('Senior level Auditor - 3 years and above', 'Senior level Auditor - 3 years and above'),
)

SALES = (
	('Software Sales - 5 years and above', 'Software Sales - 5 years and above'),
	('Software Business Development - 5 years and above', 'Software Business Development - 5 years and above'),
)



class Questionnaire(models.Model):
	job_opening = models.ForeignKey(JobOpenings, null=True,blank=True, default="")
	MBA = models.CharField(max_length=10, choices=STATUS, verbose_name="Do you have an MBA?")
	Formal_Training = models.CharField(max_length=10, choices=STATUS, verbose_name="Do you have formal training in finance")
	Description = models.TextField(default="", max_length=250, verbose_name="Describe the trainings you have acquired")
	Employment_Status = models.CharField(max_length=10, choices=STATUS, verbose_name="Are you currently employed")
	Employment_Fields = models.CharField(max_length=20, choices =FINANCE, verbose_name="Select any of the following fields that represent your experience")
	Equity = models.CharField(max_length=10, choices=STATUS, verbose_name="Do you care about having equity?")
	Salary_for_equity = models.CharField(max_length=10, choices=STATUS, verbose_name="Are you willing to trade a portion of salary for equity? ")
	Job_Salary = models.CharField(max_length=10, choices=STATUS, verbose_name="Can you live on N250,000 or less for the next 9 months?")
	Job_Time = models.CharField(max_length=10, choices=STATUS, verbose_name="I just want a 9-5 job to pay the bills")
	Told_What_to_do = models.CharField(max_length=10, choices=STATUS, verbose_name="I like to be told what to do")
	Entrepreneur = models.CharField(max_length=10, choices=STATUS, verbose_name="I am an entrepreneur at heart")
	Dislikes = models.CharField(max_length=100, choices=DISLIKES, verbose_name="Who do you dislike the most?")
	Get_along_with = models.CharField(max_length=10, choices=GENDER,verbose_name="Who do you get along with")
	Gay_people = models.CharField(max_length=10, choices=STATUS, verbose_name="Gay people are disgusting and should be put in jail")
	Muslims = models.CharField(max_length=10, choices=STATUS, verbose_name="I cannot stand muslims")
	Christians = models.CharField(max_length=10, choices=STATUS, verbose_name="Christians and others are infidels")
	
	def __str__(self):
		return self.job_opening.title
		
# class SelectiveQuestions(models.Model):
	# job_opening = models.ForeignKey(JobOpenings, null=True, blank=True)
	# question_text = models.CharField(max_length=50)
	# pub_date = models.DateTimeField(blank=True, null=True)
	# created_on = models.DateTimeField(default=timezone.now)
	
	# def publish(self):
		# self.published_date = timezone.now()
		# self.save()
	
	# def __str__(self):
		# return self.question_text
		

# class Choices(models.Model):
	# question = models.ForeignKey(SelectiveQuestions, null=True, blank=True)
	# choice_text = models.CharField(max_length=20)
	
	# def __str__(self):
		# return self.question.question_text
	
class Rsa(models.Model):
	job_opening = models.ForeignKey(JobOpenings, null=True,blank=True, default="")
	MBA = models.CharField(max_length=10, choices=STATUS, verbose_name="Do you have an MBA?")
	Formal_Training = models.CharField(max_length=10, choices=STATUS, verbose_name="Do you have formal training in Business development")
	Description = models.TextField(default="", max_length=250, verbose_name="Describe the trainings you have acquired")
	Employment_Status = models.CharField(max_length=10, choices=STATUS, verbose_name="Are you currently employed")
	Employment_Fields = models.CharField(max_length=20, choices =SALES, verbose_name="Select any of the following fields that represent your experience")
	Client_acquisition = models.TextField(verbose_name="Tell us how you intend to approach client acquisition")
	Client_retention = models.TextField(verbose_name="Tell us how you intend to approach client retention")
	Equity = models.CharField(max_length=10, choices=STATUS, verbose_name="Do you care about having equity?")
	Salary_for_equity = models.CharField(max_length=10, choices=STATUS, verbose_name="Are you willing to trade a portion of salary for equity? ")
	Job_Salary = models.CharField(max_length=10, choices=STATUS, verbose_name="Can you live on N250,000 or less for the next 3-6 months?")
	Job_Time = models.CharField(max_length=10, choices=STATUS, verbose_name="I just want a 9-5 job to pay the bills")
	Told_What_to_do = models.CharField(max_length=10, choices=STATUS, verbose_name="I like to be told what to do")
	Entrepreneur = models.CharField(max_length=10, choices=STATUS, verbose_name="I am an entrepreneur at heart")
	Dislikes = models.CharField(max_length=100, choices=DISLIKES, verbose_name="Who do you dislike the most?")
	Get_along_with = models.CharField(max_length=10, choices=GENDER,verbose_name="Who do you get along with")
	Gay_people = models.CharField(max_length=10, choices=STATUS, verbose_name="Gay people are disgusting and should be put in jail")
	Muslims = models.CharField(max_length=10, choices=STATUS, verbose_name="I cannot stand muslims")
	Christians = models.CharField(max_length=10, choices=STATUS, verbose_name="Christians and others are infidels")
	
	def __str__(self):
		return self.job_opening.title







