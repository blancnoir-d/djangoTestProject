from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index),
    path('', views.PostList.as_view()), #CBV로 페이지 만들기
    #path('<int:pk>/', views.single_post_page), # 이런 젠장할  url에 http://127.0.0.1:8000/1/ 이렇게 해야 나오네
    path('<int:pk>/', views.PostDetail.as_view()), #CBV로 페이지 만들기

]
# urlpatterns = [
#     path('', views.index, name='index'),
# ]


