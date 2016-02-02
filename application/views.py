from django.shortcuts import render, get_object_or_404, redirect
from .models import JobOpenings, Questionnaire, Rsa
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import QuestionnaireForm, RsaForm





# Create your views here.
def post_list(request):
	posts = JobOpenings.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'application/post_list.html',{'posts': posts})
	
	
def post_detail(request, pk):
	post = get_object_or_404(JobOpenings, pk=pk)
	print "Job id ", pk
	return render(request, 'application/post_detail.html', {'post': post, 'pk':pk})

	
def QuestionnaireDisplay(request, pk):
	return render(request, 'application/display.html', {'pk':pk})
	
	
def QuestionnaireProcess(request, pk):
	Yes_list = [] 
	No_list = []
	job = JobOpenings.objects.get(pk = pk)
	print job
	if request.method == 'POST':	
		#For YES response
		print "here"
		answers = Questionnaire.objects.get_or_create(
		job_opening = JobOpenings.objects.get(pk = pk),
		MBA = request.POST.get('MBA'),
		Formal_Finance_Training = request.POST.get('Formal_Finance_Training'),
		Employment_Status = request.POST.get('Employment_Status'),
		Equity = request.POST.get('Equity'),
		Salary_for_equity = request.POST.get('Salary_for_equity'),
		Job_Salary = request.POST.get('Job_Salary'),
		Entrepreneur = request.POST.get('Entrepreneur'),		
		Job_Time = request.POST.get('Job_Time'),
		Told_What_to_do = request.POST.get('Told_What_to_do'),
		Gay_people = request.POST.get('Gay_people'),
		Muslims = request.POST.get('Muslims'),
		Christians = request.POST.get('Christians'),
		)	
		
				
	return HttpResponseRedirect('results')
	return HttpResponse("Do it again")	
	
	
def QuestionnaireResults(request):
	return render(request, 'application/results.html') 
	
	
def new_form(request, pk):
	job_opening = JobOpenings.objects.get(pk = pk)
	print job_opening
	print request.POST
	if request.method == "POST":
		form = QuestionnaireForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.job_opening = job_opening		
			MBA = request.POST.get("MBA") # the selected option
			Formal_Training = request.POST.get("Formal_Training")
			Employment_Status = request.POST.get('Employment_Status')
			Equity = request.POST.get('Equity')
			Salary_for_equity = request.POST.get('Salary_for_equity')
			Job_Salary = request.POST.get('Job_Salary')
			Job_Time = request.POST.get("Job_Time")
			Told_What_to_do = request.POST.get('Told_What_to_do')
			Entrepreneur = request.POST.get('Entrepreneur')		
			Dislikes = request.POST.get('Dislikes')
			Get_along_with = request.POST.get('Get_along_with')
			Gay_people = request.POST.get('Gay_people')
			Muslims = request.POST.get('Muslims')
			Christians = request.POST.get('Christians')
			Description = request.POST.get('Description')
			
			
			
			exp_ans = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'None', 'All', 'No', 'No']
			selection = [MBA,Formal_Training, Employment_Status, Equity, Salary_for_equity, Job_Salary, Job_Time, Told_What_to_do, Entrepreneur, Dislikes, Get_along_with, Muslims, Christians]
			#print selection
			
			if exp_ans == selection and Gay_people != "Definitely":
				post.succesful_applicant = True
				job_opening.save()
				post.save()
				return redirect(reverse('application:results'))
						#return HttpResponse("Application submitted Successfully")
			else:
				post.save()
				return HttpResponse("You did not meet the required criteria for a succesful submission")
				#return redirect('post_detail', pk=post.pk)
	else:
			form = QuestionnaireForm()
			
	return render(request, 'application/new_form.html', {'form': form,'pk':pk, 'job_opening':job_opening})
	
# def specific_list(request, pk):
	# #question = get_object_or_404(SelectiveQuestions, pk=pk)
	# #question = SelectiveQuestions.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
	# question = Choices.objects.all()
	# return render(request, 'application/sales_form.html',{'question': question, 'pk': pk})
	
	

def rsa(request, pk):
	job_opening = JobOpenings.objects.get(pk = pk)
	print job_opening
	if request.method == "POST":
		form = RsaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.job_opening = job_opening
		
			MBA = request.POST.get("MBA") # the selected option
			Formal_Training = request.POST.get("Formal_Training")
			Employment_Status = request.POST.get('Employment_Status')
			Equity = request.POST.get('Equity')
			Salary_for_equity = request.POST.get('Salary_for_equity')
			Job_Salary = request.POST.get('Job_Salary')
			Job_Time = request.POST.get("Job_Time")
			Told_What_to_do = request.POST.get('Told_What_to_do')
			Entrepreneur = request.POST.get('Entrepreneur')		
			Dislikes = request.POST.get('Dislikes')
			Get_along_with = request.POST.get('Get_along_with')
			Gay_people = request.POST.get('Gay_people')
			Muslims = request.POST.get('Muslims')
			Christians = request.POST.get('Christians')
			Description = request.POST.get('Description')
			Client_acquisition = request.POST.get('Client_acquisition')
			Client_retention = request.POST.get('Client_retention')
			
			
			exp_ans = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'None', 'All', 'No', 'No']
			selection = [MBA, Formal_Training, Employment_Status, Equity, Salary_for_equity, Job_Salary, Job_Time, Told_What_to_do, Entrepreneur, Dislikes, Get_along_with, Muslims, Christians]
			#print selection
			
			if exp_ans == selection and Gay_people != "Definitely":
				post.succesful_applicant = True
				post.save()
				job_opening.save()
				return redirect(reverse('application:results'))
						#return HttpResponse("Application submitted Successfully")
			else:
				post.save()
				return HttpResponse("You did not meet the required criteria for a succesful submission")
				#return redirect('post_detail', pk=post.pk)
	else:
			form = RsaForm()
			
	return render(request, 'application/sales_form.html', {'form': form,'pk':pk, 'job_opening':job_opening})
	