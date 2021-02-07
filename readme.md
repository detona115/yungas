[![GitHub license](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)
# Prova de conceito

Esta implementação consiste em aplicar uma prova de conceito onde se contrói uma api usando python e django que recebe dados em formato json
e posteriormente expões esses dados com a opção de alguns filtros e
paginação.

## Abordagem

1. Ambiente virtual
   
    Cada desenvolvedor tem suas preferências na eleição de ferramentas para definir um ambiente virtual, para esta implementação optei em usar o pipenv que usa o Pipfile em vez do requirements.txt, no entanto será fornecido um arquivo requirements.txt para facilitar outros desenvolvedores a usar esta implementação.

2. Modelagem dos dados
   
   Se tratando de uma prova de conceito e para simplificar o desenvolvimento, optei em usar o SqLite.
   
    Esta implementação possui 7 modelos (Pessoa, Name, Location, Coordinate, Timezone, Picture, Phone, Cell) de onde são extraídos os dados de cada instância que representa uma pessoa.

    O modelo Pessoa é chave extrangeira em todos os demais modelos excepto nos modelos coordinate e timezone

3. Views
   
    Para facilitar o entendimento da implementação, optei em usar CBV em vez das FBV. (Pessoalmente prefiro as CBV 😊)

4. Serialização
   
    A serialização é feita se baseando no modelo Pessoa, já que todos os demais modelos possuem uma referência dele.


## Pré-requisitos

1. Bibliotecas
   
   Como descrito nos arquivos Pipfile e requirements.txt, as bibliotecas necessárias para rodar esta implementação são:

    * django = "~=3.1.5"

    * djangorestframework = "~=3.11.0"

    * drf-yasg = "==1.17.1"


## Como usar

Após criar seu próprio ambiente virtual e ter instalado as bibliotecas mencionadas acima, execute a migração e os testes unitários para se certificar que tudo está funcionando como esperado

```
$ python manage.py migrate
```
Lembrete 1: Não é necessário fazer o makemigrations, pois já deixei tudo pronto

```
$ python manage.py test
```

Para executar a implementação, execute:
```
$ python manage.py runserver
```

E atravès da barra de endereço no seu navegador, entre o endereço:
```
http://localhost:8000/api
```
Lembrete 2: a página http://localhost:8000 não foi implementada

Lembrete 3: a importação dos dados é feita toda vez que acessar o endpoint http://localhost:8000/api 

### Endpoints

A implementação possui dois endpoints, que são :

*   http://localhost:8000/api
*   http://localhost:8000/api/regiao/'...'

O primeiro endpoint expõe todos os dados usando as configurações predefinidas por padrão.

O segundo endpoint espera um paramêtro que pode variar entre Norte, Sul, Centro-oeste, Sudeste e Nordeste (cuidado com as letras maiúsculas)

Exemplo :

*   http://localhost:8000/api/regiao/Centro-oeste

### Filtros e Parametros

É possível filtrar a apresentação dos dados na barra de endereços com os filtros

*   page
*   page_size

Exemplo :

*   http://localhost:8000/api/?page=3
*   http://localhost:8000/api/?page=2&page_size=10
*   http://localhost:8000/api/regiao/Sudeste?page=2
*   http://localhost:8000/api/regiao/Sudeste?page=2&page_size=10

### Bonus

Esta implementação possui uma documentação auto gerada por swagger que pode ser acessada por: 

*   http://localhost:8000/swagger/


## Autor ✒️

* **Andy Kiaka** - *Job Completo* - [detona115](https://github.com/detona115)

---
⌨️ com ❤️ por [detona115](https://github.com/detona115) 😊
