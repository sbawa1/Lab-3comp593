
def main():

    # Define the complex data structure by adding personal info
    Personal_Info = {
              'full_name': 'Shallu bawa',
              'Student_id': '10279330',
              'pizza_toppings': [
                 'extra cheese',
                 'onions',
                 'pineapple'
              ], 
                 'movies' : [
                  {
                          'title' : 'Bagban',
                        'genre' : 'Romantic'
                  },
                  {
                         'title' : '3 Idiots',
                         'genre' : 'Comedy'
                  }
              ]
    }


    # Add a new movie to the data structure
    new_movie = { 'title':'Conjuring', 'genre':'Horror',}
    Personal_Info['movies'].append(new_movie)

    # Add some more pizza toppings to the data structure
    favourite_topping = (['Black olives', 'Sausage', 'Greeen pepper'])
    add_pizza_toppings_to_info(Personal_Info, favourite_topping)

    # Print information from the complex data structure
    print_my_student_id(Personal_Info)
    print_pizza_toppings(Personal_Info)
    print_movies_list(Personal_Info)

    pass


def print_my_name(info):
    name = f"My name is' , {info['full_name']}, but you call me miss Shallu"
 
def print_my_student_id(info):
    sentence =f"My student ID id', {info['student_id']}"
    print(sentence)
 
def add_pizza_toppings_to_info(info, favourite_toppings):
    info['pizza_toppings'].extend(favourite_toppings)

    for i,p in enumerate(info['pizza_toppings']):
        info['pizza_toppings'][i] = p.capitalize()

        info['pizza_toppings'].sort

def print_pizza_toppings(info):
    #print the heading
    heading = f"{info['full_name']}'s favourite pizza toppings are:"
    print(heading)
    print('-' * len(heading))

   #print dash list of all pizza toppings
    for p in info['pizza_toppings']:
       print(f"- {p}")
       print()

def print_movies_list(info):

    #my favourite movies-
    print(f"{info['full_name'].split(' ')[1]} like to watch", end='')
    for i,t in enumerate(info['movies']):
        print(t['genre'], end='')
        if i < len(info['movies'])-1:
           print(',', end='')
    print(',', end='\n\n')

    main()

