# Jurid

Projeto Teste 

## Este projeto foi feito com:

* [Django 4.0](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/alexlambertini/Jurid.git
cd jurid
python -m venv .venv

.\.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux

pip install -r requirements.txt

python manage.py migrate

```

## Libs

https://django-storages.readthedocs.io/en/latest/

https://django-extensions.readthedocs.io/en/latest/


## git

Leia o [git.md](git.md)

## Alinhamento dos templates

[djhtml](https://github.com/rtts/djhtml)

```
find web -name "*.html" | xargs djhtml -t 4 -i
```