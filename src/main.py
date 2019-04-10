import os
import threading
from pynput.keyboard import Key, Controller


def get_file_name(path, extension):
    """
    Grabs all filenames in the given path.
    >>> path = '/home/kyumin/Downloads/Music/'
    >>> get_file_name(path, '.mp3')
    ['01 Survivors (Original Mix) [NEST029].mp3']

    :param path: a string containing the path of the files you want to find.s
    :param extension: file extension you want to search
    :return a list containing the names of the files in the given path.
    """
    assert isinstance(path, str)
    assert isinstance(extension, str)

    files = []
    try:
        for r, d, f in os.walk(path):
            for file in f:
                if extension in file:
                    files.append(file)

    except NameError:
        print("That is not a valid path! Please enter in a valid path.")

    return files


def get_file_path(path, extension):
    """
    Grabs all filenames in the given path.
    >>> path = '/home/kyumin/Downloads/Music/'
    >>> get_file_path(path, '.mp3')
    ['/home/kyumin/Downloads/Music/01 Survivors (Original Mix) [NEST029].mp3']

    :param path: a string containing the path of the files you want to find.
    :param extension: file extension you want to search
    :return a list containing the names of the files in the given path.
    """
    assert isinstance(path, str)
    assert isinstance(extension, str)

    files = []
    try:
        for r, d, f in os.walk(path):
            for file in f:
                if extension in file:
                    files.append(path + file)

    except NameError:
        print("That is not a valid path! Please enter in a valid path.")

    return files


def save(keyboard, song_name):
    """
    Saves image in spek
    :param song_name:
    :return:
    """
    # Save File
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release('s')
    keyboard.release(Key.ctrl)

    # Write the song name
    keyboard.type(song_name)

    # Save File in Directory
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def open_terminal(paths):
    """
    >>> path = '/home/kyumin/Downloads/Music/'
    >>> file_paths = get_file_names(path, '.mp3')
    >>> open_terminal(file_paths)

    Runs Spek in order to save the image to train.
    :param file_paths:
    :return:
    """
    assert isinstance(paths, list)

    for files in paths:
        os.system('spek ' + repr(files))


if __name__ == '__main__':
    path_to_music = '/home/kyumin/Downloads/Music/'
    file_paths = get_file_path(path_to_music, '.mp3')
    file_names = get_file_name(path_to_music, '.mp3')

    keyboard = Controller()

    terminal_thread = threading.Thread(target=open_terminal, args=file_paths)
    save_thread = threading.Thread(target=save, args=(keyboard, file_names))

    terminal_thread.start()
    save_thread.start()

    terminal_thread.join()
    save_thread.join()

    print("Done!")
