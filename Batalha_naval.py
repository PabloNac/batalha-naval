from random import randint

mapa = [['~','~','~'], ['~','~','~'], ['~','~','~']]

def reset():
    global mapa
    mapa = [['~','~','~'], ['~','~','~'], ['~','~','~']]
    

def GerarBarcos():
    barco1 = f'{randint(0,2)}.{randint(0,2)}'
    barco2 = f'{randint(0,2)}.{randint(0,2)}'
    while True:
        if barco1 == barco2:
            barco2 = f'{randint(0,2)}.{randint(0,2)}'
        else:
            return {'barco 1':barco1,'barco 2':barco2}
        
def deploy():
    for i in player.values():
        aux = i.split('.')
        x = int(aux[0])
        y = int(aux[1])
        mapa[x].insert(y,'N')
        mapa[x].pop(y+1)

def DestruiBarco(x,y,alvo):
    for m in alvo.items():
        if f'{x}.{y}' in m:
            d = m[0]
    alvo.pop(d)
    

def MapaAtual():
    print(f'   1 2 3')
    
    for i in range(0,3):
        print(f'{i+1} ', end='|')
        
        for j in range(0,3):
            print(f'{mapa[i][j]}',end='|')
        print('')
        
def Atacar(x,y,atacante):
    global mapa
    x -= 1
    y -= 1
    
    for i in range(0,3):
        for j in range(0,3):
            
            if f'{x}.{y}' == f'{i}.{j}':
                
                if atacante == 'jogador':
                    if f'{x}.{y}' in enemy.values():
                        if mapa[x][y] != 'N':
                            mapa[x].insert(y,'O')
                            mapa[x].pop(y+1)
                        
                        DestruiBarco(x,y,enemy)
                        
                        print('Você acertou!!')
                    else:
                        if mapa[x][y] != 'N':
                            mapa[x].insert(y,'X')
                            mapa[x].pop(y+1)
                            
                        print('Você errou!')
                else:
                    if f'{x}.{y}' in player.values():
                        mapa[x].insert(y,'X')
                        mapa[x].pop(y+1)
                        print('Você foi atingido')
                        
                        DestruiBarco(x,y,player)
                    else:
                        print('Seu inimigo errou o tiro.')
                

def play():
    global player, enemy
    enemy = GerarBarcos()
    player = GerarBarcos()
    deploy()
    while True:
        print('=='*30)
        print(enemy)
        print(player)
        MapaAtual()

        if not enemy:
            print('Você venceu!')
            menu()
        if not player:
            print('Você perdeu!')
            menu()
        
        try:
            x = int(input('Digite a fileira: '))
            y = int(input('Digite a coluna: '))
        except ValueError:
            print('Digite um valor valido')
        
        
        Atacar(x,y,'jogador')
        Atacar(randint(1,3), randint(1,3),'bot')
        print('=='*30)
        

        
    

def menu():
    print('='*20)
    print('Seja bem-vindo!')
    print('[1] Iniciar')
    print('[2] Opções')
    print('[3] Sair')
    
    opção = int(input('Escolha uma opção: '))
    print('='*20)    
    if opção == 1:
        reset()
        play()
    elif opção == 2:
        pass
    else:
        quit()

menu()

