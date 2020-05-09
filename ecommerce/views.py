from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm


def home_page(request):
	context = {
		"title" : "Hello World!",
		"content" : "Welcome to the homepage"
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title" : "About Page",
		"content" : "Welcome to the about page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title" : "Contact Page",
		"content" : "Welcome to the contact page",
		"form" : contact_form
		# "brand" : "new Brand Name"
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	return render(request, "contact/view.html", context)

