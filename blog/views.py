from django.shortcuts import render

# Create your views here.

from .models import Alert_history, Category, Tag
from django.views.generic import ListView, DetailView


# 이 방식은 CBV
class PostList(ListView):
    model = Alert_history
    ordering = '-pk'

    # CBV에서 추가로 넘기고 싶은 인자가 있을 때 사용
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Alert_history.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Alert_history

    # CBV에서 추가로 넘기고 싶은 인자가 있을 때 사용
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Alert_history.objects.filter(category=None).count()
        return context


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Alert_history.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Alert_history.objects.filter(category=category)

    return render(
        request,
        'blog/alert_history_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Alert_history.objects.filter(category=None).count(),
            'category': category,
        }
    )


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.alert_history_set.all()

    return render(
        request,
        'blog/alert_history_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Alert_history.objects.filter(category=None).count(),
        }
    )

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
