import random
import time

class Soldier:
    def __init__(self, attack_speed, hp, attack_damage):
        self.attack_speed = attack_speed  # Time between attacks in seconds
        self.hp = hp                      # Soldier's health points
        self.attack_damage = attack_damage  # Damage dealt to Mega-Godzilla
        self.can_attack = True  # Flag to check if the soldier can attack

    def attack(self):
        if self.hp > 0 and self.can_attack:
            return self.attack_damage
        return 0

class MegaGodzilla:
    def __init__(self):
        self.hp = 100  # Mega-Godzilla's health points

    def normal_attack(self, soldiers):
        for soldier in soldiers:
            soldier.hp -= 3  # Damage to each soldier from normal attack
            if soldier.hp < 0:
                soldier.hp = 0  # Ensure HP doesn't go negative

    def ultimate_attack(self, soldiers):
        for soldier in soldiers:
            soldier.hp -= 6  # Damage to each soldier from ultimate attack
            soldier.can_attack = False  # Stun the soldier for 10 seconds
            if soldier.hp < 0:
                soldier.hp = 0  # Ensure HP doesn't go negative

def simulate_battle(time_limit, new_soldier_interval):
    soldiers = []
    megagodzilla = MegaGodzilla()
    start_time = time.time()
    elapsed_time = 0
    next_soldier_time = 0

    while elapsed_time < time_limit:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # Create a new soldier every `new_soldier_interval` seconds
        if elapsed_time >= next_soldier_time:
            attack_speed = random.randint(4, 19)
            hp = 10  # Initial HP for soldiers
            attack_damage = random.randint(1, 5)  # Random attack damage
            soldiers.append(Soldier(attack_speed, hp, attack_damage))
            print(f"New soldier created: Attack Speed = {attack_speed}s, HP = {hp}, Damage = {attack_damage}")
            next_soldier_time = elapsed_time + new_soldier_interval

        # Mega-Godzilla attacks every N seconds (3 to 6 seconds)
        n = random.randint(3, 6)
        time.sleep(n)  # Wait for N seconds before Mega-Godzilla's next action
        print(f"Mega-Godzilla attacks after {n} seconds!")

        # Normal attack
        megagodzilla.normal_attack(soldiers)
        print("Mega-Godzilla normal attack! Remaining soldiers' HP:")
        for soldier in soldiers:
            print(f"Soldier HP: {soldier.hp}")

        # Soldiers attack Mega-Godzilla
        for soldier in soldiers:
            if soldier.hp > 0 and soldier.can_attack:
                damage_to_megagodzilla = soldier.attack()
                print(f"Soldier attacks Mega-Godzilla for {damage_to_megagodzilla} damage!")

                # Mega-Godzilla retaliates
                if damage_to_megagodzilla > 0:
                    retaliation_damage = damage_to_megagodzilla // 4  # Mega-Godzilla retaliates with 1/4 of soldier's attack
                    soldier.hp -= retaliation_damage
                    print(f"Mega-Godzilla retaliates! Soldier takes {retaliation_damage} damage. Remaining HP: {soldier.hp}")

                # Random chance to perform Ultimate Mega-Godzilla Super Attack
                if random.random() < 0.1:  # 10% chance for ultimate attack
                    print("Mega-Godzilla performs Ultimate Super Attack!")
                    megagodzilla.ultimate_attack(soldiers)
                    print("Soldiers stunned for 10 seconds!")
                    time.sleep(10)  # Stun soldiers for 10 seconds
                    for s in soldiers:
                        s.can_attack = True  # Soldiers can attack again after stun

        # Sleep for a moment to simulate time passing
        time.sleep(1)

    print("Battle simulation ended.")

# Parameters
time_limit = 60  # Run simulation for 60 seconds
new_soldier_interval = 10  # New soldier every 10 seconds

simulate_battle(time_limit, new_soldier_interval)
