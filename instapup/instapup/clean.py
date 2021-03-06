import threading
import os

#would remove all files with the REMOVE_ME extension at the end
def clean():
    dir_name = "instapup/images/"
    test = os.listdir(dir_name)

    

    for item in test:
        if item.endswith(".REMOVE_ME"):
            os.remove(os.path.join(dir_name, item))

#would run this function again every 300 seconds
def main():
    clean()
    threading.Timer(300.0, main).start()


if __name__ == '__main__':
    main()