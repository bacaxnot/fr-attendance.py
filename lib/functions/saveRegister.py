from .checkFile import checkFile
from datetime import datetime

def saveRegister(register, dirPath):
    '''
    Saves given register in csv file named with current date.

    The function checks if a current date attendance file already exists.
    If exists, opens it to register the given name.
    If not, creates it associating a filename corresponding to the current date.
    
    If given register exists in given file, does not do anything.
    If not, appends the register and current hour to file.
    Arguments:
    - register: string of the register to insert in given file.
    - dirPath: directory path where saved registers files are storaged.
    Output:
    - boolean that indicates if the register
    '''
    # variables
    registered = False

    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')

    filePath = f'{dirPath}/{date}.csv'
    headers = 'NAME,HOUR'
    
    # checking if file exists
    checkFile(filePath, headers)
    
    # File editing
    with open(filePath, 'a+') as file:
        # reading
        file.seek(0)
        lines = file.readlines()
        # checking register existance
        for line in lines:
            entry = line.split(',')
            # register found
            if register in entry:
                return False
        # appending value
        if not registered:
            newEntry = f'\n{register},{time}'
            file.write(newEntry)
            return True
