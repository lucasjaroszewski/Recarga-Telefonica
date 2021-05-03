# Desafio: Recarga Telefônica

O projeto trata-se da implementação de uma API _(Application Programming Interface)_ para uma empresa que disponibiliza a compra de recargas para celulares. Os principais recursos a serem implementados são: a manutenção do CRUD _(Create, Read, Update and Delete)_  quanto as chamadas feitas ao back-end relacionadas às empresas; e a efetivação da recarga ao celular do usuário pelo método POST e requisições GET para busca de dados.

## Comentários sobre o desafio


## Perguntas a serem respondidas

- __Quais foram os principais desafios durante o desenvolvimento?__

O maior desafio foi desenvolver a comunicação do banco de dados __SQLAlchemy__ com a extensão __RESTful do Flask__. Que são ferramentas que nunca tive contato, portanto, foi um desafio muito recompensador.

A forma como o banco de dados é criado foi um grande desafio devido os produtos serem relacionados às empresas. Primeiramente, quando requisitados no servidor, as empresas não mostravam os produtos contidos no banco de dados, mas logo foi resolvido com o **@marshall_with** contido no __RESTful__ quando utilizado os _fields.Nested_.

Outro desafio que destaco é quanto às requisições GET para consulta dos PhoneRecharges onde o filtro pode ser tanto o **ID** da compra como o **PHONE_NUMBER** do usuário. Onde utilizo uma série de condições para filtrar o necessário.

- __O que você escolheu como arquitetura/framework/banco e por que?__

A arquitetura escolhida foi a de __Packages__ desenvolvida dentro da __Flask Framework__. No início, a estrutura constituída por um único arquivo ficou confusa, o que dificultou a manutenção do código, portanto, reorganizei o projeto em vários módulos para que ficasse mais legível e organizado. A opção por Flask se deu por se tratar de uma framework simples de se utilizar, com muita documentação disponível e a extensão RESTful que facilitou a implementação do API.

O banco de dados utilizado foi o __SQLAlchemy__ que tem uma ótima integração com o __Flask__ e sua extensão RESTful, facilitando a comunicação de relações _(relationship)_  entre os modelos criados no banco de dados.

- __O que falta desenvolver?__ 

Gostaria de ter realizado um sistema de segurança de acesso, que no momento, qualquer pessoa pode fazer um request válido ao servidor. A implementação do __Docker__ é algo que ajudaria imensamente na automatização do deploy.

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

### Métodos
### Testes
### API Endpoints


