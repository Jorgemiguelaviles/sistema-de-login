def cadastro():
import shelve
email=input('digite o email')
a=shelve.open('dbcadastro.shelve')
if email in a.keys():
print('cliente ja cadastrado')
else:
usuario={}
senha=input("senha")
usuario[email]=email
usuario["senha"]=senha
a[email]=usuario
print('cliente cadastrado com sucesso')