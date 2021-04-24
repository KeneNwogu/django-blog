from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.views.generic import CreateView, FormView
from django.urls import reverse


class RegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'register_user.html'

    def get_success_url(self):
        return reverse('home')

# Create your views here.
