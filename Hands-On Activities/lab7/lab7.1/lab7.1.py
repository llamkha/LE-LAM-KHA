import random
import time

class Soldier:
    def __init__(self, attack_speed, hp, attack_damage):
        self.attack_speed = attack_speed  # time between attacks in seconds
        self.hp = hp                      # soldier's health points
        self.attack_damage = attack_damage  # damage dealt to Godzilla

    def attack(self):
        if self.hp > 0:
            return self.attack_damage
        return 0

def godzilla_attack(soldiers):
    for soldier in soldiers:
        soldier.hp -= 3  # Godzilla deals 3 damage to each soldier
        if soldier.hp < 0:
            soldier.hp = 0  # Ensure HP doesn't go negative

def simulate_battle(time_limit, new_soldier_interval):
    soldiers = []
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < time_limit:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Create a new soldier every `new_soldier_interval` seconds
        if elapsed_time % new_soldier_interval < 1:  # To avoid creating multiple soldiers in one second
            attack_speed = random.randint(4, 19)
            hp = 10  # Initial HP for soldiers
            attack_damage = random.randint(1, 5)  # Random attack damage
            soldiers.append(Soldier(attack_speed, hp, attack_damage))
            print(f"New soldier created: Attack Speed = {attack_speed}s, HP = {hp}, Damage = {attack_damage}")

        # Godzilla attacks every 8 seconds
        if elapsed_time % 8 < 1:  # Godzilla attacks every 8 seconds
            godzilla_attack(soldiers)
            print("Godzilla attacks! Remaining soldiers' HP:")
            for soldier in soldiers:
                print(f"Soldier HP: {soldier.hp}")

        # Soldiers attack Godzilla
        for soldier in soldiers:
            if soldier.hp > 0:
                damage_to_godzilla = soldier.attack()
                print(f"Soldier attacks Godzilla for {damage_to_godzilla} damage!")

                # Godzilla retaliates
                if damage_to_godzilla > 0:
                    retaliation_damage = damage_to_godzilla // 4  # Godzilla retaliates with 1/4 of soldier's attack
                    soldier.hp -= retaliation_damage
                    print(f"Godzilla retaliates! Soldier takes {retaliation_damage} damage. Remaining HP: {soldier.hp}")

        time.sleep(1)  # Sleep for 1 second to simulate the passage of time

    print("Battle simulation ended.")

# Parameters
time_limit = 60  # Run simulation for 60 seconds
new_soldier_interval = 10  # New soldier every 10 seconds

simulate_battle(time_limit, new_soldier_interval)

