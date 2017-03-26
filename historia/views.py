from django.shortcuts import render
from django.utils import timezone
#from core.models import Postagem
from core.models import Post

#acima estou importanto as classes do models.py
def historia(request):
	posts = Post.objects.all()
	return render(request, 'historia/historia.html', {'posts': posts})
