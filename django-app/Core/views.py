from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from Core.forms import CadastroForm
from Core.models import CadastroCliente


class Index(View):
    def get(self, request, *args, **kwargs):
        forms = CadastroForm()
        context = {
            'form': forms,
        }

        return render(request, 'index/index.html', context)


class CadastroView(View):
    def get(self, request, param, **kwargs):
        forms = CadastroForm()
        msg = param
        context = {
            'form': forms,
            'msg': msg
        }

        return render(request, 'index/index.html', context)


class CadastroCreateView(View):
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
            }

            return render(request, 'index/index.html', context)

    def get(self, request):
        return redirect('index')


class ClienteViews(View):
    def get(self, request, param, **kwargs):
        data = CadastroCliente.objects.all().order_by('-id')
        msg = param
        context = {
            'dados': data,
            'msg': msg,
        }
        return render(request, 'clientes/clientes.html', context)


class AtuaizarClientesView(View):
    def get(self, request, pk):
        dados = CadastroCliente.objects.filter(pk=pk).first()
        # filter retorna uma queryset que não é compativel com
        # instance do forms. sempre usar first
        forms = CadastroForm(request.POST or None, instance=dados)
        context = {
            'forms': forms,
            'pk': pk,
        }
        return render(request, 'atualizar/atualizar.html', context)


class CadastroUpdateView(View):
    def post(self, request, pk):
        dados = dados = CadastroCliente.objects.filter(pk=pk).first()
        forms = CadastroForm(request.POST, instance=dados)

        if forms.is_valid():
            dados = forms.save(commit=False)
            dados.nome = forms.cleaned_data['nome']
            dados.data_nascimento = forms.cleaned_data['data_nascimento']
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
            }
            return render(request, 'atualizar/atualizar.html', context)


class DeletarClientesView(View):
    def get(self, request, pk):
        dados = CadastroCliente.objects.filter(pk=pk).first()
        forms = CadastroForm(request.POST or None, instance=dados)
        context = {
            'forms': forms,
            'pk': pk,
        }
        return render(request, 'deletar/deletar.html', context)


class CadastroDeleteView(View):
    def post(self, request, pk):
        dados = CadastroCliente.objects.filter(pk=pk).first()
        dados.delete()
        confirm = ['Cliente Apagado com sucesso!']
        url = reverse('clientes', args=confirm)
        return redirect(url)
