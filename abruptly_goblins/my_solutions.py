#here is the first step, which is making a list of gamers
gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")


kimberly = {
    'name': "Kimberly Warner",
    'availability': ["Monday", "Tuesday", "Friday"]
}

add_gamer(kimberly, gamers)

#here I'll add a bunch of other gamers to the list.
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#next I need to find the availability of the players
def build_daily_frequency_table():
    frequency_table = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0,
    }
    return frequency_table

count_availablility = build_daily_frequency_table()


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1
    return available_frequency

count_availablility = calculate_availability(gamers, count_availablility)

def find_best_night(availability_table):
    highest_number = 0
    best_day = ''
    for key, value in availability_table.items():
        if value > highest_number:
            highest_number = value
            best_day = key
    return best_day

best_day = find_best_night(count_availablility)

def available_on_night(gamers_list, day):
    gamers_attending = [gamer for gamer in gamers_list if day in gamer['availability']]
    return gamers_attending

attending_game_night = available_on_night(gamers, best_day)


#here I generate an email for participants
form_email = '{name}, we have selected {day_of_week} as the {game} game night.'

def send_email(gamers_who_can_attend, day, game):
    for gamers in gamers_who_can_attend:
        print(form_email.format(name=gamers["name"], day_of_week=day, game=game))

#print(send_email(gamers, best_day, 'Abruptly Goblins'))


unable_to_attend_best_night = [gamer for gamer in gamers if best_day not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
print(send_email(available_second_game_night, second_night, 'Abruptly Goblins'))
