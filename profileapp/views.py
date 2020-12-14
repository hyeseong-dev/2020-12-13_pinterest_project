from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # ProfileCreationForm의 data가 2번째 파라미터에 들어 있어요.
        temp_profile = form.save(commit=False) # 임시로 저장함.<commit=False> 키워드 인자를 이용해서
        temp_profile.user = self.request.user # self는 view에서 가져온 self임. 또, 웹브라우저에서 입력 받은 값이 우항 좌항이 db에서 가져온값
        temp_profile.save()             # 아래 문제가 해결됨
        return super().form_valid(form) # IntegrityError at /profiles/create/
                                        # NOT NULL constraint failed: profileapp_profile.user_id