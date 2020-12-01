from django import forms

class AddProjectForm(forms.Form):
    name = forms.CharField(label='项目名称', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    describe = forms.CharField(label='描述', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    status = forms.BooleanField(label='状态', widget=forms.CheckboxSelectMultiple(attrs={
        'class': "custom-control-label custom-control-color"
    }))