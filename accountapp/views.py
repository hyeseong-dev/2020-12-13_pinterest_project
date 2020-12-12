from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/helloworld.html', context={'hello_world_list':hello_world_list})

class AccountCreateView(CreateView): # 계정 생성을 위한 클래스
    model = User # 장고가 이미 만들어둔 User클래스를 사용함
    form_class = UserCreationForm# 장고가 제공한 기본적인 form을 이용(pycharm이면, UserCreationForm에 커서를 올리고 ctrl+b를 눌러 내부 소스코드를 확인해보세요.
    # form_class는 template에서 form이라는 기본 객체를 돌려줘 편리하게 우리가 지금 만드려는 input태그들을 미리 만들어 줘요.
    success_url = reverse_lazy('accountapp:hello_world') # reverse, reverse_lazy의 차이는 FBV와 CBV의 호출시 방식의 차이 때문임.
    template_name = 'accountapp/create.html' # 어떤 템플릿을 보여줄지 정합니다.


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # 설정하지 않으면 기존 user context 이름으로는 모호하기 때문에 다른 사람의 페이지로 가도 자신의 정보만 보임
    template_name = 'accountapp/detail.html' # 내 프로필 html 템플릿 위치


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm

    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'