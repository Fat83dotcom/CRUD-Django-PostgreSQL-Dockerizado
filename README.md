# CRUD-Django-PostgreSQL-Dockerizado
## CRUD básico com Django e Postgres implementando com Doker básico

* Para rodar o CRUD primeiramente você deverá ter o Doker e o Python instalado no seu computador.

*Você pode instalar um ambiente virtual, na pasta raiz do projeto, mas é opcional.

* Na pasta do repositório:

## Crie a imagem do Postgres:

```docker build -t psql:15 -f psql.dockerfile .```

## Crie uma rede:

```docker network create --driver bridge minha-rede ```

## Crie o container Postgres:

```docker run -itd --name psql -p 5432:5432 --network minha-rede -v "/caminho até a raiz/CRUD-Django-PostgreSQL-Dockerizado/data/postgres/data":"/var/lib/postgresql/data" psql:15```

## Crie a imagem Django:

*(Se quiser, altere as variaveis de ambiente do settings.py)

```docker build -t django-app:v1.0 -f django.dockerfile .```

## Crie o container Django:

```docker run -it -p 8000:8000 --network minha-rede -v "/caminho até a raiz/CRUD-Django-PostgreSQL-Dockerizado/django-app":/django-app -v "/caminho até a raiz/CRUD-Django-PostgreSQL-Dockerizado/web/static/":/web/static/ django-app:v1.0```

* para criar um superusuario no Django, entre no container:

```docker exec -it container /bin/bash```

e execute por lá o comando:

```python manage.py createsuperuser```





