# from django.contrib.auth.models import User



from django import forms 


class ManageCSVForm(forms.Form):

    geeks_field = forms.FileField(widget=forms.FileInput(attrs={
                                'class': 'form-control',
                                'id': 'formFile'
                                
                            }))
class UploadFileForm(forms.Form):

    file = forms.FileField(widget=forms.FileInput(attrs={
                                'class': 'form-control',
                                'id': 'formFile'
                                
                            }))


    # def __init__(self, *args, **kwargs):
    #     super(ManageCSVForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Fieldset(
    #             u'',
    #             'csv_file'
    #         )
    #     )
    #     self.helper.layout.append(Submit('guardar', 'Guardar'))

# class RegisterForm(forms.Form):
#     username = forms.CharField(required = True, min_length=4, max_length=50, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'placeholder': 'Username'
#         }))
#     email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'placeholder': 'example@exmaple.org'
#         }))
#     password = forms.CharField(required = True, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         }))

#     password2 = forms.CharField(
#         label= 'Confirmar Password',
#         required = True, 
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'id': 'password',
#         }))

#     def clean_username(self):
#         username = self.cleaned_data.get('username')

#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError('El usuario ya se encuentra en uso')
        
#         return username
    
#     def clean_email(self):
#         email = self.cleaned_data.get('email')

#         if User.objects.filter(username=email).exists():
#             raise forms.ValidationError('El email ya se encuentra en uso')
        
#         return email

#     # Validar que las contraseñas coincidan
#     def clean(self):
#         cleaned_data = super().clean()

#         if cleaned_data.get('password2') != cleaned_data.get('password'):
#             self.add_error('password2', 'El password no coincide')
    
#     def save(self):
#         return User.objects.create_user(
#             self.cleaned_data.get('username'),
#             self.cleaned_data.get('email'),
#             self.cleaned_data.get('password'),
#         )


