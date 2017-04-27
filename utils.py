import os


def clean_visualizations(path):
    """ Removes all files created by PyntCloud.plot()

    Warning: this will remove all html, ply and json files in path

    Parameters
    ----------
    path: str

    """
    for file in os.listdir(path):
        ext = file.split(".")[-1]
        if ext in {"html", "ply", "json"}:
            print("Removing {}".format(file))
            os.remove(os.path.join(path, file))
