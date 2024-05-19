# CRUD-Django-PostgreSQL-Dockerizado
## CRUD básico com Django e Postgres implementando com Doker básico

* Para rodar o CRUD primeiramente você deverá ter o Doker e o Python instalado no seu computador.

* Você pode instalar um ambiente virtual, na pasta raiz do projeto, mas é opcional.

* Na pasta do repositório:

## Crie a imagem do Postgres:

```docker build -t psql:15 -f psql.dockerfile .```

## Crie uma rede:

```docker network create --driver bridge minha-rede ```

## Crie o container Postgres:

```docker run -itd --name psql -p 5432:5432 --network minha-rede -v "/caminho até a raiz/CRUD-Django-PostgreSQL-Dockerizado/data/postgres/data":"/var/lib/postgresql/data" psql:15```

## Crie a imagem Django:

* (Se quiser, altere as variaveis de ambiente do settings.py)

```docker build -t django-app:v1.0 -f django.dockerfile .```

## Crie o container Django:

```docker run -it --name django -p 8000:8000 --network minha-rede -v "/caminho até a raiz/CRUD-Django-PostgreSQL-Dockerizado/django-app":/django-app -v "/caminho até a raiz/CRUD-Django-PostgreSQL-Dockerizado/web/static/":/web/static/ django-app:v1.0```

* para criar um superusuario no Django, entre no container:

```docker exec -it django /bin/bash```

e execute por lá o comando:

```python manage.py createsuperuser```

## Usando:

* Ao iniciar o container do django você deverá ver esta tela no terminal, ou algo parecido:

<img src="/screens/n7.png" alt="Terminal">

* Se ver essa tela, quer dizer que o servidor de desenvolvimento foi inciado com sucesso.

* Agora, abra seu navegador e digite o endereço ```127.0.0.1:8000```

### Voce deverá ver está tela, preencha com seus dados:

<img src="/screens/n0.png" alt="Tela inicial">

### Preencha com seus dados:

<img src="/screens/n1.png" alt="Tela preenchida">

### Visualize o cadastro:
<img src="/screens/n2.png" alt="Tela clientes">

### Modifique ou apague uma entrada:

<img src="/screens/n3.png" alt="Tela preenchida">

### Visualize a modificação:

<img src="/screens/n4.png" alt="Tela preenchida">

### Exclua uma entrada:

<img src="/screens/n5.png" alt="Tela preenchida">

### Visualize a exclusão.

<img src="/screens/n6.png" alt="Tela preenchida">

### Melhore e expanda !!

## Grande abraço!








