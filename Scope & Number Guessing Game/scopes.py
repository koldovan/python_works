#Local Scope
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
# print(potion_strengths) - will not work

#Global Scope
player_health = 10

def drink_potion():
  potion_strength = 2
  print(potion_strength)

#There is no block scope
def create_enemy():
  game_level = 3
  enemies = ["Skeleton", "Zombie", "Alien"]

  if game_level < 5:
      new_enemy = enemies[0]
      return new_enemy

created_enemy = create_enemy()
print(created_enemy)

# How to modify variables via global scope?
enemies = 1

# bad idea to use frequently, but it's possible
def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

# better way to write the function
def increase_enemies_updated():
  return enemies + 1

# Global constants. Constants are uppercased variables which can not be modified
import decimal

URL = "https://google.com"
TWITTER_HANDLE = "koldo_van"
PI = decimal.Decimal(3.141592653589793238462643383279502884197)

print(f"{PI}\n{type(PI)}")

