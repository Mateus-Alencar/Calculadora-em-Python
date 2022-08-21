import math
from tkinter import *

class Calc:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Calculadora")
        self.janela.resizable(0,0)
        self.janela.config(bg="black")

        self.telaNumeros = Entry(self.janela, font="likhan 40", bg="#696969", fg="black", width=14)
        self.telaNumeros.pack()

        self.frame = Frame(self.janela)
        self.frame.pack()

        self.botao1 = Button(self.frame, bg="#4F4F4F", bd=6, text="1", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(1))
        self.botao1.grid(row="0", column="0")
        self.botao2 = Button(self.frame, bg="#4F4F4F", bd=6, text="2", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(2))
        self.botao2.grid(row="0", column="1")
        self.botao3 = Button(self.frame, bg="#4F4F4F", bd=6, text="3", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(3))
        self.botao3.grid(row="0", column="2")

        self.botao4 = Button(self.frame, bg="#4F4F4F", bd=6, text="4", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(4))
        self.botao4.grid(row="1", column="0")
        self.botao5 = Button(self.frame, bg="#4F4F4F", bd=6, text="5", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(4))
        self.botao5.grid(row="1", column="1")
        self.botao6 = Button(self.frame, bg="#4F4F4F", bd=6, text="6", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(6))
        self.botao6.grid(row="1", column="2")

        self.botao7 = Button(self.frame, bg="#4F4F4F", bd=6, text="7", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(7))
        self.botao7.grid(row="2", column="0")
        self.botao8 = Button(self.frame, bg="#4F4F4F", bd=6, text="8", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(8))
        self.botao8.grid(row="2", column="1")
        self.botao9 = Button(self.frame, bg="#4F4F4F", bd=6, text="9", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(9))
        self.botao9.grid(row="2", column="2")

        self.botaoc = Button(self.frame, bg="#D2691E", bd=6, text="c", font='arial 20 bold', fg="white", width=5, height=2, command=lambda:self.limparTela())
        self.botaoc.grid(row="4", column="0")
        self.botao0 = Button(self.frame, bg="#4F4F4F", bd=6, text="0", font='arial 20 bold', fg="red", width=5, height=2, command=lambda:self.toqueNumeros(0))
        self.botao0.grid(row="3", column="1")
        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="=", font='arial 20 bold', fg="white", width=11, height=2, command=lambda:self.calcularTotal())
        self.botaoIgual.grid(row="4", column="1", columnspan="2")

        self.botaoDiv = Button(self.frame, bg="#1c1c1c", bd=6, text="/", font='arial 20 bold', fg="white", width=5, height=2, command=lambda:self.toqueNumeros('/'))
        self.botaoDiv.grid(row="3", column="2")
        self.botaoMult = Button(self.frame, bg="#1c1c1c", bd=6, text="*", font='arial 20 bold', fg="white", width=5, height=2, command=lambda:self.toqueNumeros('*'))
        self.botaoMult.grid(row="1", column="3")
        self.botaoSub = Button(self.frame, bg="#1c1c1c", bd=6, text="-", font='arial 20 bold', fg="white", width=5, height=2, command=lambda:self.toqueNumeros('-'))
        self.botaoSub.grid(row="2", column="3")
        self.botaoAd = Button(self.frame, bg="#1c1c1c", bd=6, text="+", font='arial 20 bold', fg="white", width=5, height=5, command=lambda:self.toqueNumeros('+'))
        self.botaoAd.grid(row="3", column="3", rowspan="2")

        self.botaoMenosUm = Button(self.frame, bg="#1c1c1c", bd=6, text="<", font='arial 20 bold', fg="white", width=5, height=2, command=lambda:self.menosUm())
        self.botaoMenosUm.grid(row="0", column="3")
        self.botaoMenosUm = Button(self.frame, bg="#1c1c1c", bd=6, text="√", font='arial 20 bold', fg="white", width=5, height=2, command=lambda:self.raiz())
        self.botaoMenosUm.grid(row="3", column="0")

        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="sen", font='arial 20 bold', fg="white", width=5, height=1, command=lambda:self.sen())
        self.botaoIgual.grid(row="5", column="0")
        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="cos", font='arial 20 bold', fg="white", width=5, height=1, command=lambda:self.cos())
        self.botaoIgual.grid(row="5", column="1")
        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="tan", font='arial 20 bold', fg="white", width=5, height=1, command=lambda:self.tan())
        self.botaoIgual.grid(row="5", column="2")
        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text=".", font='arial 20 bold', fg="white", width=5, height=3, command=lambda:self.ponto())
        self.botaoIgual.grid(row="5", column="3", rowspan="2")

        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="%", font='arial 20 bold', fg="white", width=5, height=1, command=lambda:self.toqueNumeros('/100*'))
        self.botaoIgual.grid(row="6", column="0")
        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="^", font='arial 20 bold', fg="white", width=5, height=1, command=lambda:self.potencia())
        self.botaoIgual.grid(row="6", column="1")
        self.botaoIgual = Button(self.frame, bg="#1c1c1c", bd=6, text="π", font='arial 20 bold', fg="white", width=5, height=1, command=lambda:self.telaNumeros.insert(0, 3.14))
        self.botaoIgual.grid(row="6", column="2")

        self.janela.mainloop()
    

    def potencia(self):
        self.telaNumeros.insert(END, '**')
    

    def ponto(self):
        self.telaNumeros.insert(END, '.')


    def tan(self):
        tangente = math.tan(eval(self.telaNumeros.get()))
        self.telaNumeros.delete(0, END)
        self.telaNumeros.insert(0, tangente)


    def cos(self):
        cosseno = math.cos(eval(self.telaNumeros.get()))
        self.telaNumeros.delete(0, END)
        self.telaNumeros.insert(0, cosseno)


    def sen(self):
        seno = math.sin(eval(self.telaNumeros.get()))
        self.telaNumeros.delete(0, END)
        self.telaNumeros.insert(0, seno)


    def raiz(self):
        resultRaiz = math.sqrt(eval(self.telaNumeros.get()))
        self.telaNumeros.delete(0, END)
        self.telaNumeros.insert(0, resultRaiz)


    def toqueNumeros(self, num):
        self.num = num
        '''if num == '/100*':
            self.telaNumeros.insert(END, '%')
        else:
            self.telaNumeros.insert(END, num)'''
        self.telaNumeros.insert(END, num)


    def limparTela(self):
        self.telaNumeros.delete(0, END)

    def menosUm(self):
        equacao = str(self.telaNumeros.get())
        finalstr = equacao[:-1]
        self.telaNumeros.delete(0, END)
        self.telaNumeros.insert(0, str(finalstr))


    def calcularTotal(self):
        '''if self.num == '%':
            str(eval(self.telaNumeros.get())).index('%') = '/100*' '''
        result = eval(self.telaNumeros.get())
        self.telaNumeros.delete(0, END)
        self.telaNumeros.insert(0, str(result))


Calc()
