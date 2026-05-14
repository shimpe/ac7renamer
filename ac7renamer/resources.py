from importlib.resources import files


def image_path(name: str) -> str:
    return str(files("ac7renamer").joinpath("images", name))
