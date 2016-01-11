from django.shortcuts import render, get_object_or_404
from .models import JobOpenings
from django.utils import timezone


# Create your views here.
def post_list(request):
	posts = JobOpenings.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'application/post_list.html',{'posts': posts})
	
def post_detail(request, pk):
	post = get_object_or_404(JobOpenings, pk=pk)
	return render(request, 'application/post_detail.html', {'post': post})
	