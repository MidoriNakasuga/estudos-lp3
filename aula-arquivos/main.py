# abrir arquivo
arquivo = open("dados.txt")
print(arquivo)
#conteudo = arquivo.read()
# read devolve o arquivo 
# BANANA VERDE
# UVA VERDE
# BANANA VERDE
# UVA VERDE
#conteudo = arquivo.readlines()
# readlines devolve como uma lista 
# ['BANANA VERDE\n', 'UVA VERDE\n']
# ['BANANA VERDE\n', 'UVA VERDE\n']
# print (conteudo)
# print (conteudo)

linhas=[]
for linha in arquivo:
    linhas.append(linha.strip())
# strip tira quebra de linha (\n) e espaços
# strip().lower() faz o strip e deixa tudo minúsculo
print(linhas)

arquivo.close()


# bloco with
# cria contexto de alguma coisa, quando desvia do contexto, 
# o caminho fecha, sem precisar de close

with open("dados.txt", "r") as arquivo2:
    conteudo = arquivo2.read()
    print(conteudo)

# escrever no arquivo
# w - substitui todo o conteúdo
#with open("dados.txt", "w") as arquivo3:
#    arquivo3.write("FRUTASSS")

# a - adiciona nova linha (a = append)
with open("dados.txt", "a") as arquivo4:
    arquivo4.write("\nmelão")

# ler o arquivo produtos csv e 
# carregar em memória uma lista 
# na qual cada produto é um dict

def linha_para_produto(linha):
    dados = (linha.strip().split(","))
    return {
            "nome": dados[0],
            "descricao":dados[1],
            "preco":float(dados[2]),
            "imagem":dados[3]
        }

def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produto(linha)
            produtos.append(produto)

print(obter_produtos())

def salvar_produto(nome, descricao, preco, imagem):
    texto = f"{nome}, {descricao}, {preco}, {imagem}"
    with open("produtos.csv", "a") as arquivo_produtos:
        arquivo_produtos.write(texto)
salvar_produto("Celular", "Tira foto", "1500", "celular.jpg")
salvar_produto("Tablet", "Tela grande", "2500", "tablet.jpg")
