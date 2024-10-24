from django import forms
from crud.models import CrudModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CrudForm(forms.ModelForm):
    class Meta:
        model = CrudModel
        fields = [
            "title",
            "description",
        ]
        labels = {"title":"Item"}

class CrudUpdate(forms.ModelForm): 
    class Meta:
        model = CrudModel   
        fields = [
            "description"
        ]        


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user        