
from django.urls import path
from Core.views import Index, CadastroCreateView, ClienteViews
from Core.views import CadastroView, AtuaizarClientesView, CadastroUpdateView
from Core.views import DeletarClientesView, CadastroDeleteView
from Core.views import LoginView, RegistrarUsuarioView, Login, RegistrarUsuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cadastro/<str:param>/', CadastroView.as_view(), name='cadastro'),
    path('create/', CadastroCreateView.as_view(), name='registrar'),
    path('clientes/<str:param>/', ClienteViews.as_view(), name='clientes'),
    path(
        'atualizar/<int:pk>/',
        AtuaizarClientesView.as_view(),
        name='atualizar'
    ),
    path(
        'update/<int:pk>/',
        CadastroUpdateView.as_view(),
        name='update'
    ),
    path('deletar/<int:pk>/', DeletarClientesView.as_view(), name='deletar'),
    path('delete/<int:pk>/', CadastroDeleteView.as_view(), name='delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/in/', Login.as_view(), name='login_in'),
    path(
        'registrar_usuario/',
        RegistrarUsuarioView.as_view(),
        name='reg_usuario'
    ),
    path(
        'registrar_usuario/create/',
        RegistrarUsuario.as_view(),
        name='criar_usuario'
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
