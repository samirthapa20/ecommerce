from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.urls import reverse
from .models import GuestEmail
from .signals import user_logged_in
from .forms import  LoginForm, RegisterForm, GuestForm, UserDetailChangeForm
from ecommerce.mixins import NextUrlMixin
# Create your views here.
class AccountHomeView(LoginRequiredMixin, DetailView):
	template_name = 'accounts/home.html'
	def get_object(self):
		return self.request.user

# def guest_register_view(request):
# 	form = GuestForm(request.POST or None)
# 	context = {
# 		"form": form
# 	}
	
# 	next_ = request.GET.get('next')
# 	next_post = request.POST.get('next')
# 	redirect_path = next_ or next_post or None
# 	if form.is_valid():
# 		email = form.cleaned_data.get("email")
# 		new_guest_email = GuestEmail.objects.create(email=email)
# 		if is_safe_url(redirect_path, request.get_host()):
# 			return redirect(redirect_path)
# 		else:
# 			return redirect('/register/')
# 	return redirect("/register/")

class GuestRegisterView(NextUrlMixin, FormView):
	form_class = GuestForm
	default_next = '/register/'

	def form_invalid(self,form):
		return redirect(self.default_next)

	def form_valid(self,form):
		request = self.request
		email = form.cleaned_data.get('email')
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = new_guest_email.guest_email_id
		return redirect(self.get_next_url())

class LoginView(NextUrlMixin,FormView):
	form_class = LoginForm
	success_url = '/'
	template_name = 'accounts/login.html'
	default_next = '/'

	def get_form_kwargs(self):
		kwargs = super(LoginView, self).get_form_kwargs()
		print(kwargs)
		kwargs['request'] = self.request
		return kwargs

	def form_valid(self, form):
			next_path = self.get_next_url()
			return redirect(next_path)
		


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
		else:
			print("Error")
	return render(request, "accounts/login.html", context)

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'accounts/register.html'
	success_url = '/login/'


class UserDetailUpdateView(UpdateView):
	form_class = UserDetailChangeForm
	template_name = 'accounts/detail-update-view.html'

	def get_object(self):
		return self.request.user

	def get_context_data(self,*args, **kwargs):
		context = super(UserDetailUpdateView,self).get_context_data(*args,**kwargs)
		context['title'] = 'Change Your Account Details'
		return context

	def get_success_url(self):
		return reverse("account:home")

