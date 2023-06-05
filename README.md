Este é um projeto para o desafio técnico da FUNDECC.

## Começando

Primeiramente, este projeto utiliza o [`Django REST framework`](https://www.django-rest-framework.org/#installation), logo, requere-se também as versões mais recentes do [Python](https://www.python.org/downloads) e [Django](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release) (dentre outros pacotes). Para facilitar a execução do código, foi utilizado docker no projeto.

Com isso, será necessário instalar manualmente o [docker](https://www.docker.com/get-started) em sua máquina antes de continuar com os passos abaixo.

Em seguida, clone este repositório, entre na pasta `desafio-fundecc` e abra no seu editor de código:

```bash
git clone https://github.com/johnnycfg/desafio-fundecc.git

# após finalizar, entre na pasta e abra o projeto no editor de código
cd desafio-fundecc
code .
```

Agora será necessário executar o comando de build do docker para que ele suba os containers da aplicação e do banco de dados.

```bash
docker compose up --build
```

E pronto, com isso tanto a aplicação quanto o banco já deverão estar disponíveis externamente aos containers nas portas 8001 e 5433 respectivamente.

Disponibilizei no [link](https://1drv.ms/u/s!ArzKJtKn8RIjmAeDSVzS-heF5L1j?e=dLfTxQ) uma collection do [Postman](https://www.postman.com/) com as rotas criadas e com valores pré-preenchidos para facilitar a validação, sendo necessário apenas importar o arquivo no aplicativo.
