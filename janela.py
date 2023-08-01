import requests #Requests é um biblioteca, um pacote de código. Para instalar usar: pip install requests
from tkinter import * #Pegando todas as informações da biblioteca tkinter. 

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto #editanto o parâmetro text do texto_cotacoes


janela = Tk() #Criando uma janela com tk. TK é um código do tkinter que cria a janela.
janela.title("Cotação Atual das Moedas") #Adicionando o título da janela.

texto_orientecao = Label(janela, text="Clique no botão para ver as cotações das moedas.") #Um pedaço de texto dentro da janela é chamado de Label.
texto_orientecao.grid(column=0, row=0, padx=10, pady=10) #grid, usado para escolher a posição do texto. Pad é a distância do texto e o que será inserido depois.

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes) #Button está na biblioteca do tkinter. Janela, lugar onde o botão vai ficar. Command, comando que irá executar a função pegar_cotacoes.
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop() #mainloop deixa a janela exibida. Garante que a janela vai funcionar.
