## O que é Docker Compose?

   - É uma ferramenta para rodar múltiplos containers

   - Há somente um arquivo para configurar todos os containers

   - É uma forma de rodar múltiplos builds e runs com um só comando

   - Em projetos maiores, o uso do compose é imprescindível


## Criando o primeiro compose

   - Primeiro, crie um arquivo chamado docker-compose.yaml na raiz do projeto.

   - Esse arquivo irá coordenar os containers e imagens.

   - Chaves muito utilizadas no compose: 
      
      - version: versão do compose
      - services: containers/serviços que rodam nessa aplicação
      - volumes: possível adição de volumes


## Variáveis de ambiente

   - Podemos definir variáveis de ambiente para o Docker Compose

   - Para isso, definimos um arquivo base em env_file

   - Podem ser chamadas pela sintaxe: ${VARIAVEL}

   - Essa técnica é útil quando o dado é sensível ou não pode ser compartilhado, como uma senha, pois essas informações vão no arquivo de criação do docker compose.