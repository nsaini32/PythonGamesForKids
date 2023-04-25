import random

# Define the game settings
ALIEN_HEALTH = 50
HUMAN_HEALTH = 50
ALIEN_ATTACK_DAMAGE = 10
HUMAN_ATTACK_DAMAGE = 10

# Define the game loop
while ALIEN_HEALTH > 0 and HUMAN_HEALTH > 0:
    # Alien attacks human
    human_damage = random.randint(1, ALIEN_ATTACK_DAMAGE)
    HUMAN_HEALTH -= human_damage
    print("The alien attacks the human and deals", human_damage, "damage. Human health:", HUMAN_HEALTH)
    # Check if human is still alive
    if HUMAN_HEALTH <= 0:
        print("The human has been defeated. Game over.")
        break
    # Human attacks alien
    alien_damage = random.randint(1, HUMAN_ATTACK_DAMAGE)
    ALIEN_HEALTH -= alien_damage
    print("The human attacks the alien and deals", alien_damage, "damage. Alien health:", ALIEN_HEALTH)
    # Check if alien is still alive
    if ALIEN_HEALTH <= 0:
        print("The alien has been defeated. You win!")
        break
