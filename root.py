from interface import GenaratePassWord
from random import randint
from tkinter import messagebox


def gerador():
    
    # função que gera as senhas
    
    def gerar():
        senha = str()
        alfa_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alfa_lower = 'abcdefghijklmnopqrstuvwxyz'
        numeros = '0123456789'
        simbolos = '!#$%_()*+-/<>=@^~'
        trues = [
            app.variavel1.get(), app.variavel2.get(),
            app.variavel3.get(), app.variavel4.get()
        ]
        if True not in trues:
            messagebox.showwarning(
                icon='warning',
                title='Marque uma Opção',
                message='Marque ao menos uma opção'
            )
            return
        app.display.delete(0, 100)
        while True:
            if app.variavel1.get():
                senha = senha + alfa_upper[randint(0, 25)]
            if app.variavel2.get():
                senha += alfa_lower[randint(0, 25)]
            if app.variavel3.get():
                senha += numeros[randint(0, 9)]
            if app.variavel4.get():
                senha += simbolos[randint(0, 16)]
            if len(senha) >= int(app.comprimento.get()):
                break
        app.display.insert(0, senha)

    # instancia de minha classse

    app = GenaratePassWord()
    app.botao_gerar.config(command=gerar)
    app.mainloop()

# garantindo a chamada somente desse arquivo

if __name__ == '__main__':
    gerador()