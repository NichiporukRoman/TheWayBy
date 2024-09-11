def read_message(name):
    file = open('data/travel_ways_data/messages_data/' + name, 'r', encoding='utf-8')
    message = file.read()
    file.close()
    return message