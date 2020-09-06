## Projeto Web Scraping e Machine Learning do Histórico da Mega-Senna

### Para o funcionamento desse projeto, faz-se necessário das seguintes importações:
``` pip install beautifulsoup4 ```
``` pip install requests ```
``` pip install pymongo ```

<p>Foi realizado a criação de um ambiente de virtualização em Python para execução do projeto</p>
<ul>
  <li>Crie uma Pasta</li> 
  <li>Execute para criar o ambiente: python -m venv env</li> 
  <li>Execute para rodar o ambiente: ENV\SCRIPTS\activate.bat</li> 
 </ul>

#### Objetivo
<p>O Objetivo desse projeto é extrair o histórico de resultados da Mega-Senna afim de realizar treinamentos através de técnicas em 
  Machine Learning para descoberta de possíveis padrões
</p>
<a href="https://www.resultadosmegasena.com.br/resultados-anteriores">link - fonte do datasets (extração via WEB SCRAPING)</a>

### Extração
<p>
Após a extração através da técnica de Ciência de Dados Web-Scraping, os dados no formato desejado para se trabalhar posteriomente 
  será armazenado no MongoDB e arquivo Json
</p>

### Referência utilizada
<a href="https://blog.geekhunter.com.br/como-fazer-um-web-scraping-python/">Fonte utilizada para elaboração</a>

