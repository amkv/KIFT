import os
import shutil

def del_folder(folder):
    """check folder, delete if exist"""
    if os.path.exists(folder):
        print 'Deleted: ' + folder
        shutil.rmtree(folder)
    else:
        print 'Not exist: ' + folder

def main():
    incoming_folder = 'incoming'
    outgoing_folder = 'outgoing'
    train_folder = 'train'
    query_folder = 'query'

    path = os.getcwd()
    path_static = '/src/server_src/static/'
    path_train = '/trainer/'
    path_query = '/'

    incoming = path + path_static + incoming_folder
    outgoing = path + path_static + outgoing_folder
    train = path + path_train + train_folder
    query = path + path_query + query_folder

    del_folder(incoming)
    del_folder(outgoing)
    del_folder(train)
    del_folder(query)
    os.system('make fclean')

if __name__ == "__main__":
    main()
