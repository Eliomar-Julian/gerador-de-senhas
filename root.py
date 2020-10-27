from interface import GenaratePassWord
from random import randint
from tkinter import (
    messagebox, Menu, Entry,
    Toplevel, Label, Button
)
import sqlite3
from gerenciador import Gerenciador


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
            if app.variavel5.get():
                for x in '1liLI0oO':
                    if x in senha:
                        senha = senha.replace(
                            x, numeros[
                                randint(2, 8)
                            ]
                        )
            if len(senha) >= int(app.comprimento.get()):
                break
        app.display.insert(0, senha)

    # // adiciona senha ao banco

    def adicionar():
        def guardando():
            cur.execute(
                f'''INSERT INTO senhas (rede, senha)
                VALUES (?,?)''', [
                    nome.get(), 
                    app.display.get()
                ]
            )
            con.commit()
            con.close()
            top.destroy()
        
        top = Toplevel(app)
        top.geometry(
            f'''200x200+{(app.winfo_screenwidth(
            ) - 200) // 2}+{(app.winfo_screenheight(
            ) - 200) // 5}'''
        )
        lb = Label(
            top,
            text='Nome',
            font=('Marianna', 14, 'bold')
        )
        nome = Entry(top)
        bt = Button(
            top,
            text='Salvar', 
            command=guardando
        )
        lb.pack(side='top')
        nome.pack()
        bt.pack(side='bottom', pady=20)
        con = sqlite3.connect('./db/banco.db')
        cur = con.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS senhas 
                (rede TEXT NOT NULL, senha TEXT NOT NULL)'''
        )



    # instancia de minha classse

    app = GenaratePassWord()
    app.botao_gerar.config(command=gerar)
    menu_bar =  Menu(app.botao_menu, tearoff=0)
    menu_bar.add_command(
        label=f'Gerenciar Senhas{" "*23}',
        command=lambda:Gerenciador(app)
    )
    menu_bar.add_command(
        labe='Limpar Display',
        command=lambda:app.display.delete(0, 100)
    )
    menu_bar.add_command(
        label='Salvar Senha',
        command=adicionar
    )
    app.botao_menu.config(menu=menu_bar)
    app.mainloop()

# garantindo a chamada somente desse arquivo

if __name__ == '__main__':
    gerador()