def count_games(file_name):
    print("How many games are in the file?")
    database = open(file_name)
    cont = database.readlines()
    database.close()
    return len(cont)


def decide(file_name, year):
    print("Is there a game from a given year?")
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
    print("Which was the latest game?")
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    years = [int(x[2]) for x in data]
    max_index = years.index(max(years))
    latest_game = data[max_index][0]
    return latest_game


def count_by_genre(file_name, genre):
    print("How many games do we have by genre?")
    print(genre)
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    genre_list = [x[3] for x in data]
    genre_occurance = genre_list.count(genre)
    return genre_occurance


def get_line_number_by_title(file_name, title):
    print("What is the line number of the given game (by title)?")
    print(title)
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    title_list = [x[0] for x in data]
    alist = []
    for titles in enumerate(title_list, start=1):
        alist.append(titles)
    for i in alist:
        if title == i[1]:
            title_position = i[0]
            return title_position
    return "This title is not in the list!"


def sort_abc(file_name):
    print("What is the alphabetical ordered list of the titles?")
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    title_list = [x[0] for x in data]
    sorted_title_list = sorted(title_list)
    return sorted_title_list


def get_genres(file_name):
    print("What are the genres?")
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    genre_list = [x[3] for x in data]
    set_genre = sorted(set(genre_list), key=str.lower)
    return set_genre


def when_was_top_sold_fps(file_name):
    print("What is the release date of the top sold First-person shooter game?")
    with open(file_name) as database:
        release_dates = database.read()
    data = [x.split("\t") for x in release_dates.split("\n")]
    data = data[:-1]
    fps_games = []
    for i in data:
        if i[3] == "First-person shooter":
            fps_games.append(i)
    year_of_fps = [float(x[1]) for x in fps_games]
    fps_index = year_of_fps.index(max(year_of_fps))
    year_of_release = int(fps_games[fps_index][2])
    return year_of_release


def main():
    print(count_games("game_stat.txt"), "\n")
    print(decide("game_stat.txt", 2004), "\n")
    print(get_latest("game_stat.txt"), "\n")
    print(count_by_genre("game_stat.txt", "RPG"), "\n")
    print(get_line_number_by_title("game_stat.txt", "StarCraft"), "\n")
    print(sort_abc("game_stat.txt"), "\n")
    print(get_genres("game_stat.txt"), "\n")
    print(when_was_top_sold_fps("game_stat.txt"), "\n")


main()
