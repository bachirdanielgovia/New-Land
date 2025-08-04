import random
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

def generate_new_land_map(width=20, height=10):
    # Define terrain types with symbols and colors
    terrains = {
        'forest': (Fore.GREEN + '🌲' + Style.RESET_ALL, 0.4),
        'mountain': (Fore.LIGHTBLACK_EX + '🏔️' + Style.RESET_ALL, 0.2),
        'river': (Fore.BLUE + '🌊' + Style.RESET_ALL, 0.2),
        'plain': (Fore.YELLOW + '🌾' + Style.RESET_ALL, 0.3)
    }

    # Create the map
    print("\n=== Welcome to New Land ===")
    for _ in range(height):
        row = ''
        for _ in range(width):
            # Randomly choose terrain based on weights
            terrain = random.choices(
                list(terrains.keys()),
                weights=[t[1] for t in terrains.values()],
                k=1
            )[0]
            row += terrains[terrain][0]
        print(row)
    print("=== Explore your New Land! ===\n")

if __name__ == "__main__":
    generate_new_land_map()
