# from django.contrib.messages.views import SuccessMessageMixin
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.views.generic import UpdateView

# # Create your views here.
# from .forms import MarketingPreferenceForm
# from .models import MarketingPreferece

# class MarketingPrefereceUpdateView(SuccessMessageMixin,UpdateView):
# 	form_class = MarketingPreferenceForm
# 	template_name = 'base/forms.html'
# 	success_url = '/settings/email/'
# 	success_message = "Your email Prefereces have been updated. Thank you."

# 	def dispatch(self, *args, **kwargs):
# 		user = self.request.user
# 		if not user.is_authenticated:
# 			return redirect("/login/?next=/settings/email/")
# 		return super(MarketingPrefereceUpdateView, self).dispatch(*args, **kwargs)


# 	def get_context_data(self, *args, **kwargs):
# 		context = super(MarketingPrefereceUpdateView, self).get_context_data(*args, **kwargs)
# 		context['title'] = 'Update Email Prefereces'
# 		return context

# 	def get_object(self):
# 		user = self.request.user
# 		obj, created = MarketingPreferece.objects.get_or_create(user=user)
# 		return obj