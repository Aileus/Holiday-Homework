
def write():
    import pickle
    
    with open(r'Holiday Homework\miniproj.dat', 'wb') as f:
        data = [
    {
        "name": "Inception",
        "production_cost": 160000000,
        "director": "Christopher Nolan",
        "duration": 148,
        "budget": 165_000_000
    },
    {
        "name": "The Shawshank Redemption",
        "production_cost": 25000000,
        "director": "Frank Darabont",
        "duration": 142,
        "budget": 28_000_000
    },
    {
        "name": "The Godfather",
        "production_cost": 6000000,
        "director": "Francis Ford Coppola",
        "duration": 175,
        "budget": 6_500_000
    },
    {
        "name": "Avengers: Endgame",
        "production_cost": 356000000,
        "director": "Anthony and Joe Russo",
        "duration": 181,
        "budget": 400_000_000
    },
    {
        "name": "Parasite",
        "production_cost": 11400000,
        "director": "Bong Joon-ho",
        "duration": 132,
        "budget": 12_000_000
    }
]
        pickle.dump(data,f)
write()        
        
def show():
    import pickle
    
    with open(r'Holiday Homework\miniproj.dat', 'rb') as f:
        data = pickle.load(f)
        print(data[0]['production_cost'])
show()