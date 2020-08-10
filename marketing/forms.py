from django import forms
from .models import MarketingPreferece

class MarketingPreferenceForm(forms.ModelForm):
	subscribed = forms.BooleanField(label="Receive Marketing Email", required=False)
	class Meta:
		model = MarketingPreferece
		fields = [
			'subscribed'
		]