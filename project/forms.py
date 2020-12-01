from django import forms
from django.forms import widgets

class AddProjectForm(forms.Form):
    name = forms.CharField(label='项目名称', widget=widgets.TextInput(attrs={
        'class': 'form-control'
    }))
    describe = forms.CharField(label='描述', widget=widgets.Textarea(attrs={
        'class': 'form-control'
    }))
    status = forms.BooleanField(label='状态', widget=widgets.CheckboxInput(attrs={
        'id': 'check2',
        'class': 'custom-control-input'
    }))