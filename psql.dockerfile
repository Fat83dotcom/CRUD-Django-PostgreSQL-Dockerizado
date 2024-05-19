FROM postgres:15.7-bullseye

EXPOSE 5432

# Crie um ponto de montagem para o volume dos dados
VOLUME ["/var/lib/postgresql/data"]

# Variaveis de ambiente para que o Django se conecte no Postgres, se alterar lá, altere aqui
ENV DB_ENGINE="django.db.backends.postgresql"
ENV POSTGRES_DB="data_base_site"
ENV POSTGRES_USER="fernando"
ENV POSTGRES_PASSWORD="ee1avxjnrrv^$0!#b2@"
ENV POSTGRES_HOST="9ed2974c210e"
ENV POSTGRES_PORT="5432"