from django.shortcuts import render
from django.utils import timezone

def index(request):
	return render(request, 'core/index.html', {})