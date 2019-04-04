import os
import keyboard


def get_filenames(path, extension):
    """
    Grabs all filenames in the given path.
    >>> path = '/home/kyumin/Downloads/Music/'
    >>> get_filenames(path, '.mp3')
    ['/home/kyumin/Downloads/Music/01 Survivors (Original Mix) [NEST029].mp3']

    :param path: a string containing the path of the files you want to find.
    :param extension: file extension you want to search
    :return a list containing the names of the files in the given path.
    """
    files = []
    try:
        for r, d, f in os.walk(path):
            for file in f:
                if extension in file:
                    files.append(os.path.join(r, file))

    except NameError:
        print("That is not a valid path! Please enter in a valid path.")

    return files


def open_terminal(file_paths):
    """
    >>> path = '/home/kyumin/Downloads/Music/'
    >>> file_paths = get_filenames(path, '.mp3')
    >>> open_terminal(file_paths)

    Runs Spek in order to save the image to train.
    :param file_paths:
    :return:
    """
    assert isinstance(file_paths, list)

    for files in file_paths:
        print(files)
        os.popen('spek ' + files).read()

    print('finished.')


def save(song_name):
    """
    Saves image in spek
    :param song_name:
    :return:
    """
    keyboard.press_and_release('ctrl+s')
    keyboard.write(song_name)

