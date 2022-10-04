## O que é YAML?

   - É uma linguagem de serialização.

   - Usada geralmente para configuração de arquivos, incluindo o Docker, para a configuração do Docker Compose.

   - É de fácil leitura e suas extenções são .yml ou .yaml


## Espaçamento e indentação

   - Cada fim de linha indica fim de uma instrução

   - Um ou mais espaços são utilizados para indentar , não deve ser utilizado o 'tab' para indentar.

   - O espaço é obrigatório após a declaração da chave.

## Comentários

   - '#' é utilizado para comentar em arquivos YAML.


## Strings no YAML 

   - São aceitos com ou sem aspas. 

   - Acentuação pode causar problemas, então é preferível que não seja utilizado nas strings.


## Valores nulo

   - ~ ou null são utilizados para inserir null para certa chave


## Booleanos

   - True e On - verdadeiro

   - False e Off - falso


## Arrays
   
   - Em YAML possuem duas sintaxes aceitas:

      - [1,2,3,4,5] 

      - items:
         - 1
         - 2
         - 3


## Dicionários

   - listas com chaves e valores, podem ser escritos assim:

      - obj: {a: 1, b: 2, c: 3, d: texto}

      - obj:
       - chave: 1
       - chave2: On