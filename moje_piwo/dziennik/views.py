from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from .models import wpis

class wpisCreateView(LoginRequiredMixin, CreateView):
    model = wpis
    fields = ['nazwa_piwa','surowce_1','drożdże','fermentacja',
              'objetosc','temperatura_D_D','startowa_wartosc_BLG',
              'koncowa_wartosc_BLG']
    template_name = 'createView.html'

def index(request):
    return render(request, 'index.html')