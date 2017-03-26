# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Post(models.Model):
	titulo = models.CharField(max_length=100)
	texto = models.TextField(max_length=400, null=False,blank=False)


	def publish(self):
		self.save()

	def __str__(self):
		return self.titulo

class Postagem(models.Model):
	titulo2 = models.CharField(max_length=100)
	texto2 = models.TextField(max_length=400, null=False, blank=False)

	def publish(self):
		self.save()

	def __str__(self):
		return self.titulo2