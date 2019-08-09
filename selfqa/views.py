from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import selfqa
from django.contrib import auth
from django.conf import settings

# def main(request):
#     return render(request,'selfqa.html')

class QaView(ListView):
    model = selfqa
    fields = ['question', 'answer']
    success_url = reverse_lazy('selfqa')


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

 

#  def qa_list(reqest,qa_id):
#         qa_id = get_object_or_404(Userqa, pk=qa_id)
#         current_qa = Userza.objects.get(pk = pa_id)

#         access_user = request.user  # 현재 로그인하여 접근한 사람
#         access_user_str = str(access_user)
#         original_user = current_qa.author   # 글 작성자
#         original_user_str = str(original_user)
#         # reader_user = current_qa.reader # Question 받은사람 (페이지 주인)
#         # reader_user_str = str(reader_user)

#         return render(request, 'selfqa_list.html' ,{
#         'userqa' : qa_detail,
#         'access_user' : access_user_str,
#         'original_user' : original_user_str,
#         # 'reader_user' : reader_user_str,
#     })