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
    fields = ['nazwa_piwa',
              'surowiec_1', 'surowiec_1_ilosc', 'surowiec_1_jednostka',
              'surowiec_2', 'surowiec_2_ilosc', 'surowiec_2_jednostka',
              'surowiec_3', 'surowiec_3_ilosc', 'surowiec_3_jednostka',
              'drożdże','fermentacja',
              'objetosc','temperatura_D_D','startowa_wartość_BLG',
              'końcowa_wartość_BLG']
    template_name = 'dziennik/createView.html'

    def form_valid(self, form):                                 #sprawdza zalogowanie, jeśli wylogowany to przekierowuje na stronę zalogowania
        form.instance.autor = self.request.user
        return super().form_valid(form)


def index(request):
    return render(request, 'dziennik/index.html')