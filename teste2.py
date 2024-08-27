import sqlite3
import random

class DietPlanner:
    def __init__(self):
        self.user_data = {}
        self.conn = sqlite3.connect('TACO.db')

    def collect_user_data(self):
        print("Bem-vindo ao Planejador de Dieta! Vamos coletar algumas informações sobre você.")
        self.user_data['idade'] = int(input("Qual é a sua idade? "))
        self.user_data['sexo'] = input("Qual é o seu sexo biológico? (M/F): ").upper()
        self.user_data['altura'] = float(input("Qual é a sua altura (em cm)? "))
        self.user_data['peso'] = float(input("Qual é o seu peso atual (em kg)? "))

        print("\nComo você descreveria seu nível de atividade física diária?")
        print("a) Sedentário (pouco ou nenhum exercício)")
        print("b) Levemente ativo (exercício leve 1-3 dias/semana)")
        print("c) Moderadamente ativo (exercício moderado 3-5 dias/semana)")
        print("d) Muito ativo (exercício intenso 6-7 dias/semana)")
        print("e) Extremamente ativo (exercício muito intenso diariamente ou trabalho físico)")
        self.user_data['nivel_atividade'] = input("Escolha uma opção (a, b, c, d ou e): ")

        print("\nQual é o seu principal objetivo com esta dieta?")
        print("a) Perder peso")
        print("b) Ganhar massa muscular")
        print("c) Manter o peso atual")
        print("d) Melhorar a saúde geral")
        self.user_data['objetivo'] = input("Escolha uma opção (a, b, c ou d): ")

        if self.user_data['objetivo'] in ['a', 'b']:
            self.user_data['meta_peso'] = float(input("Quanto você almeja mudar (em kg)? "))
            self.user_data['prazo'] = int(input("Em quantas semanas você espera atingir esse objetivo? "))

    def calculate_bmr(self):
        if self.user_data['sexo'] == 'M':
            bmr = 88.362 + (13.397 * self.user_data['peso']) + (4.799 * self.user_data['altura']) - (5.677 * self.user_data['idade'])
        else:
            bmr = 447.593 + (9.247 * self.user_data['peso']) + (3.098 * self.user_data['altura']) - (4.330 * self.user_data['idade'])

        activity_factors = {'a': 1.2, 'b': 1.375, 'c': 1.55, 'd': 1.725, 'e': 1.9}
        tdee = bmr * activity_factors[self.user_data['nivel_atividade']]

        if self.user_data['objetivo'] == 'a':
            return tdee - 500  # Déficit calórico para perda de peso
        elif self.user_data['objetivo'] == 'b':
            return tdee + 500  # Superávit calórico para ganho de massa
        else:
            return tdee

    def get_food_recommendations(self):
        cursor = self.conn.cursor()
        query = '''
            SELECT "Número do Alimento", "Categoria do alimento", "Descrição dos alimentos",
                   "Energia (kcal)", "Proteína (g)", "Lipídeos (g)", "Carboidrato (g)",
                   "Fibra Alimentar (g)"
            FROM alimentos
            WHERE "Categoria do alimento" LIKE ?
        '''
        
        categorias = []
        if self.user_data['objetivo'] == 'a':  # Perder peso
            categorias = ["%Hortaliças%", "%Frutas%", "%Cereais%"]
        elif self.user_data['objetivo'] == 'b':  # Ganhar massa muscular
            categorias = ["%Carnes e ovos%", "%Leite e derivados%", "%Cereais%"]
        else:
            categorias = ["%"]  # Todas as categorias

        alimentos = []
        for categoria in categorias:
            cursor.execute(query, (categoria,))
            alimentos.extend(cursor.fetchall())

        return alimentos

    def generate_meal_plan(self):
        alimentos = self.get_food_recommendations()
        calorias_diarias = self.calculate_bmr()
        refeicoes = {
            'cafe_da_manha': [],
            'almoco': [],
            'jantar': [],
            'lanches': []
        }
        
        calorias_por_refeicao = {
            'cafe_da_manha': calorias_diarias * 0.25,
            'almoco': calorias_diarias * 0.35,
            'jantar': calorias_diarias * 0.30,
            'lanches': calorias_diarias * 0.10
        }

        for refeicao, calorias_alvo in calorias_por_refeicao.items():
            calorias_atuais = 0
            while calorias_atuais < calorias_alvo and alimentos:
                alimento = random.choice(alimentos)
                if calorias_atuais + float(alimento[3]) <= calorias_alvo:
                    refeicoes[refeicao].append(alimento)
                    calorias_atuais += float(alimento[3])
                    alimentos.remove(alimento)

        return refeicoes

    def display_meal_plan(self):
        plano = self.generate_meal_plan()
        print("\nSeu plano de refeições personalizado:")
        for refeicao, alimentos in plano.items():
            print(f"\n{refeicao.capitalize()}:")
            for alimento in alimentos:
                print(f"- {alimento[2]}: {alimento[3]} kcal, {alimento[4]}g de proteínas, "
                      f"{alimento[5]}g de lipídeos, {alimento[6]}g de carboidratos, "
                      f"{alimento[7]}g de fibras")

    def run_chatbot(self):
        self.collect_user_data()
        while True:
            print("\nO que você gostaria de fazer?")
            print("1. Ver meu plano de refeições")
            print("2. Recalcular meu plano")
            print("3. Ver minhas informações")
            print("4. Sair")
            choice = input("Escolha uma opção (1-4): ")

            if choice == '1':
                self.display_meal_plan()
            elif choice == '2':
                print("Recalculando seu plano de refeições...")
                self.display_meal_plan()
            elif choice == '3':
                print("\nSuas informações:")
                for key, value in self.user_data.items():
                    print(f"{key}: {value}")
            elif choice == '4':
                print("Obrigado por usar o Planejador de Dieta. Até logo!")
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

# Uso da classe
if __name__ == "__main__":
    planner = DietPlanner()
    planner.run_chatbot()
