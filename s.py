import pandas as pd 

df = pd.read_csv("student.csv")

renomear = {
    "Hours Studied":"horas_estudadas",
    "Previous Scores":"pontuacao_anterior",
    "Extracurricular Activities":"atividades_extracurricular",
    "Sleep Hours":"horas_dormida",
    "Performance Index":"desempenho",
    "Sample Question Papers Practiced":"provas_praticadas"
}

df.rename(columns=renomear, inplace=True)


# Medias de horas estudadas 
media_horas = df["horas_estudadas"].mean()
# Menor hora estudada 
menor_hora = df["horas_estudadas"].min()
# Maior Hora Estudada
maior_hora = df["horas_estudadas"].max()
# Desvio Padrao ( maioria em media )
padrao_hora = df["horas_estudadas"].std()



print(f"Medias de Horas Estudadas: {media_horas}")
print(f"Maior Quantidade de Horas Estudadas: {maior_hora}")
print(f"Menor Quantidade de Horas Estudadas: {menor_hora}")
print(f"A Maioria estuda em media: {padrao_hora}")
