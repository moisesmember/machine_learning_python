from dao.WebScrapingDao import WebScrapingDao # Importação da classe Dao com MongoDB

megaSenna = WebScrapingDao()
historico = megaSenna.listAllMegaSenna()
print(historico)