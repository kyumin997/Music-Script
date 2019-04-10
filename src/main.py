import os


def get_file_path(path, extension):
    """
    Grabs all filenames in the given path.

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


def open_terminal(paths):
    """
    Runs ffmpeg in order to save the image to train.
    :param paths:
    :param names:
    :return:
    """
    assert isinstance(paths, list)

    __command_part_one = 'ffmpeg -y -i '
    __command_part_two = ' -lavfi showspectrumpic=s=640x374 '

    for files in paths:
        os.system(__command_part_one + repr(files) +
                  __command_part_two + repr(files) + '.png')


if __name__ == '__main__':
    path_to_music = '/home/kyumin/Downloads/Music/'
    file_paths = get_file_path(path_to_music, '.mp3')

    open_terminal(file_paths)

    print("Done!")
