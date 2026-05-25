#=========================================================   FASE 1   ============================================================

#### VARIÁVEIS FASE
vida = 100;
energia = 50;
fase1=0
fase2=0
cabana = f"""
===xxx===xxx===XXX===XX===X===XX===XXX===xxx===xxx===
Caraca.. Você se deparou com um variável virulenta totalmente virulosa.
Ela acabou te virulando e você terminou descobrindo que deveria ter ido para o barco.
Perca 20 de life e lembre-se que a cada jogada você sempre perderá 10 de energia"""
barco = f"""
===xxx===xxx===XXX===XX===X===XX===XXX===xxx===xxx===
Ao chegar no barco você encontrou uma faca e um espelho.
Contudo, pode escolher apenas um dos itens pois está com os bolsos cheios.
Escolha apenas 1
"""


#### ABRE FASE
print(f"""      
                    ==========================================
                           FASE 1 - VOCÊ CHEGOU NA ILHA
                    ==========================================
Vida: {vida}
Energia: {energia}
""")

print("""===xxx===xxx===XXX===XX===X===XX===XXX===xxx===xxx===
Você encontrou na praia uma CABANA e um BARCO abandonado.
Mas a chuva está chegando e você só tem tempo para correr
para um dos dois lugares.

Pra onde você deseja ir?""")
fase1 = int(input("CABANA = 1       BARCO = 2\n\n"))

#### ESCOLHE FASE

while fase1 != 2:
    energia -= 10
    vida -= 20
    print(cabana)
    print(f"""\nVida: {vida}
Energia: {energia}

Tente novamente:""")
    fase1 = int(input("CABANA = 1       BARCO = 2\n\n"))

if fase1 == 2:
    energia -= 10
    vida = 100
    print(barco)
    fase2 = int(input("FACA = 1\n\nESPELHO = 2"))
    
    
#FASE 2 BARCO 2
else:
    print("=====================\nFASE 2\n=====================")
    energia -= 10
    vida = 100
print(f"""Energia: {energia}
Vida: {vida}
""")

fase2 = int(input(barco))
