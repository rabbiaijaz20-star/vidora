from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
from apps.users.user_profile.models import UserProfile
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user_profile:profile')
    def form_valid(self, form):
        response = super().form_valid(form)
        # create a UserProfile for the new user
        UserProfile.objects.create(user=self.object)
        return response  