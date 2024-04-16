##Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor.
def eleicao():
    votacao = 0
    c1=0
    c2=0
    c3=0
    while votacao != 21:
        voto=int(input('Vote no candidato1(1), candidato2(2) ou candidato3(3): '))
        match voto:
            case 1:
                c1=c1+1
            case 2:
                c2=c2+1
            case 3:
                c3=c3+1
            case _:
                print('Inválido')
        votacao= votacao+1

    if c1 > c2 and c1 > c3:
        print(f'Candidato1 ganhou as eleições com {c1} votos, Candidato2 recebeu {c2} votos e Candidato3 recebeu {c3} votos')
    elif c2 > c1 and c2 > c3:
        print(f'Candidato2 ganhou as eleições com {c2} votos, Candidato1 recebeu {c1} votos e Candidato3 recebeu {c3} votos')
    else:
        print(f'Candidato3 ganhou as eleições com {c3} votos, Candidato1 recebeu {c1} votos e Candidato2 recebeu {c2} votos')

eleicao()
