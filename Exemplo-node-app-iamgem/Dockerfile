# informa a imagem base que será utilizada
FROM node

# informa a pasta onde o projeto será executado 
WORKDIR /app

# copia todos os arquivos package.json e os copia para a pasta /app (poderia informar a pasta com apenas um .[ponto])
COPY package*.json /app

# executa esse comando na máquina após a cópia dos arquivos na camada passada, é necessário fazer isso para que quando executar a imagem no Docker o framework express esteja instalado também
RUN npm install

# copia o resto dos arquivos do diretório para o container
COPY . . 

# expõe a porta que será utilizada, deve ser condizente com a porta na aplicação
EXPOSE 3000

# executa esse comando para rodar a aplicação, aceita os parâmetros em lista
CMD ["node", "app.js"]