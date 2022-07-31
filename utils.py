import imagehash, os

def is_image(path):
    return path.split(".")[-1] in ("jpeg", "jpg", "rgb", "gif", "pbm","pgm", "ppm", "tif", "rast", "xbm", "bmp", "png")

def compute_hash(path):
    try:
        with imagehash.Image.open(path) as image:
            return imagehash.phash(image)
    except Exception as e:
        print(e)

def list_absolute_paths(path):
    return list(map(lambda x: os.path.join(path, x), os.listdir(path)))


def list_subdir(root):
    files_list = []
    for root_path, dirs, files in os.walk(root):
        for file in files:
            files_list.append(os.path.join(root,file))
    return files_list

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def uniquify_filename(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1

    return path