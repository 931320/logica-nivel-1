# Coletando as notas dos 4 bimestres
bimestres = []

print("Digite as notas do aluno nos 4 bimestres:")

for i in range(1, 5):
    while True:
        try:
            nota = float(input(f"Nota do {i}º bimestre: "))
            if 0 <= nota <= 10:
                bimestres.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
