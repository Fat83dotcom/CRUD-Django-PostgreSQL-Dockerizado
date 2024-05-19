FROM python:3.11.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

VOLUME /django-app
VOLUME /web/static

WORKDIR /django-app

EXPOSE 8000

# Variaveis de ambiente para settings.py
# Descomentar se for usar a instalação manual
# ENV SECRET_KEY="7q6#hmm=q$jw1r6nbq33i9ee1avxjnr-rv^$0!#-b2@46bkf*3"
# ENV DEBUG="1"
# ENV ALLOWED_HOSTS="127.0.0.1, localhost, 192.168.0.5, 192.168.1.109"
# ENV DB_ENGINE="django.db.backends.postgresql"
# ENV POSTGRES_DB="data_base_site"
# ENV POSTGRES_USER="usuario_padrao"
# ENV POSTGRES_PASSWORD="ee1avxjnrrvb2"
# ENV POSTGRES_HOST="psql"
# ENV POSTGRES_PORT="5432"

COPY django-app /django-app
COPY script /script

RUN apt update && apt -y dist-upgrade && \
    apt install -y libpq5 && \
    apt install -y netcat && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    mkdir -p /web/static && \
    chmod -R 755 /web/static && \
    chmod -R +x /script

ENV PATH="/django-app:/script:/venv/bin:$PATH"

CMD ["commands.sh"]