# Dependencias

- Python 3

Para instalar as dependencias Python, rodar `pip install -r requirements.txt`

# Rodando o banco de dados

Precisa ter o Docker instalado
https://www.docker.com/products/docker-desktop/

(Lembrando se preciso, fazer o update rodando `wsl --update` )

Depois que atualizar, reinicie o computador.

Em seguida, abra o Docker Desktop novamente e aguarde ele mostrar "Docker is running".

e rodar no terminal:

`docker-compose up -d`

(Talvez necessário trocar a porta do mysql no arquivo `docker-compose.yml`
e também do DATABASE no `settings.py`)

Também, não se esqueça de rodar as migrações com o comando:

`python manage.py migrate`

Para acessar o phpMyAdmin (interface do banco), entrar em localhost:8080


# Rodando o servidor

`python manage.py runserver`
