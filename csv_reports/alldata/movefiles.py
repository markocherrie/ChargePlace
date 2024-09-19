
# move the data that begins with Tickets to Tickets folder

import os

def move_files():
    for file in os.listdir():
        if file.startswith('Tickets'):
            os.rename(file, 'Tickets/' + file)
            
if __name__ == '__main__':
    move_files()
    
    