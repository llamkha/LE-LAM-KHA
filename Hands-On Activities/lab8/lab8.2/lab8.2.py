import numpy as np
import random

# Define animal parameters based on table
species_params = {
    'Tiger': {'food': ['Elephant', 'Jaguar', 'Penguin'], 'food_freq': (20, 30), 'food_energy': 30, 'lambda': 1/75, 'new_energy': 15, 'life_expectancy': 300, 'initial_count': 5},
    'Elephant': {'food': ['Grass'], 'food_freq': (8, 15), 'food_energy': 4, 'lambda': 1/200, 'new_energy': 7, 'life_expectancy': 500, 'initial_count': 8},
    'Jaguar': {'food': ['Elephant', 'Tiger', 'Penguin'], 'food_freq': (35, 55), 'food_energy': 20, 'lambda': 1/80, 'new_energy': 10, 'life_expectancy': 350, 'initial_count': 5},
    'Penguin': {'food': ['Cephalopod'], 'food_freq': (4, 15), 'food_energy': 5, 'lambda': 1/80, 'new_energy': 10, 'life_expectancy': 90, 'initial_count': 12}
}

# Initialize populations of Grass and Cephalopods
grass_population = species_params['Elephant']['initial_count'] * 3
cephalopod_population = species_params['Penguin']['initial_count'] * 5

# Define simulation parameters
max_simulation_time = 1000
num_simulations = 1000

# Initialize statistics storage
extinction_counts = {species: 0 for species in species_params.keys()}
average_lifetimes = {species: [] for species in species_params.keys()}
# ... (other stats tracking variables)

# Simulation loop
for sim in range(num_simulations):
    # Initialize populations and counters for this simulation
    populations = {species: params['initial_count'] for species, params in species_params.items()}
    time = 0

    while time < max_simulation_time:
        # Handle events for feeding, births, and deaths
        # Update populations, calculate statistics

        # Check if any species extinct and update time and counters if so

        time += 1

# After simulation, calculate and print statistics
print("Average simulation time:", np.mean([...]))
print("Extinction counts per species:", extinction_counts)
# Other stats output

