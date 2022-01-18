from django.shortcuts import render

# Create your views here.
#templates라는 디렉토리를 만들어야함. 이게 root 디렉토리
def index(request):
    return render(
        request,
        'index.html',
    )