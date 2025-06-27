
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


# show()
write()
# update()    
 