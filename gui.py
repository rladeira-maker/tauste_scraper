from os import system as s
import PySimpleGUI as sg
from scraper_Tauste_v4 import main


sg.theme('DarkBlue')   # Add a touch of color

pages = ['/alimentos-saudaveis.html',
         '/artigos-de-festa.html',
         '/autos-e-ferramentas.html',
         '/bazar.html',
         '/bebidas-n-o-alcoolicas.html',
         '/bebidas-alcoolicas.html',
         '/cafe-da-manh.html',
         '/carnes-e-aves.html',
         '/especial-churrasco.html',
         '/frios.html',
         '/higiene-e-beleza.html',
         '/hortifruti.html',
         '/jardinagem.html',
         '/leites.html',
         '/limpeza.html',
         '/mercearia.html',
         '/padaria.html',
         '/pescados.html',
         '/pet-shop.html',
         ]
checks = [
    ["Alimentos Saudáveis", "Artigos de Festa", "Autos e Ferramentas",
        "Bazar", "Bebidas não alcoólicas", "Bebidas alcoólicas"],

    ["Café da Manhã", "Carnes e Aves", "Churrasco", "Frios",
        "Higiene e Limpeza", "Hortifruti"],

    ['Jardinagem', "Leites", "Limpeza", "Mercearia", "Padaria",
        "Pescados", "Pet Shop"],
]
column = [
    [[sg.Text('Selecione as seções\ndo mercado que\ndeseja pesquisar:',
            font=('Ubuntu', 11, 'bold'))]]] + [
    [[sg.Checkbox(text, pad=(5, 0), default=True, key=('-'+text+'-')
            )]
    for i, text in enumerate(check)] for j, check in enumerate(checks)
            ]

layout = [[sg.Column(column[i]) for i in range(4)],
[[sg.Button('Limpa Seleção', pad=((250,0),(0,0))), sg.Button('Inicia'),
            sg.Button('Sair'), sg.Checkbox('Apaga arquivos anteriores',
            font=('Ubuntu', 11, 'bold'), key='-Apaga-')]]]
window=sg.Window('Preços Tauste', layout, font=('Ubuntu\ Condensed',11))

while True:
    event, values = window.read()
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Limpa Seleção':
        for value in values:
            window[value]. Update(value=False)
    if event == 'Inicia':
        for idx, value in enumerate(values):
            if idx == 19: #o último elemento é -Apaga-/não está na lista
                break
            if values.get(value) is False:
                pages[idx] = ''

        pages = [j for i, j in enumerate(pages) if j != '']
        DELETE_FILE = values['-Apaga-'] is True
        s('clear')
        if not pages:
            quit()
        main(pages, DELETE_FILE)
        quit()
