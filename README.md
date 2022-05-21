# web-news_api

### Integrantes
 - Gabriel Azevedo de Souza
 - Maria Eduarda Basílio de Oliveira

### Execução
  - Construir a imagem docker do banco:
  ```bash
  docker build -t webnews_db .
  ```

  - Construir e iniciar o container que irá hospedar o banco:
  ```bash
  docker create --name webnews-api -p 3306:3306 webnews_db
  docker start webnews-api
  ```

  - Criar e acessar o ambiente virtual do PiP:
  ```bash
  # Para criar o ambiente virtual
  python -m venv venv
  
  #Acessando o ambiente virtual
    # Linux
    source venv/bin/activate

    # Para iniciar o ambiente virtual no Windows é necessário copiar o caminho completo do script 'activate.bat' que se encontra dentro do projeto em 'venv\Scripts\' e colá-lo no terminal. Ex:
    C:\Users\<seu_usuario>\Documentos\web-news_api\venv\Scripts\activate.bat
  ```

  - Executar o projeto:
  ```bash
  python setup.py
  ```
  > Não se preocupe com as dependências, o script que executa o projeto já instala as dependências a partir do arquivo requirements.txt