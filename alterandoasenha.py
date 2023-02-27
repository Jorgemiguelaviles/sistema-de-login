def alt():
import shelve
a=shelve.open('dbcadastro.shelve')
email=input('digite o email')
if email in a.keys():
senha=input('digite a nova senha')
repsenha=input('repita a nova senha')
if senha == repsenha:
usuario={}
usuario['senha']=senha
a[email]=usuario
print('senha alterada')
elif senha == a[email]['senha']:
print('essa é a sua senha antiga')
else:
print('email não localizado')