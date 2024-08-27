class DietPlanner:
    def __init__(self):
        self.user_data = {}

    def collect_user_data(self):
        # 1. Informações básicas
        self.user_data['idade'] = int(input("Qual é a sua idade? "))
        print("Qual é o seu sexo biológico? ")
        self.user_data['sexo'] = input("Escolha uma opção (M, F) ")
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

        # 4. Restrições alimentares
        print("\nVocê tem alguma restrição alimentar ? ")
        print("a) Intolerância a Lactose")
        print("b) Intolerância a Glúten")
        print("c) Alergia a Proteina do Leite")
        print("d) Não Tenho")
        self.user_data['alergias'] = input("Escolha uma opção (a, b, c ou d)")
        #self.user_data['dieta_especifica'] = input("Você segue alguma dieta específica (ex: vegetariana, vegana, sem glúten)? Qual? ")
        
        #self.user_data['restricoes_culturais'] = input("Há algum alimento que você não consome por razões religiosas ou culturais? ")

        # 5. Preferências alimentares
        #self.user_data['alimentos_favoritos'] = input("Quais são seus alimentos favoritos? ")
        #self.user_data['alimentos_indesejados'] = input("Há algum alimento que você absolutamente não gosta ou não comeria? ")
        #self.user_data['preferencia_refeicoes'] = input("Você prefere refeições mais elaboradas ou mais simples e rápidas? ")

        # 6. Histórico médico
        #self.user_data['condicoes_medicas'] = input("Você tem alguma condição médica que afeta sua dieta (ex: diabetes, hipertensão, colesterol alto)? ")
        #self.user_data['medicamentos'] = input("Você toma algum medicamento que possa afetar seu metabolismo ou necessidades nutricionais? ")

        # 7. Hábitos alimentares atuais
        #self.user_data['num_refeicoes'] = int(input("Quantas refeições você costuma fazer por dia? "))
        #self.user_data['lanches'] = input("Você costuma fazer lanches entre as refeições principais? (Sim/Não) ")
        #self.user_data['refeicoes_fora'] = input("Com que frequência você come fora de casa? ")

        # 8. Estilo de vida
        #self.user_data['rotina_diaria'] = input("Descreva brevemente sua rotina diária típica: ")
        #self.user_data['horario_regular'] = input("Você tem um horário regular para as refeições? (Sim/Não) ")
        #self.user_data['pula_refeicoes'] = input("Você costuma pular refeições? Se sim, qual e por quê? ")

        # 9. Conhecimento nutricional
        #self.user_data['dieta_anterior'] = input("Você já seguiu alguma dieta antes? Se sim, qual foi sua experiência? ")
        #self.user_data['cozinha'] = input("Você sabe cozinhar? Com que frequência cozinha suas próprias refeições? ")

        # 10. Metas adicionais
        #self.user_data['metas_adicionais'] = input("Além do seu objetivo principal, há algum aspecto específico da sua saúde ou forma física que você gostaria de melhorar? ")

    def display_user_data(self):
        print("\nDados coletados:")
        for key, value in self.user_data.items():
            print(f"{key}: {value}")

# Uso da classe
planner = DietPlanner()
planner.collect_user_data()
planner.display_user_data()
