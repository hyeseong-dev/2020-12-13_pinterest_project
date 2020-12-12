from django.contrib import admin
from django.urls import path, include

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'), # url을 통해 해당 뷰가 호출되요.

]
