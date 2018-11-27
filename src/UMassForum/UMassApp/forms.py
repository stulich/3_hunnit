from django import forms
from UMassApp.models import DiscussionPost


class CreateDForm(forms.ModelForm):
	title = forms.CharField(max_length=25)
	content = forms.CharField(max_length=400)

	class Meta:
		model = DiscussionPost
		fields = ('title', 'content',)