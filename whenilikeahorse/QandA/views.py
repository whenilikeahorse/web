
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Userqa
from .forms import UserqaForm


class UserqaList(ListView):
    template_name = 'qa_list.html'
    model = Userqa

def new_qa(request):
    if request.method == "POST":
        form = UserqaForm(request.POST)

        if form.is_valid():
            qa = form.save(commit=False)
            # post.username = request.user
            qa.save()
            return redirect('userqalist', pk = qa.pk) # POST로 form 이 채워져있으면 form을 수정하고 userqalist로 전달해줌
    else:
        form = UserqaForm() # default는 비워진 form 보여주고
    
    return render(request, 'userqa.html', {'form': form } ) # form을 사용할 곳인 templates에 form 전달

class Qa_detail(DetailView):
    model = Userqa
    template_name : 'qa_detail.html'