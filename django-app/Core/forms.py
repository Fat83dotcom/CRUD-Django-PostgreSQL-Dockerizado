from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from Core.models import CadastroCliente
from utils.django_forms import add_placeholder, add_class
from utils.django_senhas import validar_senha


class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ('nome', 'nasc', 'email', 'cidade')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['nome'], 'Digite o nome do cliente.')
        add_class(self.fields['nome'], 'form-control')
        add_placeholder(self.fields['nasc'], 'Digite o data de nascimento.')
        add_class(self.fields['nasc'], 'form-control')
        add_placeholder(self.fields['email'], 'Digite o email.')
        add_class(self.fields['email'], 'form-control')
        add_placeholder(self.fields['cidade'], 'Digite a cidade.')
        add_class(self.fields['cidade'], 'form-control')

    widgets = {
        'nasc': forms.DateInput()
    }


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['email'], 'Digite o email.')
        add_class(self.fields['email'], 'form-control')
        add_placeholder(self.fields['senha'], 'Digite a Senha.')
        add_class(self.fields['senha'], 'form-control')

    email = forms.CharField(
        widget=forms.EmailInput()
    )
    senha = forms.CharField(
        widget=forms.PasswordInput()
    )


class UsuarioForm(forms.ModelForm):
    msg = 'A senha deve conter no mínimo\
          12 caracteres, incluindo 4 letras e 4 simbolos.'

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite um nome de usuário.')
        add_class(self.fields['username'], 'form-control')
        add_placeholder(self.fields['email'], 'Digite o email.')
        add_class(self.fields['email'], 'form-control')
        add_placeholder(self.fields['password'], 'Digite a Senha.')
        add_class(self.fields['password'], 'form-control')
        add_placeholder(self.fields['password2'], 'Confirmar Senha.')
        add_class(self.fields['password2'], 'form-control')

    username = forms.CharField(max_length=100)
    email = forms.CharField(
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text=(msg),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if validar_senha(password):
            return password
        raise ValidationError(
            'A senha não contém os requisitos.',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        existe = User.objects.filter(email=email).exists()

        if existe:
            raise ValidationError(
                'Este email não pode ser usado, já existe.'
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError({
                'password': 'As senhas não correspondem.'
            })
