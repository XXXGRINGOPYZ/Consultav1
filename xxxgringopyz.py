import requests,os,time

a = '\033[04;33m'
v = '\033[01;32m'
f = '\033[m'
c = '\033[01;36m'
az = '\033[01;34m'
ve = '\033[04;31m'

os.system ("clear")
while True:
 def menu():  print(f'{ve}=============================================={ve}')
print(f'{v}Seja bem vindo ao painel 𝑋.𝑋.𝑋-ꪶ͢𝐺𝑅𝐼𝑵𝐺𝛩ꫂ.py fdpt')
print(f'{ve}=============================================={ve}')
print(f'{az}vllw{f} {c}@MyDickXD{f} {az}ajudou muito!!!seu mito{f}')
print( )
print(f"{a}[{v}1{a}]{v}CONSULTA CEP{f}")
def cep():cep = input(f'{ve}DIGITE O CEP QUE DESEJA CONSULTA: {ve}')
if len(cep) != 8:
 exit()
elif len(cep) == 8:
 r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep));data = r.json( )
print(f'{v}consulta realizada: {v}')
print( )
print('CEP: {} '.format(data['cep' ]))
print('Logradoura: {}'.format(data['logradouro']))
print('Cidade: {}'.format(data['bairro' ]))
print('Localidade: {}'.format(data['localidade']))
print('complemento: {}'.format(data['complemento']))
print('Ibge: {}'.format(data['ibge' ]))
print('Uf: {}'.format(data['uf' ]))
print('DDD: {}'.format(data['ddd' ]))
print('Gia: {}'.format(data['gia']))
print('Siafi: {}'.format(data['siafi']))
print( )
time.sleep(3)
def cep2():
 d = input("Nova consulta ? [S/N]")
if d == "S" or d == "s":
 while True:
   os.system("clear");cep();cep2()
elif d == "n" or d == "N":
  menu2()
try:
    def menu2():
      menu()
    per = input(">>>")
    if per == "1" or per == "01":
       os.system("clear");cep();cep2()

except KeyboardInterrupt:
   exit()
try:
   menu()
   per = input(">>>")
   if per == "1" or per == "01":
     os.system("clear");cep();cep2()

except:
  exit()