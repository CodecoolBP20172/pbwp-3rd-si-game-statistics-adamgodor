from operator import itemgetter
def count_games(file_name):
    database = open(file_name)
    cont = database.readlines()
    database.close
    return len(cont)

def decide(file_name, year):
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    years = [int(x[2]) for x in data]
    if year in years:
        return True
    else:
        return False

def get_latest(file_name):
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    years = [int(x[2]) for x in data]
    max_index = years.index(max(years))
    print(max_index)
    latest_game = data[max_index][0]
    return latest_game

def count_by_genre(file_name, genre):
    pass
def get_line_number_by_title(file_name, title):
    pass

count_games("game_stat.txt")
decide("game_stat.txt", 2004)
print(get_latest("game_stat.txt"))
