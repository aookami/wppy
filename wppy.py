class Person(object):

    def __init__(self, name):
        self.name = name

    messages = []


class Message(object):

    def __init__(self, ano, mes, dia, hora, min, text, whose):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.hora = hora
        self.text = text
        self.whose = whose


people = []

file = open("wtf2.txt", encoding='utf8')

data = file.readline()

print(data)
data = file.readline()
data = file.readline()
data = file.readline()
lista = []

n = 0

while True:
    n = n + 1
    line = file.readline()
    if line == '':
        break
    lista.append(line)

for data in lista:
    checknumberchange = "mudou seu número de telefone para um novo número. Toque para enviar uma mensagem ou para adicionar o novo número."
    checkadded = "adicionou"

    if checknumberchange in data:
        continue
    if checkadded in data:
        continue
    if "saiu" in data:
        continue
    if "alterou a imagem deste grupo" in data:
        continue
    if "alterou o nome de" in data:
        continue

    if "PM" in data:
        ampm = "PM"
        splitdata = data.split("PM")

    if "AM" in data:
        ampm = "PM"
    date = splitdata[0]

    splitdate = date.split("/")
    splitdate.append(splitdate[2].split(", ")[0])
    splitdate.append(splitdate[2].split(", ")[1])
    splitdate.pop(2)
    splitdate.append(ampm)
    
    horaaux = splitdate[3].split(":")[0]
    minaux = splitdate[3].split(":")[1]

    if ampm == "PM":
        horaaux = str(int(horaaux) + 12)
    if int(horaaux) >= 24:
        horaaux = str(int(horaaux) - 24)

    splitdate.pop(3)
    splitdate.pop(3)

    splitdate.append(horaaux)
    splitdate.append(minaux)
    # aqui 0-dia 1-mes 2-ano 3-hora 4- min

    nameandstring = splitdata[1]
    name = nameandstring.split(": ")[0]  # temos o nome em name
    string = nameandstring.split(": ")[1]

    isinpeople = False
# criando o objeto mensagemdef __init__

# (self, ano, mes, dia, hora, min, text, whose)

    thismessage = Message(splitdate[2], splitdate[1], splitdate[0], horaaux, minaux, string, name)
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
for x in people:
    for y in x.messages:
        print(x.name, y.whose)
print(n)

file.close()
