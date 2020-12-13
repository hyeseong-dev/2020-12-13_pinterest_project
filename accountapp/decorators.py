from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk']) # db에서 가져온 user
        if not user == request.user: # 우항은 클라이언트가 입력한 user값
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated