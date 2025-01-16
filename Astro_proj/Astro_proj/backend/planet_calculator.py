import requests
import pandas as pd

class PlanetCalculator:
    def __init__(self):
        self.habitability_counts = {
            'habitable': 0,
            'partially_habitable': 0,
            'potentially_habitable': 0,
            'previously_habitable': 0,
            'non_habitable': 0,
            'theoretical': 0
        }
        self.total_planets = 0
        self.planets = []

    def fetch_planet_data(self):
        url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['bodies']
        else:
            return None

    # ... (rest of your class code)

    import requests
import pandas as pd

class PlanetCalculator:
    def __init__(self):
        self.habitability_counts = {
            'habitable': 0,
            'partially_habitable': 0,
            'potentially_habitable': 0,
            'previously_habitable': 0,
            'non_habitable': 0,
            'theoretical': 0
        }
        self.total_planets = 0
        self.planets = []

    def fetch_planet_data(self):
        url = "https://api.le-systeme-solaire.net/rest/bodies/"  # Example API for solar system bodies
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['bodies']
        else:
            return None

    def classify_habitability(self, planet):
        # Simulated criteria for habitability categories
        if planet['isPlanet']:
            if planet['discoveredBy'] and planet['moons'] and 'name' in planet['moons'][0] and 'water' in planet['moons'][0]['name'].lower():
                return 'habitable'
            elif planet['moons'] and len(planet['moons']) > 2:
                return 'partially_habitable'
            elif 'water' in planet['englishName'].lower():
                return 'potentially_habitable'
            elif planet['discoveredBy'] and 'evo' in planet['discoveredBy'].lower():
                return 'previously_habitable'
        return 'non_habitable'

    def add_planet(self, name, habitability, theoretical=False):
        self.planets.append({'name': name, 'habitability': habitability, 'theoretical': theoretical})
        self.habitability_counts[habitability] += 1
        if theoretical:
            self.habitability_counts['theoretical'] += 1
        self.total_planets += 1

    def delete_theoretical_planet(self, name):
        for planet in self.planets:
            if planet['name'].lower() == name.lower() and planet['theoretical']:
                self.habitability_counts[planet['habitability']] -= 1
                self.habitability_counts['theoretical'] -= 1
                self.planets.remove(planet)
                self.total_planets -= 1
                return f"\n---\n**Result**: Theoretical planet '{name}' has been deleted.\n---"
        return f"\n---\n**Result**: Theoretical planet '{name}' not found.\n---"

    def delete_manual_planet(self, name):
        for planet in self.planets:
            if planet['name'].lower() == name.lower() and not planet['theoretical']:
                self.habitability_counts[planet['habitability']] -= 1
                self.planets.remove(planet)
                self.total_planets -= 1
                return f"\n---\n**Result**: Manual planet '{name}' has been deleted.\n---"
        return f"\n---\n**Result**: Manual planet '{name}' not found.\n---"

    def calculate_habitability_ratios(self):
        if self.total_planets == 0:
            return "No planets have been added yet."
        ratios = {key: count / self.total_planets for key, count in self.habitability_counts.items()}
        result = "\n---\n**Result**: Habitability Ratios\n"
        for category, ratio in ratios.items():
            result += f"{category.replace('_', ' ').capitalize()}: {ratio:.2f}\n"
        result += "---"
        return result

    def list_planets(self):
        if not self.planets:
            return "No planets have been added yet."
        
        manual_planets = [planet for planet in self.planets if not planet['theoretical']]
        theoretical_planets = [planet for planet in self.planets if planet['theoretical']]
        
        manual_df = pd.DataFrame(manual_planets)
        theoretical_df = pd.DataFrame(theoretical_planets)
        
        result = "\n---\n**Manual Planets**:\n"
        result += manual_df.to_string(index=False) if not manual_df.empty else "No manual planets added."
        
        result += "\n\n---\n**Theoretical Planets**:\n"
        result += theoretical_df.to_string(index=False) if not theoretical_df.empty else "No theoretical planets added."
        
        result += "\n---"
        
        return result

    def reset(self):
        self.habitability_counts = {key: 0 for key in self.habitability_counts}
        self.total_planets = 0
        self.planets = []
        return "\n---\n**Result**: Data has been reset.\n---"

def main():
    calculator = PlanetCalculator()
    while True:
        print("\nNASA Planet Habitability Calculator")
        print("1. Fetch planet data")
        print("2. Add a planet manually")
        print("3. Add a theoretical planet")
        print("4. Delete a theoretical planet")
        print("5. Delete a manual planet")
        print("6. Calculate habitability ratios")
        print("7. List planets")
        print("8. Reset data")
        print("9. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            planet_data = calculator.fetch_planet_data()
            if planet_data:
                for planet in planet_data[:500]:  # Limiting to 500 planets for demonstration purposes
                    name = planet['englishName']
                    habitability = calculator.classify_habitability(planet)
                    calculator.add_planet(name, habitability)
                    print(f"Added planet: {name} - {habitability.replace('_', ' ').capitalize()}")
            else:
                print("Failed to fetch planet data.")
        elif choice == '2':
            name = input("Enter the name of the planet (or type 'back' to return): ").strip()
            if name.lower() == 'back':
                continue
            habitability = input("Enter the habitability status (habitable/partially_habitable/potentially_habitable/previously_habitable/non_habitable): ").strip().lower()
            if habitability in calculator.habitability_counts:
                calculator.add_planet(name, habitability)
            else:
                print("Invalid input. Please enter a valid habitability status.")
        elif choice == '3':
            name = input("Enter the name of the theoretical planet (or type 'back' to return): ").strip()
            if name.lower() == 'back':
                continue
            habitability = input("Enter the habitability status (habitable/partially_habitable/potentially_habitable/previously_habitable/non_habitable): ").strip().lower()
            if habitability in calculator.habitability_counts:
                calculator.add_planet(name, habitability, theoretical=True)
            else:
                print("Invalid input. Please enter a valid habitability status.")
        elif choice == '4':
            name = input("Enter the name of the theoretical planet to delete: ").strip()
            print(calculator.delete_theoretical_planet(name))
        elif choice == '5':
            name = input("Enter the name of the manual planet to delete: ").strip()
            print(calculator.delete_manual_planet(name))
        elif choice == '6':
            print(calculator.calculate_habitability_ratios())
        elif choice == '7':
            print(calculator.list_planets())
        elif choice == '8':
            print(calculator.reset())
        elif choice == '9':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()


