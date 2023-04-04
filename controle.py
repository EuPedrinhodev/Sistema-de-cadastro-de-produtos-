from PyQt5 import uic,QtWidgets
import mysql.connector
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cadastro_produtos'



)
cursor = banco.cursor()
print(banco)
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    print('Código:',linha1)
    print('Descrição:',linha2)
    print('Preço:',linha3)

    categoria = ''

    if formulario.radioButton.isChecked():
        print('Categoria Informatica foi selecionado')
        categoria ='Eletronicos'
    elif formulario.radioButton_2.isChecked():
        print('Categoria Alimentos foi selecionada')
        categoria ='Informatica'
    else:
        print('Categoria Eletrônicos foi selecionada')
        categoria ='Alimentos'
    print('codigo:',linha1)
    print('Descrição:',linha2)
    print('preço',linha3)

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO produtos (codigo,descrição,preço,categoria) VALUES (%s,%s,%s,%s)'
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execut(comando_SQL,dados)
    banco.commit()



app=QtWidgets.QApplication([])
formulario=uic.loadUi('formulario.ui')
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()

