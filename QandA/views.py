
from django.shortcuts import render, redirect, get_object_or_404
from .models import Userqa
from .forms import UserqaForm, UserqaForm2
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from django.forms import formset_factory

def qa_list(request):
    logined = request.user   # login한 User
    logined_user = logined.username
    user_qa = Userqa.objects.filter( reader = logined_user )
    n = user_qa.count()
    
    return render(request, 'home.html', {
        'userqas' : user_qa,
        'n' : n,
    })

@login_required
def qa_new(request):
    user_name = request.user.username
    UserqaFormset = formset_factory(UserqaForm, extra = 0)
    formset2 = UserqaFormset( initial = [    # form의 초기값을 지정해주기 위한 formset 사용
        {
            'author' : user_name,
            'reader' : "write nickname!"
    }])

    if request.method == "POST":
        formset = UserqaFormset(request.POST)
        
        if formset.is_valid():
            for form in formset:
                qa = form.save(commit=False)    # commit = False좀 알아보자 // 바로 저장 안하려고 하는거라는데
                qa.save()
                return redirect('qa_list')  # POST로 form 이 채워져있으면 form을 수정하고 index 'url'을 이동한다
    else:
        formset = formset2     # default는 작성자가 request.user인 formset을 보여준다
    return render(request, 'qa_form.html', {'formset': formset} ) # form을 사용할 곳인 templates에 form 전달

@login_required
def qa_answer(request, qa_id):
    userqa = Userqa.objects.get(pk = qa_id)

    if request.method == "POST":
        form = UserqaForm2(request.POST, instance = userqa)

        if form.is_valid():
            qa = form.save(commit=False)
            qa.save()
            return render(request, 'qa_detail.html', {'userqa' : userqa})  # 그리고 이제 update된 instance를 보내줘서 답변 보여주면 되는거
    else:
        form = UserqaForm2(instance = userqa)

        return render(request, 'qa_answer_form.html', {
            'userqa' : userqa,
            'form' : form,
        } )

def qa_detail(request, qa_id):
    qa_detail = get_object_or_404(Userqa, pk=qa_id) # 특정 개체 가져오기 없으면 404에러
    current_qa = Userqa.objects.get(pk = qa_id)
    
    access_user = request.user  # 현재 로그인하여 접근한 사람
    access_user_str = str(access_user)
    original_user = current_qa.author   # 글 작성자
    original_user_str = str(original_user)
    reader_user = current_qa.reader # Question 받은사람 (페이지 주인)
    reader_user_str = str(reader_user)

    return render(request, 'qa_detail.html' ,{
        'userqa' : qa_detail,
        'access_user' : access_user_str,
        'original_user' : original_user_str,
        'reader_user' : reader_user_str,
    })

# qa 수정 및 삭제

@login_required
def qa_update(request, qa_id):
    userqa = get_object_or_404(Userqa, pk = qa_id)

    if request.method == "POST":
        form = UserqaForm(request.POST, instance = userqa)  # request된 것을 instance에 update를 이런식으로 해준다고 함 

        if form.is_valid():
            form.save()
            return render(request, 'qa_detail.html', {'userqa' : userqa}) # 그리고 이제 update된 instance를 보내줘서 보여주면 되는거
    else:
        form = UserqaForm(instance = userqa)
    
    return render(request, 'qa_update.html', {'form': form } ) # 값이 채워진 form 을 보여줄 것

@login_required
def qa_delete(request, qa_id):
    qa = get_object_or_404(Userqa, pk = qa_id)
    qa.delete()
    return redirect('qa_list')