
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
        
def show():
    import pickle
    
    with open(r'Holiday Homework\miniproj.dat', 'rb') as f:
        movies = pickle.load(f)
        
        try:
            for movie in movies:
                for k,v in movie.items():
                    a = str(k)
                    a = a.capitalize()
                    if a == 'Budget' : a = 'Budget ($)'
                    if a == 'Duration' : a = 'Duratuon (mins)'
                    if a == 'Production_cost' : a = 'Production Cost ($)'
                    
                    print(a,":",v)
                print('\n')
                
        except EOFError:
            print('No data')


def update():
    import pickle
    movie_id = input('Enter the movie id of the movie you want to make changes to: ')
    movie_id = movie_id.capitalize()
    with open(r'Holiday Homework\miniproj.dat', 'rb') as f:
        movies = pickle.load(f)
        
        m = [i.get('m_id') for i in movies]
        # print(m)
        
        for movie in movies:
            if movie['m_id'] == movie_id:
                key = []
                val = []
                for k,v in movie.items():
                    key.append(k), val.append(v)
                    a = str(k)
                    a = a.capitalize()
                    if a == 'Duration' : a = 'Duratuon (mins)'
                    if a == 'Production_cost' : a = 'Production Cost ($)'
                    print(a,":",v)
                    
                selected_movie = dict(zip(key,val))
                # print(selected_movie)
                print('\n')
                
            elif movie_id not in m:
                print(f'The Movie Id : {movie_id} Not found!')
                exit()
                
        print('Select the field you want to edit: \n 1--> Name \n 2--> Production Cost \n 3--> Director \n 4--> Duration \nType 1 to 4 to select')
        field = int(input('Enter the number of the field you want to edit: '))

        match field:
            case 1:
                print(r'You have selected the "Name" field')
                name = input('Type the new name: ')
                selected_movie['name'] = name
            case 2:
                print(r'You have selected the "Production Cost" field')
                cost = int(input('Type the new production cost: '))
                selected_movie['production_cost'] = cost
            case 3:
                print(r'You have selected the "Director" field')
                director = input('Type the new director: ')
                selected_movie['director'] = director
            case 4:
                print(r'You have selected the "Duration" field')
                duration = int(input('Type the new duration (in minutes): '))
                selected_movie['duration'] = duration
            case _:
                print("Invalid selection.")

        print(selected_movie)
        data = []
        for movie in movies:
                if movie['m_id'] == selected_movie['m_id']:
                    movie = selected_movie
                    data.append(selected_movie)
                else:
                    data.append(movie)
                    
        with open(r'Holiday Homework\miniproj.dat', 'wb') as f:
            pickle.dump(data,f)        

def search():
    import pickle
    print('Select the field you want to search: \n 1--> Movie Id \n 2--> Name \n 3--> Production Cost \n 4--> Director \n 5--> Duration \nType 1 to 5 to select')
    field = int(input('Enter the number of the field you want to search: '))
    match field:
        case 1:
            print(r'You have selected the "Movie Id" field')
            movie_id = input('Type the movie id: ')
        case 2:
            print(r'You have selected the "Name" field')
            name = input('Type the name: ')
        case 3:
            print(r'You have selected the "Production Cost" field')
            cost = int(input('Type the production cost: '))
        case 4:
            print(r'You have selected the "Director" field')
            director = input('Type the director: ')
        case 5:
            print(r'You have selected the "Duration" field')
            duration = int(input('Type the duration (in minutes): '))
        case _:
            print("Invalid selection.")
    
    with open(r'Holiday Homework\miniproj.dat', 'rb') as f:
        movies = pickle.load(f)
        
        found = False
        for movie in movies:
            matched = False
            if 'name' in locals() and name.lower() in movie['name'].lower():
                matched = True
            elif 'director' in locals() and director.lower() in movie['director'].lower():
                matched = True
            elif 'cost' in locals() and cost == movie['production_cost']:
                matched = True
            elif 'duration' in locals() and duration == movie['duration']:
                matched = True
            elif 'movie_id' in locals() and movie_id == movie['m_id']:
                matched = True

            if matched:
                found = True
                print("\nMovie Found-->")
                for k, v in movie.items():
                    label = str(k).capitalize()
                    if label == 'Duration': label = 'Duration (mins)'
                    elif label == 'Production_cost': label = 'Production Cost ($)'
                    print(f" {label} : {v}")

        if not found:
            print("\nNo matching movie found.")

        
        
        
search()
# show()
# write()
# update()    
 