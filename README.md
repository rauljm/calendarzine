# Calendarzine
--
##### Essa aplicação possui os seguintes objetivos:

Prover uma API para:

- Editar e remover agendamentos.
- Lista e filtrar agendamentos por data e sala.
- Editar e remover salas de reuniões.

#### Diagramação da aplicação
---

![Caption for the picture.](calendarzine.png)


##### Instalando:
---

Crie um virtualenv exclusivo para o projeto. Aconselhamos utilizar o [virtualenvwrapper](https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper) para criar um novo ambiente.
Com o virtualenvwrapper devidamente configurado, rode o seguinte comando no terminal:

```
 mkvirtualenv -p python3 calendarzine
```
Sete a seguinte variável de ambiente necessária para o flask "descobrir" onde ele deve iniciar a sua aplicação 

```
export FLASK_APP="app/create_app.py"
```

Por fim, instale as depêndencias do projeto:
```
pip3 install -r requirements.txt
```

Estamos utilizando o Sqlite como banco relacional. Acreditamos que seja necessário criar um novo arquivo de migração de banco de dados. Antes de verificar essa necessidade, rode o seguinte comando:

```
flask db upgrade
```

Caso a seguinte mensagem apareça, será necessário criar uma nova migração:
````
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
````

Para criar uma nova migração, digite:
```
flask db migrate
```
e então, digite:
```
flask db upgrade
```

Para iniciar a aplicação digite:
```
flask run
````

#### Testando

Para rodar os testes do projeto, digite o seguinte comando:
```
nosetests --with-coverage --cover-package=app
```

A cobertura de testes atual do projeto está em 94%.

```
--------------------------------------------------
app/__init__.py                    0      0   100%
app/controller/__init__.py         0      0   100%
app/controller/room.py            33      1    97%
app/controller/schedule.py        52      6    88%
app/controller/user.py            17      0   100%
app/create_app.py                 28      0   100%
app/exceptions/__init__.py         0      0   100%
app/exceptions/exceptions.py       6      0   100%
app/models/__init__.py             2      0   100%
app/models/room.py                 6      0   100%
app/models/schedule.py            10      0   100%
app/models/user.py                 5      0   100%
app/views/__init__.py              0      0   100%
app/views/room.py                 37      2    95%
app/views/schedule.py             59      8    86%
app/views/user.py                 20      0   100%
--------------------------------------------------
TOTAL                            275     17    94%
----------------------------------------------------------------------
Ran 37 tests in 1.499s

```
#### Utilizando a aplicação

Iremos utilizar o [CURL](https://curl.haxx.se/) para utilizar a aplicação, mas pode-se utilizar o [Postman](https://www.getpostman.com/) também, por exemplo.

Inserindo um novo usuário:
```
curl http://localhost:5000/user/ -d '{"name": "Raul Martins"}' -H "Content-Type: application/json" -X POST
```
Inserindo uma nova sala
```
curl http://localhost:5000/room/ -d '{"name": "Sala1", "description": "Descricao"}' -H "Content-Type: application/json" -X POST
```
Inserindo um novo agendamento
```
curl http://localhost:5000/schedule/ -d '{"user_name": "Raul Martins", "description": "Descricao Agendamento", "room_name": "Sala1", "date": "2018-10-13"}' -H "Content-Type: application/json" -X POST
```
Capturando um usuário pelo ID:
```
curl http://localhost:5000/user/1 -X GET
```
Caputurando uma sala pelo nome:
```
curl http://localhost:5000/room/Sala1 -X GET
```
Capturando todos os agendamentos de uma data:
```
curl http://localhost:5000/schedule/2018-10-13 -X GET
```
Capturando todos os agendamentos de uma determinada sala:
```
curl http://localhost:5000/schedule/room/Sala1 -X GET
```
Atualizando a descrição de uma sala:
```
curl http://localhost:5000/room/1 -X PUT -d '{"description": "Descricao Sala Renovado"}' -H "Content-Type: application/json"
```
Atualizando a descrição de um agendamento:
```
curl http://localhost:5000/schedule/1 -X PUT -d '{"description": "Descricao Agendamento Renovado"}' -H "Content-Type: application/json"
```
