import sqlite3

class DietPlanner:
    def __init__(self):
        self.user_data = {}
        self.conn = sqlite3.connect('diet_planner.db')  # Conecta ao banco de dados existente

    def collect_user_data(self):
        # 1. Informações básicas
        self.user_data['idade'] = int(input("Qual é a sua idade? "))
        print("Qual é o seu sexo biológico? ")
        self.user_data['sexo'] = input("Escolha uma opção (M, F): ")
        self.user_data['altura'] = float(input("Qual é a sua altura (em cm)? "))
        self.user_data['peso'] = float(input("Qual é o seu peso atual (em kg)? "))

        # 2. Nível de atividade física
        print("\nComo você descreveria seu nível de atividade física diária?")
        print("a) Sedentário (pouco ou nenhum exercício)")
        print("b) Levemente ativo (exercício leve 1-3 dias/semana)")
        print("c) Moderadamente ativo (exercício moderado 3-5 dias/semana)")
        print("d) Muito ativo (exercício intenso 6-7 dias/semana)")
        print("e) Extremamente ativo (exercício muito intenso diariamente ou trabalho físico)")
        self.user_data['nivel_atividade'] = input("Escolha uma opção (a, b, c, d ou e): ")

        # 3. Objetivos
        print("\nQual é o seu principal objetivo com esta dieta?")
        print("a) Perder peso")
        print("b) Ganhar massa muscular")
        print("c) Manter o peso atual")
        print("d) Melhorar a saúde geral")
        self.user_data['objetivo'] = input("Escolha uma opção (a, b, c ou d): ")

        if self.user_data['objetivo'] in ['a', 'b']:
            self.user_data['meta_peso'] = float(input("Quanto você almeja mudar (em kg)? "))
            self.user_data['prazo'] = int(input("Em quantas semanas você espera atingir esse objetivo? "))
        else:
            self.user_data['meta_peso'] = None
            self.user_data['prazo'] = None

        # 4. Restrições alimentares
        print("\nVocê tem alguma restrição alimentar? ")
        print("a) Intolerância a Lactose")
        print("b) Intolerância a Glúten")
        print("c) Alergia à Proteína do Leite")
        print("d) Não Tenho")
        self.user_data['alergias'] = input("Escolha uma opção (a, b, c ou d): ")

        # Buscando dados de alimentos do banco de dados
        self.get_food_recommendations()

    def get_food_recommendations(self):
        # Consulta os alimentos adequados com base nas preferências e restrições do usuário
        cursor = self.conn.cursor()

        # Exemplo de query básica que pode ser ajustada conforme as colunas da sua tabela 'alimentos'
        query = '''
            SELECT nome, calorias, proteinas, carboidratos, gorduras 
            FROM alimentos 
            WHERE restricoes NOT LIKE ? 
            AND restricoes NOT LIKE ?
        '''
        alergia_lactose = "%lactose%" if self.user_data['alergias'] == "a" else "%%"
        alergia_gluten = "%gluten%" if self.user_data['alergias'] == "b" else "%%"

        cursor.execute(query, (alergia_lactose, alergia_gluten))

        alimentos = cursor.fetchall()

        print("\nAlimentos recomendados:")
        for alimento in alimentos:
            print(f"{alimento[0]}: {alimento[1]} calorias, {alimento[2]}g de proteínas, "
                  f"{alimento[3]}g de carboidratos, {alimento[4]}g de gorduras")

    def display_user_data(self):
        print("\nDados coletados:")
        for key, value in self.user_data.items():
            print(f"{key}: {value}")

# Uso da classe
planner = DietPlanner()
planner.collect_user_data()
planner.display_user_data()

