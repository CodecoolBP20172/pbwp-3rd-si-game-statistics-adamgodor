def get_most_played(file_name):
    print("What is the title of the most played game?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    sells = [float(x[1]) for x in data]
    max_index = sells.index(max(sells))
    highest_sold = data[max_index][0]
    return highest_sold


def sum_sold(file_name):
    print("How many copies have been sold total?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    sells = sum([float(x[1]) for x in data])
    return sells


def get_selling_avg(file_name):
    print("What is the average selling?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    sells = [float(x[1]) for x in data]
    avg_sells = (sum(sells) / len(sells))
    return avg_sells


def count_longest_title(file_name):
    print("How many characters long is the longest title?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    titles = [str(x[0]) for x in data]
    longest_title = max(titles, key=len)
    return len(longest_title)


def get_date_avg(file_name):
    print("What is the average of the release dates?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    years_of_release = [int(x[2]) for x in data]
    avg_release = (sum(years_of_release) / len(years_of_release))
    return round(avg_release)


def get_game(file_name, title):
    print("What properties has a game?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    for row in data:
        if title == row[0]:
            row[1] = float(row[1])
            row[2] = int(row[2])
            game_data = row
            print("Game title: {}".format(game_data[0]))
            print("Copies sold in million: {}".format(game_data[1]))
            print("Date of release: {}".format(game_data[2]))
            print("Genre: {}".format(game_data[3]))
            print("Publisher: {}".format(game_data[4]))
            print("\n")
            return game_data
    return print("This title is not in the list!", "\n")


def count_grouped_by_genre(file_name):
    print("How many games are there grouped by genre?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    genre_list = [x[3] for x in data]
    genre_counter = {}
    for genre in genre_list:
        if genre in genre_counter:
            a = genre_counter.get(genre) + 1
            genre_counter[genre] = a
        else:
            genre_counter.update({genre: 1})
    for k, v in genre_counter.items():
        print(str(k).rjust(22) + " : " + str(v))
    print("\n")
    return genre_counter


def get_date_ordered(file_name):
    print("What is the date ordered list of the games?")
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    title = [str(x[0]) for x in data]
    date = [int(x[2]) for x in data]
    title_date_list = list(zip(title, date))
    ordered_data = sorted(
        sorted(
            title_date_list,
            key=lambda title_date_list: title_date_list[0]),
        key=lambda title_date_list: title_date_list[1],
        reverse=True)
    orderded_list_by_date_and_name = [str(x[0]) for x in ordered_data]
    for i in orderded_list_by_date_and_name:
        print(i)
    return orderded_list_by_date_and_name


def main():
    print(get_most_played("game_stat.txt"), "\n")
    print(sum_sold("game_stat.txt"), "\n")
    print(get_selling_avg("game_stat.txt"), "\n")
    print(count_longest_title("game_stat.txt"), "\n")
    print(get_date_avg("game_stat.txt"), "\n")
    get_game("game_stat.txt", "Minecraft")
    count_grouped_by_genre("game_stat.txt")
    get_date_ordered("game_stat.txt")


main()
