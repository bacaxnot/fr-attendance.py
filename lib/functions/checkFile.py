def checkFile(filePath, headers = ''):
    '''
    Checks if file in given path exists. If not, creates it.
    Prints in console informative messages.
    Arguments:
    - filePath: string of desired file path
    '''
    try:
        # file exists
        with open(filePath, 'r') as file:
            pass
    
    except IOError:
        # file does not exist
        with open(filePath, 'a') as file:
            # headers appending
            if headers:
                file.write(headers)