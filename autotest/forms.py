from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
                                            attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    # 账号密码的校验
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        print(user, '校验的user')
        if user is None:
            raise forms.ValidationError('用户名或密码错误')
        else:
            self.cleaned_data['user'] = user
            print('self.cleaned_data', self.cleaned_data['user'])
        return self.changed_data


