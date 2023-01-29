import doctest 

# All functions in this file were implemented by me as well as the type alias DateInfo

# represents information for a date (year number, month number, day number) 
# assumes year number, month number, and day number represent a valid date in the calendar year 
DateInfo = tuple[int, int, int] 
YEAR_INDEX = 2 
MONTH_INDEX = 1 
DAY_INDEX = 0 

# represents information for a Netflix show (show type, show title, list of show director names, list of show actor names, date show was added) 
NetflixShowInfo = tuple[str, str, list[str], list[str], DateInfo]
TITLE_INDEX = 1 
ACTOR_LIST = 3 
DATE_ADDED = 4 

def multiply_by(list1: list[float], list2: list[int]) -> None: 
    '''
    given a list of elements that can be multiplied by an integer and a second list of non-negative integers, the function will upadte the first list so that every element in the first list is multiplied by value at the corresponding position in the second list. 
    >>> multiply_by([1, 2, 3], [2, 4, 0]) 
    >>> multiply_by([1, 2, 3], [2, 4]) 
    >>> multiply_by([1, 2, 3], [2, 4, 0, 2]) 
    >>> multiply_by([5.5, -4, 0], [23, 3]) 
    >>> multiply_by([5.5, -4, 0], [23, 3, 1, 0]) 
    >>> multiply_by([1.2, 0.5], [13, 2, 3, 0]) 
    '''
    len_list1 = len(list1) 
    len_list2 = len(list2) 
    
    if len_list1 > 0 and len_list2 > 0: 
        if len_list2 <= len_list1: 
            for index in range(len_list2): 
                list1[index] *= list2[index] 
        elif len_list2 > len_list1: 
            for index in range(len_list1): 
                list1[index] *= list2[index] 

def create_date(date: str) -> DateInfo: 
    '''
    given a string that represents a valid date in the calendar year and returns a date as a tuple (as specified in DateInfo). 
    
    Precondition: date must be in the format 'day-month-year' where day is a 2 digit integer representing a valid day in the month, month is the first 3 letters of a valid month, and its first letter is uppercase, and year is a 2 digit integer representing a year in the 2000's 
    >>> create_date('10-Jan-18') 
    (2018, 1, 10)
    >>> create_date('22-Feb-00') 
    (2000, 2, 22)
    >>> create_date('23-Mar-10') 
    (2010, 3, 23)
    >>> create_date('01-Apr-01') 
    (2001, 4, 1)
    >>> create_date('02-May-02') 
    (2002, 5, 2)
    >>> create_date('30-Jun-05') 
    (2005, 6, 30)
    >>> create_date('21-Jul-19') 
    (2019, 7, 21)
    >>> create_date('05-Aug-18') 
    (2018, 8, 5)
    >>> create_date('14-Sep-20') 
    (2020, 9, 14)
    >>> create_date('31-Oct-21') 
    (2021, 10, 31)
    >>> create_date('22-Nov-10') 
    (2010, 11, 22)
    >>> create_date('20-Dec-09') 
    (2009, 12, 20)
    '''
    final_tuple = []
    date_list = date.split('-') 
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
    index = 0 
    
    final_tuple.append(int(str(20) + str(date_list[YEAR_INDEX]))) 
    
    while not months[index] == date_list[MONTH_INDEX]: 
        index += 1 
    
    final_tuple.append(index+1) 
    
    if str(date_list[DAY_INDEX])[0] == 0: 
        final_tuple.append(int(str(date_list[DAY_INDEX])[1]))  
    else: 
        final_tuple.append(int(date_list[DAY_INDEX])) 
    
    return tuple(final_tuple) 

def create_show(show_type: 'str', title: 'str', director_names: 'str', actor_names: 'str', date_added_Netflix: 'str') -> NetflixShowInfo: 
    '''
    given show type, title, directors, actors, and date added to Netflix, the function returns a Netflix show tuple 
    
    Precondition: names of directors and actors are separated by ':' and the date added to Netflix is given in the format 'day-month-year'. Where day is a 2 digit integer representing a valid day in the calendar month, month is the first 3 letters of a valid month, where the first letter is uppercase, and year is a 2 digit integer representing a year in the 2000's. date_added_Netflix is not an empty string. 
    >>> create_show('Movie', 'The Invention of Lying', 'Ricky Gervais:Matthew Robinson', 'Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey', '02-Jan-18') 
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))
    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09') 
    ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))
    >>> create_show('Movie', 'The Bad Kids', 'Keith Fulton:Louis Pepe', '', '01-Apr-17') 
    ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1))
    '''
    final_tuple = [] 
    directors_list = director_names.split(':') 
    actors_list = actor_names.split(':') 
    len_directors = len(director_names) 
    len_actors = len(actor_names) 

    final_tuple.append(show_type) 
    final_tuple.append(title) 
    
    if not len_directors == 0: 
        final_tuple.append(directors_list) 
    else: 
        final_tuple.append([]) 
        
    if not len_actors == 0: 
        final_tuple.append(actors_list) 
    else: 
        final_tuple.append([]) 
    
    date = create_date(date_added_Netflix) 
    final_tuple.append(date) 
    
    return tuple(final_tuple) 

def get_titles(show_list: list[NetflixShowInfo]) -> list[str]: 
    '''
    given a list of NetflixShowInfo tuples, the function returns a list of strings containing the titles of each of the Netflix shows in the order that they appear in the given list. 
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))]) 
    ['The Invention of Lying', 'The Mind Explained']
    >>> get_titles([(), ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))]) 
    ['The Invention of Lying']
    >>> get_titles([('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12)), ()]) 
    ['The Mind Explained']
    '''
    final_list = [] 
    len_show_list = len(show_list) 
    index = 0 
    
    while index < len_show_list: 
        show_tuple = show_list[index]
        if len(show_tuple) > 0: 
            final_list.append(show_tuple[TITLE_INDEX]) 
        index += 1 
    
    return final_list 

def is_actor_in_show(show_tuple: NetflixShowInfo, actor: str) -> bool: 
    '''
    given a tuple containing information on a Netflix show and a string representing an actor, the function returns True if the given actor is an actor in the given Netflix show. False otherwise. 
    
    Precondition: actor is not an empty string 
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Rob Lowe') 
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'MAtthew Robinson') 
    False
    >>> is_actor_in_show(('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12)), 'emma Stone') 
    True
    >>> is_actor_in_show(('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12)), 'Rob Lowe') 
    False
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'emma stone') 
    False
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'roB lowE') 
    True
    >>> is_actor_in_show(('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), 'emma Stone') 
    False
    '''
    actors = show_tuple[ACTOR_LIST] 
    len_actors = len(actors) 
    index = 0 
    
    while index < len_actors and not actors[index].lower() == actor.lower():
        index += 1 
    
    if len_actors == 0: 
        return False
    elif index == len_actors: 
        return actors[index-1].lower() == actor.lower() 
    else: 
        return True 

def count_shows_before_date(show_list: list[NetflixShowInfo], date: DateInfo) -> int: 
    '''
    given a list of tuples containing NetflixShowInfo and a date in the format DateInfo, the function will return a count of the number of Neflix show tuples for which the date they were added is BEFORE the given date in the calendar. 
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], (2018, 12, 12)) 
    2
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], (2020, 1, 3)) 
    4
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], (2015, 10, 31)) 
    0
    '''
    count = 0 
    len_show_list = len(show_list) 
    
    for index in range(len_show_list):  
        show_tuple = show_list[index] 
        show_date = show_tuple[DATE_ADDED] 
        if show_date < date: 
            count += 1 
    
    return count 

def get_shows_with_actor(show_list: list[NetflixShowInfo], actor: 'str') -> list[NetflixShowInfo]: 
    '''
    given a list of tuples that contain NetflixShowInfo and a string representing an actor, the function returns a list of only the Netflix show tuples that the given actor has acted in. 
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], 'Emma Stone') 
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], 'emmA sTone') 
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))], 'Ricky Gervais') 
    []
    '''
    final_list = [] 
    len_show_list = len(show_list) 
    
    for index in range(len_show_list): 
        show_tuple = show_list[index] 
        if is_actor_in_show(show_tuple, actor) == True: 
            final_list.append(show_tuple) 
    
    return final_list 
