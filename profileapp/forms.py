from django import forms
from profileapp.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']