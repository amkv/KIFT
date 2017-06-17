
def add_to_history(path, output_from_bla, text_to_client):
    with open(path + '/history/' + 'logs', 'a') as file:
        file.write('user: ' + output_from_bla + '\n')
        file.write('bla:  ' + text_to_client + '\n\n')
