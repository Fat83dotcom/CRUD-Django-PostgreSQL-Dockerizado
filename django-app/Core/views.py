from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Core.forms import CadastroForm, LoginForm, UsuarioForm
from Core.models import CadastroCliente
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, View):
    title = 'Cadastro'

    def get(self, request, *args, **kwargs):
        forms = CadastroForm()
        context = {
            'form': forms,
            'title': self.title,
        }

        return render(request, 'index/index.html', context)


class CadastroView(LoginRequiredMixin, View):
    title = 'Cadastrar Cliente'

    def get(self, request, **kwargs):
        forms = CadastroForm()
        context = {
            'form': forms,
            'title': self.title,
        }

        return render(request, 'index/index.html', context)


class CadastroCreateView(LoginRequiredMixin, View):
    title = 'Cadastro'

    def post(self, request):
        forms = CadastroForm(request.POST)

        if forms.is_valid():
            dados = forms.save(commit=False)
            dados.criado_por = request.user
            dados.save()
            confirm = 'Cliente cadastrado com sucesso!'
            messages.success(request, confirm)
            return redirect('clientes')

        messages.error(
            request, 'Não foi possível cadsatrar, verifique os dados.'
        )
        forms = CadastroForm(request.POST)
        context = {
            'form': forms,
            'title': self.title,
        }

        return render(request, 'index/index.html', context)

    def get(self, request):
        return redirect('index')


class ClienteViews(LoginRequiredMixin, View):
    title = 'Clientes Cadastrados'

    def get(self, request, **kwargs):
        data = CadastroCliente.objects.all().order_by('-id')
        context = {
            'dados': data,
            'title': self.title,
        }
        return render(request, 'clientes/clientes.html', context)


class AtuaizarClientesView(LoginRequiredMixin, View):
    title = 'Atualizar'

    def get(self, request, pk):
        dados = get_object_or_404(CadastroCliente, pk=pk)
        # filter retorna uma queryset que não é compativel com
        # instance do forms. sempre usar first
        forms = CadastroForm(request.POST or None, instance=dados)
        context = {
            'forms': forms,
            'pk': pk,
            'title': self.title,
        }
        return render(request, 'atualizar/atualizar.html', context)


class CadastroUpdateView(LoginRequiredMixin, View):
    title = 'Atualizar'

    def post(self, request, pk):
        dados = dados = get_object_or_404(CadastroCliente, pk=pk)
        forms = CadastroForm(request.POST, instance=dados)

        if forms.is_valid():
            dados = forms.save(commit=False)
            dados.nome = forms.cleaned_data['nome']
            dados.nasc = forms.cleaned_data['nasc']
            dados.email = forms.cleaned_data['email']
            dados.cidade = forms.cleaned_data['cidade']
            dados.modificado_por = request.user.username
            print(request.user.username)
            dados.save()
            confirm = 'Cliente atualizado com sucesso!'
            messages.success(request, confirm)
            return redirect('clientes')

        messages.error(
            request, 'Não foi possível atualiza, verifique os dados.'
        )
        form = CadastroForm(request.POST)
        context = {
            'forms': form,
            'pk': pk,
            'title': self.title,
        }
        return render(request, 'atualizar/atualizar.html', context)


class DeletarClientesView(LoginRequiredMixin, View):
    title = 'Apagando'

    def get(self, request, pk):
        dados = get_object_or_404(CadastroCliente, pk=pk)
        forms = CadastroForm(request.POST or None, instance=dados)
        context = {
            'forms': forms,
            'pk': pk,
            'title': self.title,
        }
        return render(request, 'deletar/deletar.html', context)


class CadastroDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        dados = get_object_or_404(CadastroCliente, pk=pk)
        dados.delete()
        confirm = 'Cliente Apagado com sucesso!'
        messages.success(request, confirm)
        return redirect('clientes')


class LoginView(View):
    title = 'Login'

    def get(self, request, *args, **kwargs):
        forms = LoginForm()
        context = {
            'forms': forms,
            'title': self.title,
        }

        return render(request, 'login/login.html', context)


class RegistrarUsuarioView(View):
    title = 'Cadastrar Usuário'

    def get(self, request, *args, **kwargs):
        reg_ususario = request.session.get('dados_form', None)
        if reg_ususario:
            forms = UsuarioForm(reg_ususario)
        else:
            forms = UsuarioForm()
        context = {
            'title': self.title,
            'forms': forms,
        }

        return render(request, 'login/registrarUsuario.html', context)


class Login(View):
    def post(self, request, *args, **kwargs):
        forms = LoginForm(request.POST)

        if forms.is_valid():
            auth_usuario = authenticate(
                email=forms.cleaned_data['email'],
                password=forms.cleaned_data['senha']
            )
            if auth_usuario is not None:
                messages.success(request, 'Login efetuado com sucesso.')
                login(request, auth_usuario)
                return redirect('index')

        messages.error(request, 'Verifique seus dados e tente novamente.')
        return redirect('login')


class RegistrarUsuario(View):
    def post(self, request, *args, **kwargs):
        post = request.POST
        request.session['dados_form'] = post
        forms = UsuarioForm(post)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Usuário criado com sucesso.')
            del (request.session['dados_form'])
            return redirect('login')
        messages.error(request, 'Usuário não foi criado, revise o fomrulário.')
        return redirect('reg_usuario')


class LogoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
