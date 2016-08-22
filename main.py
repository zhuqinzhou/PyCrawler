import os


def createProjectDirectory(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

def createDataFiles(projName, baseURL):
    queue = projName + '/q.txt'
    crawled = projName + '/crawled.txt'
    if not os.path.isfile(queue):
        createFile(queue, baseURL)
    if not os.path.isfile(crawled):
        createFile(crawled, '')

def createFile(path, date):
    file = open(path, 'w')
    file.write(date)
    file.close()

def appendToFile(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def clearFile(path):
    with open(path, 'w'):
        pass

def fileToSet(fileName):
    result = set();
    with open(fileName, 'rt') as file:
        for line in file:
            result.add(line.replace('\n', ''))
    return result

def setToFile(links, file):
    clearFile(file)
    for link in links:
        appendToFile(file, link)