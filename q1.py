hp = 100
qtd_ataque = 0
dano = [20, 35, 10, 50, 80]

for i in range(len(dano)):
    if(hp > 0):
        hp-=  dano[i]
        print(f"Vida atual é {hp}")
        qtd_ataque +=1
        

print(f"\nVida final: 0\nataques recebidos: {qtd_ataque}\nStatus: derrotado")


