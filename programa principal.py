a=input("o que deseja?"
"[1] cadastrar-se"
"[2]alterar a senha"
"[3]login")
if a == "1":
import cadastro
cadastro.cadastro()
elif a == "2":
import alterandoasenha
alterandoasenha.alt()
elif a == "3":
import login
login.login()
else:
print('desculpa opcao nao localizada')