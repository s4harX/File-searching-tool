import os


def search(name, path="/"):
    try:
        with os.scandir(path) as er:
            for e in er:
                if e.is_dir(follow_symlinks=False):
                    re = search(name, e.path)
                    if re:
                        return re
                elif e.name == name:
                    return e.path
    except:
        pass


print("File searcher")
while True:
    result = (search(input("Enter file name: ")))

    if result:
        print(result)

    else:
        print("Not found")
