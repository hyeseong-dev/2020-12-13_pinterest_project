from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # 템플릿 지정만 파라미터로 넘겨주면 끝
    path('logout/', LogoutView.as_view(), name='logout'),
    # 별도로 로그아웃 템플릿을 만드는 것이 아닌 기존 템플릿을 이용할 것 이기에 template_name 지정 불필요
    path('create/', AccountCreateView.as_view(), name='create'), # url을 통해 해당 뷰가 호출되요.
    path('detail/<int:pk>/', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', AccountUpdateView.as_view(), name='update'),

]