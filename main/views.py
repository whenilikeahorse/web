from django.shortcuts import render
from django.contrib.auth.models import User
from QandA.models import Userqa

def main(request):
    users = User.objects.all().exclude(username = request.user)
    
    return render(request, 'index.html', {
        'users' : users,
    })
    
def other_page(request, user_id):
    page_owner = User.objects.get(pk = user_id) # 다른 page 주인
    owner_name = page_owner.username
    user_qa2 = Userqa.objects.filter( reader = owner_name )
    n2 = user_qa2.count()
    return render(request, 'other_page.html',{
        'owner_name' : owner_name,
        'userqas2' : user_qa2,
        'n2' : n2,
    })

def search_page(request):
    return render(request, 'search_page.html')