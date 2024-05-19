# CRUD-Django-PostgreSQL-Dockerizado
## CRUD básico com Django e Postgres implementando com Doker básico

* Para rodar o CRUD primeiramente você deverá ter o Doker e o Python instalado no seu computador.

* Na pasta do repositório:

## Crie a imagem do Postgres:

* Execute o Docker file para o Postgres:

```docker build -t psql:15 -f psql.dockerfile .```

## Crie uma rede:

```docker network create --driver bridge minha-rede ```

## Crie o container Postgres:

```docker run -itd -p 5432:5432 --network minha-rede --mount type=bind,source="caminho/completo/até/data/postgres/data",target="/var/lib/postgresql/data" psql:15```

* Após cria-lo, copie o nome ou seu código e cole na variavel de ambiente ```ENV POSTGRES_HOST="" no ```django.dockerfile```


## Crie a imagem do Django:

* Execute o Docker file para o Django (Se quiser, altere as variaveis de ambiente do settings.py, lembrando que devem ser as mesmas no ```psql.dockerfile```)

```docker build -t django-app:teste -f django.dockerfile .```

* crie o container Django:

```docker run -it -p 8000:8000 --network minha-rede -v "caminho/completo/até/django-app":/django-app django-app:teste```

* para criar um superusuario no Django, entre no container e execute por lá os comandos:

```docker exec -it container /bin/bash```
```python manage.py createsuperuser```




