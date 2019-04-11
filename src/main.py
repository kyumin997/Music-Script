from Spek import *
from UserInterface import *

if __name__ == '__main__':
    path_to_music = '/home/kyumin/Downloads/Music/'
    file_paths = get_file_path(path_to_music, '.mp3')

    #open_terminal(file_paths)

    root = Tk()
    root.geometry("500x250+710+415")
    app = MusicUI(root)
    app.hide()
    music_dir = app.get_file_dir()
    app.msg_box()
    app.show()
    root.mainloop()

    print("Done!")
