from django import forms
from application.models import Questionnaire, Rsa


class QuestionnaireForm(forms.ModelForm):
	# MBA = forms.
	# Formal_Finance_Training = models.CharField(max_length=10, widget=atttr{label="",{)
	# Employment_Status = models.CharField(max_length=10, choices=STATUS)
	# Employment_Fields = models.CharField(max_length=100, choices=EXP_FIELD)
	# Equity = models.CharField(max_length=10, choices=STATUS)
	# Salary_for_equity = models.CharField(max_length=10, choices=STATUS)
	# Job_Salary = models.CharField(max_length=10, choices=STATUS)
	# Job_Time = models.CharField(max_length=10, choices=STATUS)
	# Told_What_to_do = models.CharField(max_length=10, choices=STATUS)
	# Entrepreneur = models.CharField(max_length=10, choices=STATUS)
	# Dislikes = models.CharField(max_length=100, choices=DISLIKES)
	# Get_along_with = models.CharField(max_length=10, choices=GET_ALONG)
	# Gay_people = models.CharField(max_length=10, choices=STATUS)
	# Muslims = models.CharField(max_length=10, choices=STATUS)
	# Christians = models.CharField(max_length=10, choices=STATUS)
	
	Description = forms.CharField(label="", widget=forms.Textarea(attrs = {'placeholder':"Please describe the trainings"}))
	
	class Meta:
		model = Questionnaire
		exclude = ['job_opening']
		
		

# class JobOpeningsForm(forms.ModelForm):
	
	# class Meta:
		# model = JobOpenings
		# exclude = ['pretext','text']
		
		
class RsaForm(forms.ModelForm):
	Description = forms.CharField(label="", widget=forms.Textarea(attrs = {'placeholder':"Please describe the trainings"}))
	
	class Meta:
		model = Rsa
		exclude= ['job_opening']