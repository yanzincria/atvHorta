from planta_poo import Planta
sair=0
p1 = Planta()
opcoes = int(input(" Olá, boa tarde. Qual serviço você deseja: \n [1] cadastrar \n[2] consultar plantas\n [3] consultar planta \n[4] deletar Planta \n[5] atualizar informações"))
while sair == 0:
    opcoes = int(input(" Olá, boa tarde. Qual serviço você deseja: \n [1] cadastrar \n[2] consultar plantas\n [3] consultar planta \n[4] deletar Planta \n[5] atualizar informações"))
    if opcoes ==1:
        nome =input("informe o nome da planta: ") 
        id = int(input("informe o id da planta: "))
        data_plantio = input("informe a data de plantio: ")
        tipo = input("informe o tipo da planta: ")
        quantidade =int(input("Informe a quantidade da (s) plantas: "))

        p1.cadastrarPlanta(nome,id, data_plantio, tipo, quantidade)
    elif opcoes ==2: 
        p1.consultarPlanta()
    elif opcoes ==3:
        id = id = int(input("Infrome o Id da Planta que você deseja consultar: "))
        p1.consultarPlantaIndividual(id)
    elif opcoes == 4:
        id = int(input("Infrome o Id da Planta que você deseja deletar: "))
        p1.deletarPlanta(id)
    elif opcoes ==5:
        id = int(input("Informe o código da planta: "))
        nome = input("Informe o novo nome da planta: ")
        p1.atualizarPlanta(nome, id)
    sair = int(input("Deseja sair da horta: \n[1] Sim\n [0] Não "))
    
    













