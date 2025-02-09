import pandas as pd
import random
from datetime import datetime, timedelta

# Configurar semente para reprodutibilidade
random.seed(42)

# 1. Listas de dados fictícios
nomes_m = ['João', 'Pedro', 'Lucas', 'Carlos', 'Gabriel', 'Fernando', 'Rafael', 'Marcos', 'Antônio', 'Daniel']
nomes_f = ['Maria', 'Ana', 'Juliana', 'Patrícia', 'Camila', 'Amanda', 'Fernanda', 'Beatriz', 'Letícia', 'Isabela']
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Costa', 'Rodrigues', 'Almeida', 'Carvalho', 'Gomes']

escolas = [
    'U E de Ensino Médio Vila Maria',
    'Ceep Em Saude Mons José Luis Barbosa Cortez',
    'Ceep José Pacifico de Moura Neto',
    'Ceep Paulo Ferraz',
    'Ceep Pref João Mendes Olimpio de Melo',
    'Ceep Professor Ruy Leite Berger Filho'
]

escolaridades = [
    'Ensino Médio Completo',
    'Ensino Médio Incompleto',
]

cursos = [
    'Engenharia de Prompts para IA Generativa',
    'IA Generativa de Imagens',
    'IA Generativa de Videos',
    'Criação de conteúdo com IA',
    'IA para SEO e Otimização de conteúdos',
    'Lógica de programação com Python',
    'Manipulação de dados com Python',
    'Introdução a IA com scikit-learn',
    'Introdução a visão computacional com OpenCV'
]
prof_fabrio = [ 'Engenharia de Prompts para IA Generativa','IA Generativa de Imagens','IA Generativa de Videos']
prof_mario = [ 'Criação de conteúdo com IA', 'IA para SEO e Otimização de conteúdos']
prof_carlos = ['Lógica de programação com Python','Manipulação de dados com Python','Introdução a IA com scikit-learn','Introdução a visão computacional com OpenCV']

# 2. Função para gerar dados aleatórios
def gerar_aluno(id):
    sexo = random.choice(['Masculino', 'Feminino'])
    nome = (
        random.choice(nomes_m if sexo == 'Masculino' else nomes_f) + 
        ' ' + random.choice(sobrenomes) + 
        ' ' + random.choice(sobrenomes)
    )
    
    idade = random.randint(15, 21)
    escola = random.choice(escolas)
    escolaridade = random.choice(escolaridades)
    curso = random.choice(cursos)
    
    # Gerar data de matrícula aleatória entre 01/01/2023 e 01/02/2025
    data_inicio = datetime(2023, 1, 1)
    data_fim = datetime(2025, 2, 1)
    delta = data_fim - data_inicio
    data_matricula = data_inicio + timedelta(days=random.randint(0, delta.days))
    
    concluiu = random.choices([True, False], weights=[0.7, 0.3])[0]
    respostas = random.randint(0, 100) if not concluiu else random.randint(70, 100)
    avaliacao = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.1, 0.15, 0.3, 0.4])[0]
    if curso in prof_fabrio:
        professor = "Fábio Andrade"
    elif curso in prof_mario:
        professor = "Mario Santos"
    else:
        professor = "Carlos Cunha"

    return {
        'nome_aluno': nome,
        'sexo_aluno': sexo,
        'idade_aluno': idade,
        'escola_aluno': escola,
        'escolaridade_aluno': escolaridade,
        'curso': curso,
        'professor': professor, 
        'data_matricula': data_matricula.strftime('%d/%m/%Y'),
        'concluiu_curso': concluiu,
        'respostas_corretas': respostas,
        'avaliacao_curso': avaliacao
    }


dados = [gerar_aluno(i) for i in range(10000)]
df = pd.DataFrame(dados)

# 4. Salvar em CSV
df.to_csv('alunos_cursos.csv', index=False, encoding='utf-8-sig')
print("Arquivo CSV gerado com sucesso!")