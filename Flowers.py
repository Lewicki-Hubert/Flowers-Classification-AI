import math


def load_data(filepath):
    dataset = []
    with open(filepath, 'r') as file:
        for line in file:
            # Zamiana przecinków na kropki i rozdzielenie linii
            row = line.replace(',', '.').strip().split()
            # Konwersja atrybutów na float, etykieta pozostaje jako string
            row = [float(attr) if i < len(row) - 1 else attr for i, attr in enumerate(row)]
            dataset.append(row)
    return dataset


def euclidean_distance(row1, row2):
    # Oblicza odległość euklidesową między dwoma wierszami danych.
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return math.sqrt(distance)


def get_neighbors(train, test_row, k):
    distances = []
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = [distances[i][0] for i in range(k)]
    return neighbors


def predict_classification(train, test_row, k):
    neighbors = get_neighbors(train, test_row, k)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)

    # Sprawdź, czy istnieje remis
    max_count = output_values.count(prediction)
    classes_with_max_count = [cls for cls in set(output_values) if output_values.count(cls) == max_count]

    if len(classes_with_max_count) > 1:  # Jeśli istnieje więcej niż jedna klasa z maksymalną liczbą głosów
        # Sortuj sąsiadów według odległości i wybierz klasę pierwszego (najbliższego) sąsiada z tej posortowanej listy
        sorted_neighbors = sorted(neighbors, key=lambda x: x[1])
        prediction = sorted_neighbors[0][-1]

    return prediction


def k_nn_classification(train, test, k):
    correct = 0
    for row in test:
        prediction = predict_classification(train, row, k)
        if prediction == row[-1]:
            correct += 1
    accuracy = correct / float(len(test)) * 100.0
    return correct, accuracy


def user_interface():
    # Wczytywanie danych treningowych
    train_data_path = input("Podaj ścieżkę do pliku z danymi treningowymi: ")
    train = load_data(train_data_path)

    # Określenie liczby atrybutów
    num_attributes = len(train[0]) - 1

    while True:
        # Wczytanie wartości k od użytkownika przy każdej iteracji
        k = int(input("Podaj wartość parametru k: "))

        user_choice = input("Chcesz (1) sklasyfikować zbiór testowy, czy (2) wprowadzić wektor atrybutów? (1/2): ")

        if user_choice == '1':
            test_data_path = input("Podaj ścieżkę do pliku z danymi testowymi: ")
            test = load_data(test_data_path)
            correct, accuracy = k_nn_classification(train, test, k)
            print(f'Liczba prawidłowo zaklasyfikowanych przykładów: {correct}/{len(test)}')
            print(f'Dokładność: {accuracy:.2f}%')
        elif user_choice == '2':
            test_row_input = input(f"Wprowadź wektor {num_attributes} atrybutów oddzielony spacjami (bez etykiety): ")
            test_row = [float(attr) for attr in test_row_input.split()]

            if len(test_row) != num_attributes:
                print(f"Błąd: Należy podać dokładnie {num_attributes} atrybutów.")
                continue

            prediction = predict_classification(train, test_row, k)
            print(f'Przewidziana klasa dla wprowadzonego wektora: {prediction}')
        else:
            print("Niepoprawne polecenie.")

        if input("Czy chcesz kontynuować? (tak/nie): ") != 'tak':
            break


user_interface()
