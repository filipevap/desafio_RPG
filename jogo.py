'''Criem um jogo chamado A Ilha dos Códigos Perdidos.

O jogo precisa ter:

Nome do jogador;
Idade;
Vida inicial de 100;
Energia inicial de 50;
Pelo menos 5 fases;
Escolhas com if/elif/else;
Pelo menos 1 while;
Pelo menos 1 for;
Uso de operadores matemáticos;
Uso de operadores relacionais;
Uso de and, or ou not;
final de vitória ou derrota.'''

######## A Ilha dos Códigos Perdidos ########

######## Apresentação do joguinho:
print("Seja bem vindo à Ilha dos Códigos Perdidos, uma terra cheia de escolhas e blábláblá")


######## Conhecer o jogador:
nomejogador = input("Qual o seu nome?")
idadejogador = int(input("Qual a sua idade?")
vida = 100;
energia = 50;

print(f"""{nomejogador}, você está pronto para a maior aventura de sua vida?
Será que o seu coraçãozinho, no auge dos {idadejogador} anos aguenta essa emoção?
Você começa essa aventura com 'life' de {vida}pts e energia em {energia}pts""")


#=========================================================   FASE 1   ============================================================
# Chegou na Ilha
vida = 100;
energia = 50;

print(f"""=====================\nFASE 1 - VOCÊ CHEGOU NA ILHA\n=====================
Energia: {energia}
Vida: {vida}

""")
final1 = 0
print("""Você encontrou na praia uma CABANA e um BARCO abandonado.
Mas a chuva está chegando e você só tem tempo para correr para um dos dois lugares.
Pra onde você deseja ir?""")
final1 = int(input("CABANA = 1\n\nBARCO = 2")

####
             
if final1 != 1  
    fase2, final1 = int(input(f"""Caraca.. Você se deparou com um variável virulenta totalmente virulosa.
    Ela acabou te virulando e você terminou descobrindo que deveria ter ido para o barco.
    Digite '2' para ir para o BARCO"""))
final1 = 0
             
else final1 == 1:
    energia -= 10
    vida = 100
print(f"""Energia: {energia}
Vida: {vida}
""")
    
    
#FASE 2 BARCO 2
else:
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
print(f"""Energia: {energia}
Vida: {vida}
""")

    fase2 = int(input("Ao chegar no barco você encontrou uma faca e um espelho. Contudo, pode escolher apenas um dos itens pois está com os bolsos cheios. Escolha apenas 1\nFaca - 3            Espelho - 4"))

oioioi

#=========================================================   FASE 2   ============================================================
#FASE 3 - faca e espelho
if fase2 == 2: #ESCOLHA FACA
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
    print(f"Energia: {energia}\nVida: {vida}")

    fase3 = int(input("""Ao chegar no barco você encontrou uma faca e um espelho.
    Contudo, pode escolher apenas um dos itens pois está com os bolsos cheios.
    Escolha apenas 1.
    Faca - 3
    Espelho - 4"""))

elif fase3 == 3:
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
    print(f"Energia: {energia}\nVida: {vida}")
  
    print("meu deus, que desastrado!!! Você acabou tropeçando na tábua do barco e caiu sobre a faca... Perca 50 de Energia")

else:
    print("escolheu o espelho")
#=========================================================   FASE 2   ============================================================

energia -= 10


#=========================================================   FASE 2   ============================================================

energia -= 10
