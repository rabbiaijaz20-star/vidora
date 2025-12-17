# my_project/apps/users/user_profile/forms.py

from django import forms
from .models import UserProfile

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        labels = {
            'avatar': 'Upload your avatar'
        }
