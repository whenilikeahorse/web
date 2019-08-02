from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import selfqa

# def main(request):
#     return render(request,'selfqa.html')

class QaView(ListView):
    model = selfqa

class QaCreate(CreateView):
    model = selfqa
    fields = ['question', 'answer']
    success_url = reverse_lazy('selfqa')

class QaDetail(DetailView):
    model = selfqa

class QaUpdate(UpdateView):
    model = selfqa
    fields = ['question', 'answer']
    success_url = reverse_lazy('selfqa')

class QaDelete(DeleteView):
    model = selfqa
    success_url = reverse_lazy('selfqa')

