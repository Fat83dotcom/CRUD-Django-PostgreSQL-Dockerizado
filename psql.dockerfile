FROM postgres:15.7-bullseye

EXPOSE 5432

# Crie um ponto de montagem para o volume dos dados
VOLUME ["/var/lib/postgresql/data"]
