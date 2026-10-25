import random, requests

POOL = ["pikachu", "bulbasaur", "charmander", "squirtle", "snorlax"]
API = "https://pokeapi.co/api/v2/pokemon/"
mons = []

for name in POOL:                          
    try:
        r = requests.get(API + name, timeout=10)
        if r.status_code == 200:
            j = r.json()                   
            abilities = [a["ability"]["name"] for a in j["abilities"]]
            mons.append((j["name"], j["height"] / 10, j["weight"] / 10, abilities))
        else:
            print(f"[{r.status_code}] skipped {name}")
    except requests.exceptions.RequestException as e:
        print(f"[network error] {e}")

if not mons:
    print("Could not load any Pokemon.")
else:
    secret, height, weight, abilities = random.choice(mons)   
    print(f"Height: {height} m   Weight: {weight} kg")
    for i in range(1, 4):                                     
        if i == 3:                                            
            print(f"Hint - abilities: {', '.join(abilities)}")
        if input(f"Attempt {i}/3: ").strip().lower() == secret:
            print(f"Correct! It was {secret.title()}! You win!")
            break
        print("Nope.")
    else:                                                     
        print(f"Out of attempts! The answer was {secret.title()}:")
        print(f"  {height} m, {weight} kg, abilities: {', '.join(abilities)}")