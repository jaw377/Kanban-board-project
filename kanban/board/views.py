from django.shortcuts import render
from .models import ticket
from .forms import ticketform
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def board(request):
    form = ticketform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    tickets = ticket.objects.all()
    return render(request,'board/board.html',{'tickets':tickets, 'form':form})