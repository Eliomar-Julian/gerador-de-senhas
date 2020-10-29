from tkinter import (
    Toplevel, Button, Entry,
    END, ttk, messagebox
)
import sqlite3


class Gerenciador(Toplevel):
    def __init__(self, parent):        
        self.parent = parent
        Toplevel.__init__(self)
        self.geometry('400x200+400+50')
        self.resizable(False, True)
        self.dicionario = dict()
        conn = sqlite3.connect('./db/banco.db')
        curs = conn.cursor()
        curs.execute('''SELECT * FROM senhas''')
        
        for x in curs.fetchall():
            self.dicionario[x[0]] = x[1]
        
        conn.close()
        self.combo = ttk.Combobox(
            self,
            values=list(
                self.dicionario.keys()
            )
        )
        self.combo.bind(
            '<<ComboboxSelected>>',
            self.manipular
        )
        self.ver = Entry(
            self,
            width=250
        )
        bt = Button(
            self,
            text='Remover',
            command=self.remover
        )        
        self.combo.pack(pady=10)
        self.ver.pack(pady=5, ipady=5, ipadx=5, padx=10)
        bt.pack()

    def manipular(self, event):
        self.ver.delete(0, 100)
        self.ver.insert(
            0, self.dicionario[
                self.combo.get()
            ]
        )

    def remover(self):
        rm = self.combo.get()
        msg = messagebox.askyesno(
            icon='warning',
            title='confirmar',
            message='Tem certeza que quer retirar a senha de %s?' % rm
        )
        if msg != True:
            return
        conn = sqlite3.connect('./db/banco.db')
        cur = conn.cursor()
        cur.execute(
            '''DELETE FROM senhas WHERE rede=(?)''', [rm]
        )
        conn.commit()
        conn.close()
        self.destroy()