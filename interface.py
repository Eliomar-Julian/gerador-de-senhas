from tkinter import (
    Tk, Label, Button, ttk, BooleanVar,
    Entry, PhotoImage, Frame, Checkbutton
)


class GenaratePassWord(Tk):
    def __init__(self):
        super(GenaratePassWord, self).__init__()
        self.iconbitmap('./img/password.ico')
        self.title('Gerador de Senha')
        self.resizable(False, False)
        self.geometry(
            f'''{500}x{400}+{(self.winfo_screenwidth(
            )- 500) // 2}+{(self.winfo_screenheight(
            ) - 500) // 3}'''
        )
        self.variavel1 = BooleanVar(self)
        self.variavel1.set(False)
        self.variavel2 = BooleanVar(self)
        self.variavel2.set(False)
        self.variavel3 = BooleanVar(self)
        self.variavel3.set(False)
        self.variavel4 = BooleanVar(self)
        self.variavel4.set(False)
        self.variavel5 = BooleanVar(self)
        self.variavel5.set(False)

        self.frame1 = Frame(self)
        self.frame2 = Frame(self)
        self.frame3 = Frame(self)
        self.frame4 = Frame(self)
        
        self.img_menu   = PhotoImage(file='./img/menu.png')
        self.img_copia  = PhotoImage(file='./img/clipboard.png')
        self.img_play   = PhotoImage(file='./img/play.png')
        self.img_play_reduzida  = self.img_play.subsample(3)
        self.img_copia_reduzida = self.img_copia.subsample(2)
        self.img_menu_reduzida  = self.img_menu.subsample(3)
        
        self.texto      = Label(
            self.frame1, text='Gerador de senhas aleatórias'
        )
        self.display    = Entry(
            self.frame2, font=('Arial', 15, 'bold'), width=38
        )
        self.copiar_bt  = Button(
            self.frame2,
            relief='solid',
            bd=1,
            image=self.img_copia_reduzida,
            command=self.copiar
        )
        self.botao_gerar = Button(
            self.frame3,
            text=' Gerar Senha ',
            compound='left',
            image=self.img_play_reduzida,
            relief='solid',
            width=250,
            font=('Arial', 12, 'bold')
        )
        self.botao_menu = Button(
            self.frame3,
            text=' MENU ',
            compound='left',
            image=self.img_menu_reduzida,
            relief='groov',
            bd=1,
            width=200,
            font='Arial 12 bold'
        )
        self.caixa = ttk.LabelFrame(
            self.frame4,
            text='Opções de Senha'
        )
        self.alpha_upper    = Checkbutton(
            self.caixa,
            text=f'USAR: ABCDEFGHIJKLMNOPQRSTUVWXYZ{" "*75}',
            var=self.variavel1
        )
        self.alpha_lower    = Checkbutton(
            self.caixa,
            text='USAR: abcdefghijklmnopqrstuvwxyz',
            var=self.variavel2
        )
        self.alpha_numeric  = Checkbutton(
            self.caixa, 
            text='USAR: 0 1 2 3 4 5 6 7 8 9',
            var=self.variavel3
        )
        self.alpha_simbol   = Checkbutton(
            self.caixa,
            text='USAR: !#$%_()*+-/<>=@^~',
            var=self.variavel4
        )
        self.alpha_confuse  = Checkbutton(
            self.caixa,
            text='NAO usar: 1liLI0oO',
            var=self.variavel5
        )
        self.info = Label(self.caixa, text='Comprimento da Senha')
        self.comprimento = ttk.Combobox(
            self.caixa,
            values=[
                4, 8, 12, 16, 20, 24
            ]
        )
        self.comprimento.current(1)

        #disposição na tela
        
        self.frame1.pack(fill='x')
        self.texto.pack(side='left')
        self.frame2.pack(fill='x')
        self.display.pack(side='left', padx=10, pady=10)
        self.copiar_bt.pack(side='right', padx=5, ipadx=3, ipady=3)
        self.frame3.pack(fill='x')
        self.botao_gerar.pack(side='left', padx=10, pady=10)
        self.botao_menu.pack(side='right', padx=10, pady=10)
        self.frame4.pack(fill='x')
        self.caixa.pack(padx=10, pady=10, side='left', fill='x')
        self.alpha_upper.pack()
        self.alpha_lower.pack(anchor='w')
        self.alpha_numeric.pack(anchor='w')
        self.alpha_simbol.pack(anchor='w')
        self.alpha_confuse.pack(anchor='w')
        self.info.pack(anchor='sw')
        self.comprimento.pack(fill='x', padx=10, pady=10, anchor='n')
    
    def copiar(self):
        self.clipboard_clear()
        self.display.clipboard_append(self.display.get())
