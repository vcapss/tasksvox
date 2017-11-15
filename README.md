# Projeto Tasks

## Ambiente/Instalação

1.  Crie um virtualenv com python3:
    ```sh
    # exemplo usando virtualenvwrapper
    mkvirtualenv tasks -p python3
    ```

2. Instale as dependências do Python:
    ```sh
    pip install -r requirements.txt
    ```

3. Ative a virtualenv:
     ```sh
    source tasks/bin/activate ou workon tasks
    ```

4. Rode o projeto:
    ```sh
    python manage.py runserver
    ```

5. Crie um superusuário:
     ```sh
    python manage.py createsuperuser
    ```

6. Dashboard do projeto disponivel em:
    `127.0.0.1:/admin/`
    
7. Rodar os testes unitários:
    ```sh
    python manage.py test
    ```
    
----------------------------------------------------------

# Resources:

## Usuário Resources

Pegar o token de acesso a API:
```
    http://127.0.0.1:8000/usuario/login/ | Request: POST 

    Payload esperado
    {
        "username": <seu_usuario>
        "password": <sua_senha>
    }
    
    Resposta:
    {
        "key": "<seu_token>"
    }
```

Para se deslogar, ou pegar outro token:
```
    http://127.0.0.1:8000/usuario/logout/ | Request: GET 
```

## Tasks Resources

### Observação: Todas as requests precisam do seguinte Header na requisição, em caso contrário você não será autorizado a obter os resources da API

```sh
Authorization: Token <seu_token>
```

### GET

Listar todas as tasks: http://127.0.0.1:8000/tasks/
```json
# Lista das tarefas que NÃO estão deletadas
[
    {
        "id": 1,
        "name": "Tasks",
        "description": "addsdsa",
        "priority": 4,
        "owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1",
        "files": [
            {
                "id": 1,
                "url": "url",
                "created": "2017-11-13T23:44:31.078968-02:00"
            }
        ],
        "created": "2017-11-13T23:44:31.070594-02:00",
        "done": true,
        "user_task_owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1"
    },
    {
        "id": 2,
        "name": "Tasks",
        "description": "addsdsa",
        "priority": 4,
        "owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1",
        "files": [
            {
                "id": 2,
                "url": "url",
                "created": "2017-11-13T23:44:31.078968-02:00"
            }
        ],
        "created": "2017-11-13T23:44:31.070594-02:00",
        "done": false,
        "user_task_owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1"
    }
]
```

GET task pelo id: http://127.0.0.1:8000/tasks/{id}/
```json

{
    "id": 1,
    "name": "Tasks",
    "description": "addsdsa",
    "priority": 2,
    "owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1",
    "files": [
        {
            "id": 1,
            "url": "url",
            "created": "2017-11-13T23:44:31.078968-02:00"
        }
    ],
    "created": "2017-11-13T23:44:31.070594-02:00",
    "done": true,
    "user_task_owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1"
}
```

POST - http://127.0.0.1:8000/tasks/
```json
 {
        "name": "Tasks",
        "description": "addsdsa",
        "priority": 3,
        "owner": "e6b24c28-3364-45e4-b0c0-90d4d78c07c1",
        "files": [
            {
                "url": "tre" // para criar um novo anexo no payload de tasks
            },
            {
                "id": 1 // para associar a task um arquivo já criado
            }
        ]
}
```

PUT - http://127.0.0.1:8000/tasks/{id}
DELETE - http://127.0.0.1:8000/tasks/{id}

Para atribuir a tarefa ao usuário que fez (O usuário que finalizou é automaticamente atribuido, pelo seu token de acesso):

http://127.0.0.1:8000/tasks/52/finish/

```json
{"done": "true" // "false"}
```

   


