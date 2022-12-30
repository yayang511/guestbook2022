from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MessageList(ListView):
    model = Message
    ordering=['-id']

class MessageDetail(DetailView):
    model = Message
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']
    success_url = reverse_lazy('msg_list')

class MessageDelete(Loginrequiredmixin, DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')