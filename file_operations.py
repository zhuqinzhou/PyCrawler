import os


def create_project_directory(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        create_file(queue, base_url)
    if not os.path.isfile(crawled):
        create_file(crawled, '')


def create_file(path, date):
    file = open(path, 'w')
    file.write(date)
    file.close()


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


def clear_file(path):
    with open(path, 'w'):
        pass


def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as file:
        for line in file:
            result.add(line.replace('\n', ''))
    return result


def set_to_file(links, file):
    clear_file(file)
    # why can't remove sorted() ?
    for link in sorted(links):
        append_to_file(file, link)
