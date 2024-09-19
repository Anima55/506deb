import random

# Функція для підкидання монети
def flip_coin():
    return random.choice(["Орел", "Решка"])

# Початок гри
print("Натисни Enter, щоб підкинути монету або введи 'q' для виходу.")

while True:
    # Очікуємо на дію гравця
    player_input = input("Підкинути монету? ")
    
    if player_input.lower() == 'q':
        print("Гру завершено.")
        break
    else:
        # Виводимо результат підкидання
        result = flip_coin()
        print(f"Випало: {result}")
        