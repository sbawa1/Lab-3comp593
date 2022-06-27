
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

    print_my_name(Personal_Info)
    print_my_student_id(Personal_Info)
    print_pizza_toppings(Personal_Info)
    print_movies_list(Personal_Info)
    add_pizza_toppings_to_info(Personal_Info,favourite_topping)

    pass


def print_my_name(Personal_Info):
    name = f"My name is' , {Personal_Info['full_name']}, but you call me miss Shallu"
 
def print_my_student_id(Personal_Info):
    sentence =f"My student ID id', {Personal_Info['student_id']}"
    print(sentence)
 
def add_pizza_toppings_to_info(Personal_Info, favourite_toppings):
    Personal_Info['pizza_toppings'].extend(favourite_toppings)

    for i,p in enumerate(Personal_Info['pizza_toppings']):
        Personal_Info['pizza_toppings'][i] = p.capitalize()

        Personal_Info['pizza_toppings'].sort

def print_pizza_toppings(Personal_Info):
    #print the heading
    heading = f"{Personal_Info['full_name']}'s favourite pizza toppings are:"
    print(heading)
    print('-' * len(heading))

   #print dash list of all pizza toppings
    for p in Personal_Info['pizza_toppings']:
       print(f"- {p}")
       print()

def print_movies_list(Personal_Info):

    #my favourite movies-
    print(f"{Personal_Info['full_name'].split(' ')[1]} like to watch", end='')
    for i,t in enumerate(Personal_Info['movies']):
        print(t['genre'], end='')
        if i < len(Personal_Info['movies'])-1:
           print(',', end='')
    print(',', end='\n\n')

    main()

