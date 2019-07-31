from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from QandA.models import Userqa 
from django.contrib.auth.hashers import check_password
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm


# # 계정 관리   (우선 주석 처리해놓겠습니다 -수지-)

# def signup(request):
#     if request.method == 'POST':
#         if len(request.POST['username']) < int(8) or len(request.POST['username']) > int(15):
#             return render(request, 'signup.html', {'error': '아이디는 8글자 이상/ 15글자 미만으로 하세요'})
        
#         elif request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'signup.html', {'error': '해당 아이디가 이미 존재합니다'})
#             except:
#                 user = User.objects.create_user(
#                     request.POST['username'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return redirect('index')
        
#         else:
#             return render(request, 'signup.html', {'error': '비밀번호를 동일하게 입력하세요'})
    
#     else:
#         return render(request, 'signup.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
        
#         if user is not None:
#             auth.login(request, user)
#             return redirect('user_page')
#         else:
#             return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 올바르지 않습니다'})
#     else:
#         return render(request, 'login.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('index')
#     return render(request, 'index.html')

# 유저 페이지 관리

def user_page(request):
    logined = request.user   # login한 User
    logined_user = logined.username
    user_qa = Userqa.objects.filter( reader = logined_user )[:3]
    user_qa_view = Userqa.objects.filter( reader = logined_user )
    n = user_qa_view.count()
    return render(request, 'user_page.html', {
        'userqas' : user_qa,
        'n' : n,
    })

#############################################
#######수지test#################

# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#             # age= request.POST["age"]
#             # occupation= request.POST["occupation"]
#             # profile = Profile(user=user,age=age,occupation=occupation)
#             # profile.save()
#             auth.login(request,user)
#             return redirect('home')
#     return render(request, 'account/signup.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('main')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password )
        if user is not None:
            auth.login(request, user)
            return redirect('user_page')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST': 
        auth.logout(request)
        return redirect('index')
    return render(request, 'index.html')

def change_pw(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("main")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "change_pw.html",context)

@login_required
@transaction.atomic #block의 코드가 성공적으로 수행되면 변화를 DB에 커밋하고 예외가 있으면 롤백
def profile(request):
    context= {}
    if request.method == 'POST':
        print(request.user)
        # user_form = UserForm(request.POST or None, instance=request.user)
        profile_form = ProfileForm(request.POST or None, instance=request.user.profile)
        # if user_form.is_valid() and profile_form.is_valid():
        if profile_form.is_valid():
            # user_form.save()
            save_data = profile_form.save()
            save_data.user = request.user
            print(save_data)
            save_data.save()
            print("valid")
            return redirect('user_page')
        else:
            print("error")
            print(user_form.errors, profile_form.errors)
            # messages.error(request, _('Please correct the error below.'))
        # user_form.save()
        # profile_form.save()
        # print("valid")
        # return redirect('home')
    else:
        print("not post")
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# @login_required
# @transaction.atomic
# def profile(request):
#     if request.method == 'POST':
#         print(request.user)
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('home')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#         # 이름, 이메일, 전화번호가 등록되어 있으면 홈으로, 아니면 회원정보 등록화면으로 이동
#         if request.user.username and request.user.email and request.user.profile.age:
#             return redirect('home')
#         else:
#             return render(request, 'account/profile.html', {
#                 'user_form': user_form,
#                 'profile_form': profile_form
#             })
