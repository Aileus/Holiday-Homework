
def write():
    import pickle
    
    with open(r'Holiday Homework\miniproj.dat', 'wb') as f:
        data = [
            {
                "m_id": "M001",
                "name": "Inception",
                "production_cost": 160000000,
                "director": "Christopher Nolan",
                "duration": 148
            },
            {
                "m_id": "M002",
                "name": "The Shawshank Redemption",
                "production_cost": 25000000,
                "director": "Frank Darabont",
                "duration": 142
            },
            {
                "m_id": "M003",
                "name": "The Godfather",
                "production_cost": 6000000,
                "director": "Francis Ford Coppola",
                "duration": 175
            },
            {
                "m_id": "M004",
                "name": "Avengers: Endgame",
                "production_cost": 356000000,
                "director": "Anthony and Joe Russo",
                "duration": 181
            },
            {
                "m_id": "M005",
                "name": "Parasite",
                "production_cost": 11400000,
                "director": "Bong Joon-ho",
                "duration": 132
            }
        ]
        pickle.dump(data,f)
write()        
        
def show():
    import pickle
    
    with open(r'Holiday Homework\miniproj.dat', 'rb') as f:
        movies = pickle.load(f)
        
        for movie in movies:
            for k,v in movie.items():
                
                a = str(k)
                a = a.capitalize()
                if a == 'Budget' : a = 'Budget ($)'
                if a == 'Duration' : a = 'Duratuon (mins)'
                if a == 'Production_cost' : a = 'Production Cost ($)'
                
                print(a,":",v)
            print('\n')
            
show()