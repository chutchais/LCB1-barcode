from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import message
class MessageDetailView(DetailView):
	model = message