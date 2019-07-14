
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Userqa
from .forms import UserqaForm
from django.urls import reverse_lazy


def qa_list(request):
    userqas = Userqa.objects.all()
    n = Userqa.objects.count()
    return render(request, 'qa_list.html',{
            'userqas' : userqas,
            'number' : n,
    })

def qa_new(request):
    if request.method == "POST":
        form = UserqaForm(request.POST)

        if form.is_valid():
            qa = form.save(commit=False)
            qa.username = request.user
            qa.save()
            return redirect('qa_list') # POST로 form 이 채워져있으면 form을 수정하고 qa_list로 전달해줌
    else:
        form = UserqaForm() # default는 비워진 form 보여주고
        return render(request, 'qa_form.html', {'form': form } ) # form을 사용할 곳인 templates에 form 전달

def qa_detail(request, qa_id):
    qa_detail = get_object_or_404(Userqa, pk=qa_id)
    userqa = Userqa.objects.get(pk=qa_id)

    return render(request, 'qa_detail.html' ,{
        'qa_detail' : qa_detail,
        'userqa' : userqa,
    })

# qa 수정 및 삭제
def qa_update(request, qa_id):

    if request.method == "POST":
        form = UserqaForm(request.POST) # 덮어쓰기 어떻게하냐?

        if form.is_valid():
            qa_update = form.save(commit=False)
            qa_update.username = request.user
            qa_update.save()
            return redirect('qa_list')
    else:
        qa = Userqa.objects.get(pk = qa_id)
        form = UserqaForm(instance = qa)
    
    return render(request, 'qa_form.html', {'form': form } ) # 값이 채워진 form 을 보여줄 것