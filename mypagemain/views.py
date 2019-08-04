from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'mypage.html')

def timeline(request):
    return render(request, 'timeline.html')