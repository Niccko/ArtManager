import imagehash, os
from diffimg import diff


def is_image(path):
    return path.split(".")[-1] in ("jpeg", "jpg", "rgb", "gif", "pbm", "pgm", "ppm", "tif", "rast", "xbm", "bmp", "png")


def is_video(path):
    return path.split(".")[-1] in ("mp4")


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
            files_list.append(os.path.join(root_path, file))
    return files_list


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def uniquify_filename(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + "(" + str(counter) + ")" + extension
        counter += 1
    return path


def file_in_folder(folder, file):
    files = [os.path.basename(f) for f in os.listdir(folder)]
    return file in files


def calculate_similarity(paths):
    diffs = []
    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            im_diff = diff(paths[i], paths[j], delete_diff_file=True)
            diffs.append([paths[i], paths[j], im_diff])
    return diffs
