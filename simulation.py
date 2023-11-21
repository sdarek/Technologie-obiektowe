# simulation.py

from src.models import Person
from src.utils.distance_calculator import calculate_distance
from src.utils.probability_calculator import calculate_infection_probability
from src.visualization.animation import create_animation

# simulation.py

import random


def initialize_population(n, m, initial_infected_percentage):
    population = [[Person(x, y) for x in range(n)] for y in range(m)]

    # Zainfekuj początkową liczbę osobników
    num_infected = int((initial_infected_percentage / 100) * (n * m))
    infected_people = random.sample([person for row in population for person in row], num_infected)

    for person in infected_people:
        person.infect(symptomatic=True)  # Możesz dostosować to zależnie od modelu

    return population


def run_simulation(population, simulation_time):
    for _ in range(simulation_time):
        for row in population:
            for person in row:
                if person.is_infected():
                    # Osoba jest zakażona, sprawdź czy zainfekuje innych
                    for other_row in population:
                        for other_person in other_row:
                            if person != other_person and not other_person.is_immune():
                                distance = calculate_distance(person, other_person)
                                if distance <= 2:  # Odległość zakażenia
                                    infection_probability = calculate_infection_probability(person.is_symptomatic())
                                    if random.random() < infection_probability:
                                        other_person.infect(symptomatic=True)

                # Przemieszczanie się osobników (możesz dostosować tę część do swojego modelu)
                direction = random.uniform(0, 2 * math.pi)
                speed = random.uniform(0, 2.5)
                person.move(direction, speed)

        # Aktualizacja stanu populacji (możesz dodać dodatkowe kroki)
        for row in population:
            for person in row:
                person.recover()

        # Wyświetlanie informacji o stanie symulacji
        print(f"Step: {_ + 1}")
        print("Infected:", sum(person.is_infected() for row in population for person in row))
        print("Immune:", sum(person.is_immune() for row in population for person in row))
        print("--------------------")


def main():
    # Parametry symulacji
    n = 50  # liczba wierszy
    m = 50  # liczba kolumn
    initial_infected_percentage = 10  # procent zakażonych na początku
    simulation_time = 100  # czas trwania symulacji (liczba kroków czasowych)

    # Inicjalizacja populacji
    population = initialize_population(n, m, initial_infected_percentage)

    # Uruchomienie symulacji
    run_simulation(population, simulation_time)

    # Wizualizacja wyników
    create_animation(population, n, m, simulation_time)

if __name__ == "__main__":
    main()
