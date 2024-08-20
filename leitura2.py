import csv

def buscar_alimentos_csv(arquivo_csv, criterios_busca, intervalo_calorias=None, colunas_desejadas=None):
    resultados = []
    
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        
        for linha in leitor_csv:
            corresponde = True
            for coluna, valor in criterios_busca.items():
                if coluna != 'Energia (kcal)':
                    if linha[coluna].lower() != valor.lower():
                        corresponde = False
                        break
            
            if corresponde and intervalo_calorias:
                calorias = float(linha['Energia (kcal)'])
                if not (intervalo_calorias[0] <= calorias <= intervalo_calorias[1]):
                    corresponde = False
            
            if corresponde:
                # Incluir apenas as colunas desejadas
                if colunas_desejadas:
                    resultado_filtrado = {k: linha[k] for k in colunas_desejadas if k in linha}
                    resultados.append(resultado_filtrado)
                else:
                    resultados.append(linha)
    
    return resultados

# Exemplo de uso
arquivo_csv = 'alimentos.csv'  # Caminho para o arquivo CSV de alimentos
criterios_busca = {
    'Categoria do alimento': 'Cereais e derivados',
}
intervalo_calorias = (100, 130)  # Intervalo de calorias desejado
colunas_desejadas = ['Descrição dos alimentos', 'Energia (kcal)', 'Proteína (g)', 'Lipídeos (g)']  # Colunas que você quer incluir

resultados = buscar_alimentos_csv(arquivo_csv, criterios_busca, intervalo_calorias, colunas_desejadas)

if resultados:
    print(f'Encontrado {len(resultados)} alimento(s):')
    for resultado in resultados:
        print(resultado)
else:
    print('Nenhum alimento encontrado.')
