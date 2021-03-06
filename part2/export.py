export_data = []


def get_most_played(file_name):
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    sells = [float(x[1]) for x in data]
    max_index = sells.index(max(sells))
    highest_sold = data[max_index][0]
    export_data.append(highest_sold)
    return highest_sold


def sum_sold(file_name):
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    sells = sum([float(x[1]) for x in data])
    export_data.append(sells)
    return sells


def get_selling_avg(file_name):
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    sells = [float(x[1]) for x in data]
    avg_sells = (sum(sells) / len(sells))
    export_data.append(avg_sells)
    return avg_sells


def count_longest_title(file_name):
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    titles = [str(x[0]) for x in data]
    longest_title = max(titles, key=len)
    export_data.append(len(longest_title))
    return len(longest_title)


def get_date_avg(file_name):
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    years_of_release = [int(x[2]) for x in data]
    avg_release = (sum(years_of_release) / len(years_of_release))
    export_data.append(avg_release)
    return round(avg_release)


def get_game(file_name, title):
    with open(file_name) as database:
        release_dates = database.read().strip()
    data = [x.split("\t") for x in release_dates.split("\n")]
    for row in data:
        if title == row[0]:
            row[1] = float(row[1])
            row[2] = int(row[2])
            game_data = row
            export_data.append(game_data)
            return game_data
    export_data.append("This title is not in the list!")
    return "This title is not in the list!"


def count_grouped_by_genre(file_name):
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
    export_data.append(genre_counter)
    return genre_counter


def get_date_ordered(file_name):
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
    export_data.append(orderded_list_by_date_and_name)
    return orderded_list_by_date_and_name


def export(file_name="data2.csv"):
    export_file = open(file_name, "w")
    for i in export_data:
        export_file.write(str(i))
        export_file.write("\n")
    export_file.close()


def main():
    get_most_played("game_stat.txt")
    sum_sold("game_stat.txt")
    get_selling_avg("game_stat.txt")
    count_longest_title("game_stat.txt")
    get_date_avg("game_stat.txt")
    get_game("game_stat.txt", "StarCraft")
    count_grouped_by_genre("game_stat.txt")
    get_date_ordered("game_stat.txt")
    export()


main()
