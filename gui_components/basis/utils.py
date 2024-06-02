import pathlib
from pathlib import Path
import re
from os import PathLike

from PyQt5.QtWidgets import QWidget, QLayout


def nearest(lst, number):
    """
    Find closes number in a list
    :param lst: List to find number
    :param number: Reference number
    :return: The Closest number from list
    """
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - number))]


def is_valid_filename(filename: str) -> bool:
    """
    Returns true if filename is valid
    :param filename: filename to validate
    :return: True if valid, false if not
    """
    if not re.match(r'^[a-zA-Z0-9_-]+$', filename):
        return False

    if len(filename) > 255:
        return False

    if filename.startswith('.') or filename.endswith('.'):
        return False

    reserved = ['/', '\\', '?', '*', '<', '>', '|', '"', ':', ';', ',']
    for r in reserved:
        if r in filename:
            return False

    return True


def get_folders_dict(path: str | PathLike) -> dict:
    """
    Get a dict with structure of folder. key is folder name and value is path to folder
    :param path: path to calculate dict
    :return: dict with folder structure
    """
    folders_dict = {}
    folders = pathlib.Path(path)
    for folder in folders.iterdir():
        if folder.is_dir():
            folders_dict[folder.name] = pathlib.Path(path, folder)
    return folders_dict


def remove_widget_from_layout(widget: QWidget, layout: QLayout, delete=False):
    """
    Removes a widget from layout and delete if afterward
    :param widget: Widget to remove
    :param layout: Layout to find Widget
    :param delete: If True delete widget after removing from layout
    :return:
    """
    if widget in [layout.itemAt(i).widget() for i in range(layout.count())]:
        layout.removeWidget(widget)
        if delete:
            widget.deleteLater()


def swap_list_elements(list_src: list, pos1: int, pos2: int) -> list:
    # popping both the elements from list
    first_ele = list_src.pop(pos1)
    second_ele = list_src.pop(pos2 - 1)

    # inserting in each other's positions
    list_src.insert(pos1, second_ele)
    list_src.insert(pos2, first_ele)

    return list_src


def rm_tree(pth: str | PathLike | Path):
    """
    Remove recursively content of folder
    :param pth: Path to folder
    :return:
    """
    pth = pathlib.Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


def create_default_folders(dir_struct: dict, root_path: str | Path) -> True:
    """
    Created folders recursively from a dict structure
    :param dir_struct: Dir structure to create
    :param root_path: Root path where to place the folders
    :return: True=Succeeded, False=Exception during dir creation
    """
    for feature, val in dir_struct.items():
        path = root_path.joinpath(feature)
        if isinstance(val, dict):
            try:
                path.mkdir()
            except OSError as e:
                return False
            create_default_folders(val, path)
    return True
