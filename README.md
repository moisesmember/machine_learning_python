## Projeto Web Scraping e Machine Learning do Histórico da Mega-Senna

### Para o funcionamento desse projeto, faz-se necessário das seguintes importações:
``` pip install beautifulsoup4 ```
``` pip install requests ```
``` pip install pymongo ```
``` pip install pandas ```

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
<a href="https://www.resultadosmegasena.com.br/resultados-anteriores" target="_blank">link - fonte do datasets (extração via WEB SCRAPING)</a>

### Extração
<p>
Após a extração através da técnica de Ciência de Dados Web-Scraping, os dados no formato desejado para se trabalhar posteriomente 
  será armazenado no MongoDB e arquivo Json
</p>

### Referência utilizada
<a href="https://blog.geekhunter.com.br/como-fazer-um-web-scraping-python/" target="_blank">Fonte utilizada para elaboração</a>

<a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">Sobre a biblioteca BeautifulSoup</a>

<a href="https://pythonbasics.org/pandas-json/" target="_blank">JSON with Python Pandas</a>

<a href="https://medium.com/data-hackers/escrita-e-leitura-de-arquivos-csv-em-python-6a256c608818">CSV em Python</a>

