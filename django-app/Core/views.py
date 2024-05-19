from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from Core.forms import CadastroForm
from Core.models import CadastroCliente


class Index(View):
    title = 'Cadastro'

    def get(self, request, *args, **kwargs):
        forms = CadastroForm()
        context = {
            'form': forms,
            'title': self.title,
        }

        return render(request, 'index/index.html', context)


class CadastroView(View):
    title = 'Cadastrar Cliente'

    def get(self, request, param, **kwargs):
        forms = CadastroForm()
        msg = param
        context = {
            'form': forms,
            'msg': msg,
            'title': self.title,
        }

        return render(request, 'index/index.html', context)


class CadastroCreateView(View):
    title = 'Cadastro'

    def post(self, request):
        forms = CadastroForm(request.POST)

        if forms.is_valid():
            forms.save()
            confirm = ['Cliente cadastrado com sucesso!']
            url = reverse('clientes', args=confirm)
            return redirect(url)
        else:
            forms = CadastroForm(request.POST)
            context = {
                'form': forms,
                'title': self.title,
            }

            return render(request, 'index/index.html', context)

    def get(self, request):
        return redirect('index')


class ClienteViews(View):
    title = 'Clientes Cadastrados'

    def get(self, request, param, **kwargs):
        data = CadastroCliente.objects.all().order_by('-id')
        msg = param
        context = {
            'dados': data,
            'msg': msg,
            'title': self.title,
        }
        return render(request, 'clientes/clientes.html', context)


class AtuaizarClientesView(View):
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


class CadastroUpdateView(View):
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
            dados.save()
            confirm = ['Cliente atualizado com sucesso!']
            url = reverse('clientes', args=confirm)
            return redirect(url)
        else:
            form = CadastroForm(request.POST)
            context = {
                'forms': form,
                'pk': pk,
                'title': self.title,
            }
            return render(request, 'atualizar/atualizar.html', context)


class DeletarClientesView(View):
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


class CadastroDeleteView(View):
    def post(self, request, pk):
        dados = get_object_or_404(CadastroCliente, pk=pk)
        dados.delete()
        confirm = ['Cliente Apagado com sucesso!']
        url = reverse('clientes', args=confirm)
        return redirect(url)
