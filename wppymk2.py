


class Message(object):

    def __init__(self, ano, mes, dia, hora, text, whose):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.text = text
        self.whose = whose
        
class Person(object):
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.numeroimg = 0
        self.numeromsg = 0

    

people = []

file = open("wtf.txt", encoding='utf8')

data = file.readline()

lista = []

n = 0

while True:
    n = n + 1
    line = file.readline()
    if line == '':
        break
    lista.append(line)
u = 0
for data in lista:
    u = u +1
    print(u)
    if "mudou seu n" in data:
        continue
    if "adicionou" in data:
        continue
    if "saiu" in data:
        continue
    if "alterou a imagem deste grupo" in data:
        continue
    if "alterou o nome de" in data:
        continue
    if "Se você escrever" in data:
        continue
    if "Você removeu" in data:
        continue
    if "alterado" in data:
        continue   

    try:    
    #   â€Ž20/09/16, 18:51 - Oscar Henrichs: No puedo   hj
        daymonthyearhour = data.split(" - ")[0]
        namestring = data.split(" - ")[1]
        daymonthyear = daymonthyearhour.split(", ")[0]
        hour = daymonthyearhour.split(", ")[1]
        day = daymonthyear.split("/")[0]
        month = daymonthyear.split("/")[1]
        year = daymonthyear.split("/")[2]
        name = namestring.split(": ")[0]
        string = namestring.split(": ")[1]
        
    except:
        pass

# criando o objeto mensagemdef __init__

# (self, ano, mes, dia, hora, min, text, whose)
    isinpeople = False

    thismessage = Message(year, month, day, hour, string, name)
    for x in people:
        if x.name == name:
            isinpeople = True  # verificando se a pessoa existe na lista de pe

    if isinpeople is False:
        people.append(Person(name))  # criou a pessoa

    for x in people:
        if x.name == thismessage.whose:
            thisperson = x  # selecionando a pessoa na lista de pessoas para f

            
    thisperson.messages.append(thismessage)

print("BREKAO")


people.sort(key = lambda num: [x.messages for x in people])

for x in people:
    print(x.name, len(x.messages))

for x in people:
    for y in x.messages:
        if x.name != y.whose:
            print("DEU ERRO")
file.close()