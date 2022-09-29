## O que são Imagens

- Imagens são originadas de arquivos que programamos para que o docker crie um estrutura que execute determinadas ações em containers.  São instruções para rodar um container. 

- Elas contêm informações como: imagens base, diretório base, comandos a serem executados, porta da aplicação etc. 

- Ao rodar um container baseado na imagem, as instruções serão executadas em camadas. 


## Como escolher uma boa imagem?

- http://hub.docker.com é o site onde são feitos os downloads das imagens. 
- Porém qualquer pessoa pode fazer o upload de sua imagem nesse site, tornando isso um problema. Portanto, imagens oficiais são aquelas que são confiáveis. 
- Outro parâmetro a se atentar, são os números de downloads e a quantidade de stars. 

## Criando uma imagem

- Para criar uma imagem devemos de um arquivo Dockerfile em uma pasta que ficará o projeto. 
- Para o Dockerfile ser executado, precisamos de algumas instruções: 
- A ordem de execução das instruções a seguir importa, pois cada instrução é armazenada em cache no computador, isso indica que o Dockerfile é dividido em camadas, cada instrução é uma camada e a sua execução é feita do topo à base. Sabendo disso, caso esse documento seja alterado, e consequentemente a imagem tenha que ser 'buildada' de novo, somente os comandos, a partir da linha modificada, serão executados novamente, as camadas a cima já estão no cache da máquina. 
- Então basicamente, o Dockerfile é utilizado para gerar uma imagem modificada de uma imagem base, e suas instruções indicam o que será modificado da original para a modificada. O Dockerfile é a diferença entre a imagem base e a imagem modificada.

```
FROM: imagem base 
WORKDIR: diretório onde o projeto será executado
EXPOSE: expõe a porta de uma imagem, por meio dessa porta, podemos expor o container para podermos acessar.
COPY: copia certos arquivos para dentro da imagem para poder executar o container. Esses arquivos serão copiados na pasta indicada no WORKDIR.
```

