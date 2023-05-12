import csv

animais_sorted = sorted(["gato", "cachorro", "bode", "vaca", "boi", "carneiro", "cobra", "leão", "onça", "girafa", "urso", "lobo", "tigre", "peixe", "baleia", "macaco", "elefante", "lagarto", "jacaré", "sapo"])

# Para imprimir no terminal:
[print(animal) for animal in animais_sorted]

# Para gravar no arquivo csv, linha a linha:
with open('./dados-em-massa/animais.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    [writer.writerow([animal]) for animal in animais_sorted]