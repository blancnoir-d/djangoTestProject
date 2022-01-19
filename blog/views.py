from django.shortcuts import render

# Create your views here.

from .models import Alert_history
from django.views.generic import ListView, DetailView

# def index(request):
#     getData = Alert_history.objects.all() #모델명.objects.all() : 모델 모든걸 가져온다??
#     #getData = Alert_history.objects.all().order_by('-pk')
#
#
#     # templates라는 디렉토리를 만들어야함. 이게 root 디렉토리
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'data': getData,
#         }
#     )

# #아 페이지마다 이렇게 만드는건가?? # 이방식은 함수형 FBV
# def single_post_page(request, pk):
#     post = Alert_history.objects.get(pk=pk)
#     # templates라는 디렉토리를 만들어야함. 이게 root 디렉토리
#     return render(
#         request,
#         'blog/alert_history_detail.html',
#         {
#             'post': post,
#         }
#     )

#이 방식은 CBV
class PostList(ListView):
    model = Alert_history
    ordering = '-pk'


class PostDetail(DetailView):
    model = Alert_history


