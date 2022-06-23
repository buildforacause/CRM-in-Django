from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, User, Agent


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {"username": UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
