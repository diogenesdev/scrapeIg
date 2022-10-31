# scrapeIg

Este scrapper foi desenvolvido com as seguintes tecnologias:
- Python
- Flask
- HTML
- CSS

<hr>

## Instruções para instalação

Para rodar localmente, seguir os passos.

- Rodar o comando ``pip install <pacote>`` nos seguintes pacotes:
    - instagramy
    - requests
    - flask


Para Mac M1 
``python3 -m pip install <pacote>``


- Após isso, via terminal, navegar até o diretório raíz da aplicação e executar os seguintes comandos:
    - `` $env:FLASK_APP = "index" `` (nome do arquivo principal que chama as outras classes/arquivos)
    - `` $env:FLASK_ENV = "development" `` (ambiente que a aplicação vai rodar)
    - `` flask run `` (inicia a aplicação no ambiente local. ``localhost:5000``)


Para OSX(Mac)
``export FLASK_APP = "index" ``
``export FLASK_ENV = "development" ``
