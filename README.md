### teste-backend(python)

# Como usar:

faça clone do repositório

Abrindo o terminar use o comando:

### `pip install -r requirements.txt`

rode as migrations para que a aplicação rode localmente
### `./manage.py makemigrations`
### `./manage.py migrate`

agora utilize o mesmo terminal para rodar o servidor:

### `./manage.py runserver`

# Enviando um arquivo:

tenha um arquivo CNAB.txt com os seus dados

acesse a rota:

### http://localhost:8000/api/archive/

selecione o arquivo e faça o envio

# Visualizando dados na tabela:

### http://localhost:8000/api/data/
