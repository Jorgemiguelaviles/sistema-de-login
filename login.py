def login():
import shelve
a=shelve.open('dbcadastro.shelve')
email=input('digite o email')
senha=input('digite a senha')
if email in a.keys() and senha == a[email]['senha']:
print('login efetuado')
else:
print('email e/ou senha errados')