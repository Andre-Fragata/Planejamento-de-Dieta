import csv

def buscar_dados_csv(arquivo_csv, coluna_busca, valor_busca):
    resultados = []
    
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        
        for linha in leitor_csv:
            if linha[coluna_busca] == valor_busca:
                resultados.append(linha)
    
    return resultados

# Exemplo de uso
arquivo_csv = 'alimentos.csv'  # Caminho para o seu arquivo CSV
coluna_busca = 'Descrição dos alimentos'      # Coluna na qual você deseja buscar o valor
valor_busca = 'Mingau tradicional, pó'       # Valor que você está procurando

resultados = buscar_dados_csv(arquivo_csv, coluna_busca, valor_busca)

if resultados:
    print(f'Encontrado {len(resultados)} resultado(s):')
    for resultado in resultados:
        print(resultado)
else:
    print('Nenhum resultado encontrado.')

