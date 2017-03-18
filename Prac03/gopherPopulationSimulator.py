"""
Program simulates the gopher population over a ten year period based on:
    - initial population of 1,000
    - births is a random number between 10 - 20%
    - deaths is a random number between 5 - 25%
"""
import random


STARING_POPULATION = 1000


def calc_yearly_change(population, births, deaths):
    current_population = population + births - deaths
    return current_population


def main():
    print("Welcome to the Gopher Population Simulator!\nStarting population is: 1000")
    population = STARING_POPULATION
    count = 0
    for i in range(10):
        birth_rate = random.randint(10, 20)
        death_rate = random.randint(5, 25)
        births = int(birth_rate * STARING_POPULATION / 100)
        deaths = int(death_rate * STARING_POPULATION / 100)
        current_population = int(calc_yearly_change(population, births, deaths))
        population = current_population
        count += 1
        print("Year {}\n{}\n{} gophers were born. {} died.\nPopulation: {}\n".format(count, "*****", births, deaths,
              current_population))

main()
