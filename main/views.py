from django.shortcuts import render
from django.contrib.auth.models import User
from QandA.models import Userqa

def main(request):
    users = User.objects.all().exclude(username = request.user)[0:6]
    
    return render(request, 'index.html', {
        'users' : users,
    })
    
def other_page(request, user_id):
    page_owner = User.objects.get(pk = user_id) # 다른 page 주인
    owner_name = page_owner.username
    user_qa2_view = Userqa.objects.filter( reader = owner_name )
    user_qa2 = Userqa.objects.filter( reader = owner_name )[0:3]
    n2 = user_qa2_view.count()
    return render(request, 'other_page.html',{
        'owner_name' : owner_name,
        'userqas2' : user_qa2_view,
        'n2' : n2,
    })

def search_page(request):
    return render(request, 'search_page.html')

def search(request):
    if request.method == 'POST':
        search_word = request.POST['search_word']
        users = User.objects.filter(
            Q(username__icontains=search_word) # Q 객체를 사용해서 검색
        ).distinct() # 중복 제거
        return render(request, 'search.html', {'users':users, 'search_word':search_word})
    return render(request, 'index.html')