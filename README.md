# Desafio: Recarga Telefônica

O projeto trata-se da implementação de uma API _(Application Programming Interface)_ para uma empresa que disponibiliza a compra de recargas para celulares. Os principais recursos a serem implementados são: a manutenção do CRUD _(Create, Read, Update and Delete)_  quanto as chamadas feitas ao back-end relacionadas às empresas; e a efetivação da recarga ao celular do usuário pelo método POST e requisições GET para busca de dados.

## Perguntas a serem respondidas

- __Quais foram os principais desafios durante o desenvolvimento?__

O maior desafio foi desenvolver a comunicação do banco de dados __SQLAlchemy__ com a __Flask Framework__. Como são ferramentas que não tive contato prévio, ter sido posto em prova para resolver os problemas, foi muito recompensador.

A estruturação dos modelos compostos pelo banco de dados e suas relações se mostraram de difícil acesso . Primeiramente, quando requisitados no servidor, as empresas não mostravam os produtos contidos no banco de dados, mas logo foi resolvido com o **marshall_with** contido no __RESTful__ quando utilizado os _fields.Nested_.

Outra questão que destaco, é quanto às requisições GET para consulta dos PhoneRecharges onde o filtro pode ser tanto o **ID** da compra como o **PHONE_NUMBER** do usuário. Desta forma, utilizo uma série de condições para filtrar o necessário.

- __O que você escolheu como arquitetura/framework/banco e por que?__

A arquitetura escolhida foi a de __Packages__ desenvolvida dentro da __Flask Framework__. Inicialmente estruturei o código em um único arquivo, porém ao analisar que dificultaria a manutenção do mesmo, reorganizei em diversos módulos resultando em um projeto mais legível e organizado. Por ser uma framework simples de se utilizar, com diversas documentações disponíveis, foi escolhido o Flask e a extensão RESTful que facilitou a implementação do API.

O banco de dados utilizado foi o __SQLAlchemy__ que tem uma ótima integração com o __Flask__ e sua extensão RESTful, facilitando a comunicação de relações _(relationship)_  entre os modelos criados.

- __O que falta desenvolver?__ 

Gostaria de ter realizado um sistema de segurança de acesso, pois no momento qualquer pessoa pode fazer um request válido ao servidor. A implementação do __Docker__ é algo que ajudaria imensamente na automatização do deploy.

A implementação está concluída com os testes básicos citados no desafio, acredito que mais testes devem ser implementados para melhores validações do API.

- __Como poderíamos melhorar o que você entregou?__

Pesquisando e aprendendo sobre a __Flask Framework__ notei que não é possível processamentos assíncronos, logo AIOHTTP seria uma ótima solução caso os Endpoints fossem consumidos por grandes requisições. 

- __Python é a melhor escolha para esta atividade? Por que?__

Python é a única linguagem de back-end que conheço, mas sinto que ela é muito poderosa, sua sintaxe é extremamente intuitiva e fácil de usar. E a comunidade por trás é muito acolhedora.

## Como executar o projeto

É recomendado que se utilize o ambiente virtual do Python _(virtualenv)_ para que não ocorram conflitos de dependências entre outros projetos.

```bash
# Instale do ambiente virtual
pip install virtualenv

# Clone o repositório
git clone https://github.com/lucasjaroszewski/Recarga-Telefonica

# Entre na pasta criada
cd Recarga-Telefonica

# Crie e ative o ambiente virtual
virtualenv myenv
source myenv/Scripts/activate

# Instale os requerimentos
pip install -r requirements.txt

# Execute o servidor
python run.py
```

## Documentação

### Métodos GET

```bash
# GET /CompanyProducts/
# GET /CompanyProducts/<string:company_id>
# GET /PhoneRecharges/
# GET /PhoneRecharges/<string:id>
# GET /PhoneRecharges/<string:phone_number>
```

### Testes

```bash
# Criar database
python database.py

# Test 1 - CompanyProducts
test_companyproducts.py

# Test 2 - PhoneRecharges
test_phonerecharges.py
```
