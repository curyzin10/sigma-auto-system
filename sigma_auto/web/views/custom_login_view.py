from django.contrib.auth.views import LoginView
from ..forms.login_form import CustomLoginForm


class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    authentication_form = CustomLoginForm
