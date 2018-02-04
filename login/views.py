from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django import forms
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from website.sms import send_sms
from .models import Data
from .filters import UserFilter
from django.views.generic.base import TemplateView
import pandas as pd

#class good():
    #df = pd.read_excel('Contaminated habitations as per lab testing (All) .xls')
    #print(df.head())

# def index(request):
   # all_users = User.objects.all()
  # return render(request, 'login/index.html', {'all_users': all_users})

class HomePage(TemplateView):
    template_name = 'login/home.html'

class hiw(TemplateView):
    template_name = 'login/hiw.html'

class cform(TemplateView):
    template_name = 'login/cform.html'


def profile(request):
    all_datas = Data.objects.all()
    template_name = 'login/profile.html'
    return render(request, template_name, {'all_datas': all_datas})



def send(request):
    all_datas = Data.objects.all()
    user = User.is_authenticated
    message = render_to_string('login/wssomail.html', {
        'user': user,
        'all_datas': all_datas

    })
    mail_subject = 'Contamination'
    to_email = User.email
    email = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=['kumarkalyan.1998@gmail.com'])
    email1 = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=['prayanshratan2984@gmail.com'])
    email2 = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=['yashkmkrishan@gmail.com'])


    email.send()
    email1.send()
    email2.send()
    return HttpResponse('hey dude check your mail')


class RegisterFormView(View):
    form_class = RegistrationForm
    template_name = 'login/register.html'

    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            username = form.cleaned_data['username']


            if password==confirm_password:
                user.is_active = False
                user.set_password(password)
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('login/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                mail_subject = 'Activate your account.'
                to_email = form.cleaned_data.get('email')

                email = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, to=[to_email])
                email.send()
                user = authenticate(username=username, password=password)
                return HttpResponse('Please confirm your email address and then <a href="/login/login"><strong>Login Here!</strong></a>')
            else:
                return HttpResponse('<a><strong>Passwords do not match!</strong></a><br><a href=""><strong>Click Here</strong></a> <a>to try again!</a>')

        return render(request, self.template_name, {'form': form})

class LoginFormView(View):
    form_class = LoginForm
    template_names = 'login/loginn.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_names, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            return HttpResponseRedirect("profile")
        else:
            return HttpResponse('<a href=""><strong>Click Here</strong></a> <a>to try again!</a> ')

"""class MobileVerForm(View):
    form_class = MobileVer
    template_name = 'login/userss_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            send_sms(str(form.cleaned_data['mobile']), "a message is sent")
            return HttpResponse("Your mobile is successfully verified")"""


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('<a>Email confirmed. Click to</a> <a href="/login/login"><strong>Login Here</strong></a>')
    else:
        return HttpResponse('Activation link is invalid! Click to</a><a href="/login/login"><strong>Login!</strong></a>')

def Display(request):
    all_users = User.objects.all()
    template_name = 'login/display.html'
    return render(request, template_name, {'all_users': all_users, 'n': range(100)})

def Lottery(request):
    all_users = User.objects.all()
    template_name = 'login/lottery.html'
    return render(request, template_name, {'all_users': all_users})

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'login/user_list.html', {'filter': user_filter})