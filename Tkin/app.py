import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

def connection():
    conn = pymysql.connect(
        host ='localhost',
        user='root',
        password='',
        db='clientes_db'
    )
    return conn


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tags="orow")

    my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',12))
    my_tree.grid(row=8,column=0,columnspan=5,rowspan=11,padx=10,pady=20)



def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def cadastrar():
    estid =str(estiEntry.get())
    nome = str(nomeEntry.get())
    s_nome = str(s_nomeEntry.get())
    endereco = str(enderecoEntry.get())
    telefone = str(telefoneEntry.get())

    if (estid =="" or estid==" ") or (nome=="" or nome==" ") or (s_nome=="" or s_nome==" ") or (endereco=="" or endereco ==" ") or (telefone =="" or telefone==" "):
        messagebox.showinfo("Error", "Você deve preecher todos os campos")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes VALUES('"+estid+"','"+nome+"','"+s_nome+"','"+endereco+"','"+telefone+"')")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Este Cliente já está cadastrado")
            return
        
    refreshTable()

def resetar():
    resposta = messagebox.askquestion("ATENÇÃO!","Deletar todos os dados cadastrais?")
    if resposta != "yes":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Erro resetar")
            return
        
        refreshTable()
        
def deletar():
        resposta = messagebox.askquestion("ATENÇÃO!","Deletar este cadastro?")
        if resposta != "yes":
            return
        else:
            selected_item = my_tree.selection()[0]
            deleteData = str(my_tree.item(selected_item)['values'][0])
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM CLIENTES WHERE ESTID ='"+str(deleteData)+"'")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error","Erro deletar")
                return
        
        refreshTable()

def selecionar():
    try:
        selected_item = my_tree.selection()[0]
        estid = str(my_tree.item(selected_item)['values'][0])
        nome = str(my_tree.item(selected_item)['values'][1])
        s_nome = str(my_tree.item(selected_item)['values'][2])
        endereco = str(my_tree.item(selected_item)['values'][3])
        telefone = str(my_tree.item(selected_item)['values'][4])

        setph(estid,1)
        setph(nome,2)
        setph(s_nome,3)
        setph(endereco,4)
        setph(telefone,5)

    except:
        messagebox.showinfo("ERROR","Erro selecionar")

def pesquisar():
    estid = str(estiEntry.get())
    nome = str(nomeEntry.get())
    s_nome =str(s_nomeEntry.get())
    endereco = str(enderecoEntry.get())
    telefone = str (telefoneEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes where ESTID ='"+estid+"' or nome ='"+nome+"' or s_nome ='"+s_nome+"' or endereco ='"+endereco+"' or telefone='"+telefone+"' ")

    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit
        conn.close
    except:
        messagebox.showinfo("ERROR","Erro de pesquisar")

def atualizar():
    SelectedEstID =''

    try:
        selecte_item =my_tree.selection()[0]
        SelectedEstID = str(my_tree.item(selecte_item)['values'][0])

    except:
        messagebox.showinfo("ERROR","Erro de atualizar")

    estid = str(estiEntry.get())
    nome = str(nomeEntry.get())
    s_nome = str(s_nomeEntry.get())
    endereco = str(enderecoEntry.get())
    telefone = str(telefoneEntry.get())

    if (estid == "" or estid == " ") or (nome =="" or nome ==" ") or (s_nome =="" or s_nome==" ") or (endereco =="" or endereco == " ") or (telefone =="" or telefone ==" "):
        messagebox.showinfo("ERROR","Favor, preencher todos os campos.")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET ESTID='"+
            estid+"',NOME='"+
            nome+"',S_NOME='"+
            s_nome+"',ENDERECO='"+
            endereco+"',TELEFONE='"+
            telefone+"'WHERE ESTID='"+
            SelectedEstID+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("ERROR","Este ID existe.")
            return
        
    refreshTable()


root = Tk()
root.title("Cadastro Cliente")
root.geometry("11177x670")

my_tree = ttk.Treeview(root)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

def setph(word,num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)

cad_icone = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\cadastrar.png')
atualizar_icone = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\atualizar.png')
deletar_icone = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\deletar.png')
pesquisar_icone = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\pesquisar.png')
resetar_icone = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\reiniciar.png')
selecionar_icone = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\selecionar.png')

img = PhotoImage(file='C:\\Users\Pichau\OneDrive\Área de Trabalho\Tkin\\img.png')
root.iconphoto(FALSE,img)
label = Label(root, text="Cadastro de Clientes", font=('arial', 30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

estidLabel = Label(root,text="Cliente ID:",font=('Arial',15))
nomeLabel = Label(root, text="Nome:",font=('Arial',15))
s_nomeLabel = Label(root,text='S_Nome:',font=('Arial',15))
enderecoLabel = Label(root, text="Endereço:", font=('Arial',15))
telefoneLabel = Label(root,text="Telefone:",font=('Arial',15))

estidLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
nomeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
s_nomeLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
enderecoLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
telefoneLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

estiEntry = Entry(root,width=55,bd=1,font=('Arial',15),textvariable=ph1)
nomeEntry = Entry(root,width=55,bd=1,font=('Arial',15),textvariable=ph2)
s_nomeEntry = Entry(root,width=55,bd=1,font=('Arial',15),textvariable=ph3)
enderecoEntry = Entry(root,width=55,bd=1,font=('Arial',15),textvariable=ph4)
telefoneEntry = Entry(root,width=55,bd=1,font=('Arial',15),textvariable=ph5)

estiEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
nomeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
s_nomeEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
enderecoEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
telefoneEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)

def Limpar():
    estiEntry.delete(0,'end')
    nomeEntry.delete(0,'end')
    s_nomeEntry.delete(0,'end')
    enderecoEntry.delete(0,'end')
    telefoneEntry.delete(0,'end')
    estiEntry.focus_set()

LimparBtn = Button(
    root,text="Limpar Campos", padx=50,pady=5,width=8,
    bd=1,font=('Arial',15),bg="#F4FE82",command=Limpar)
LimparBtn.grid(row=0,column=5,columnspan=1,rowspan=2)


cadastrarBtn = Button(
    root,text="Cadastrar", anchor="center", width=90,
    bd=1, font=('Arial',15),bg="#84F894",compound=TOP, image= cad_icone, command=lambda:[cadastrar(),Limpar()])

atualizarBtn = Button(
    root,text="Atualizar",anchor= "center",width=90,
    bd=1,font=('Arial',15),bg="#84E8F8", compound=TOP, image= atualizar_icone, command=atualizar)

deletarBtn = Button(
    root,text="Deletar",anchor="center",width=90,
    bd=1,font=('Arial',15),bg="#FF9999", compound=TOP, image= deletar_icone, command= deletar)

pesquisarBtn = Button(
    root,text="Pesquisar",anchor="center",width=90,
    bd=1,font=('Arial',15),bg="#F4FE82",compound=TOP,image=pesquisar_icone,command=pesquisar)

resetarBtn = Button(
    root,text="Resetar",anchor="center",width=90,
    bd=1,font=('Arial',15),bg="#F398FF",compound=TOP,image=resetar_icone, command=resetar)

selecionarBtn = Button(
    root,text="Selecionar",anchor="center",width=90,
    bd=1,font=('Arial',15),bg="#EEEEEE",compound=TOP,image=selecionar_icone,command=selecionar)

cadastrarBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
atualizarBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deletarBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
pesquisarBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetarBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selecionarBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading",font=('Arial Bold',15,))

my_tree['columns'] = ("Est ID", "Nome","S_Nome","Endereco","Telefone")

my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Est ID", anchor=W,width=170)
my_tree.column("Nome", anchor=W,width=150)
my_tree.column("S_Nome",anchor=W,width=150)
my_tree.column("Endereco",anchor=W,width=150)
my_tree.column("Telefone",anchor=W,width=150)

my_tree.heading("Est ID",text="Cliente ID",anchor=W)
my_tree.heading("Nome",text="Nome",anchor=W)
my_tree.heading("S_Nome",text="S_nome",anchor=W)
my_tree.heading("Endereco",text="Endereco",anchor=W)
my_tree.heading("Telefone",text="Telefone",anchor=W)

refreshTable()


root.mainloop()