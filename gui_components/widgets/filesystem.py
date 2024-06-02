import logging
import os
import pathlib
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu, QFileSystemModel, QWidget, QFileDialog

from gui_components.ui.ui_fs_viewer_widget import Ui_FileSystemViewer
from gui_components.basis.utils import rm_tree

logger = logging.getLogger(__name__)


class FileSystemViewer(QWidget):
    """
    Widget for File System Viewer.
    Viewer allows navigation on a selected folder and opens the selected file with the FileViewer
    """

    def __init__(self,
                 root_path: str | Path,
                 title: str = "",
                 header_hidden: bool = True
                 ):
        super().__init__()

        self._root_path = pathlib.Path(root_path)

        self._ui = Ui_FileSystemViewer()
        self._ui.setupUi(self)

        self._file_model = QFileSystemModel()
        self._ui.tree_view.setModel(self._file_model)
        self._ui.tree_view.expandAll()
        self._ui.tree_view.header().hideSection(1)
        self._ui.tree_view.header().hideSection(2)
        self._ui.tree_view.header().hideSection(3)
        self._ui.tree_view.setHeaderHidden(header_hidden)
        self._ui.tree_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self._ui.tree_view.customContextMenuRequested.connect(self.on_context_menu)
        self._ui.tree_view.setRootIndex(self._file_model.setRootPath(self._root_path.__str__()))
        self._ui.tree_view.repaint()

        self._ui.tree_view.doubleClicked.connect(self.handle_double_click)

        if title == "":
            self._ui.lbl_title.hide()
        else:
            self._ui.lbl_title.setText(f'<h1>{title}</h1>')

        # connect signals
        self._ui.btn_expand_all.clicked.connect(self.button_click)
        self._ui.btn_collapse_all.clicked.connect(self.button_click)
        self._ui.btn_select_path.clicked.connect(self.button_click)
        self._ui.btn_level_up.clicked.connect(self.button_click)

    def set_root_path(self, path: str | Path):
        self._root_path = pathlib.Path(path)
        self._ui.tree_view.setRootIndex(self._file_model.setRootPath(self._root_path.__str__()))
        self._ui.tree_view.repaint()

    def on_context_menu(self, pos):

        index = self._ui.tree_view.indexAt(pos)
        if not index.isValid():
            return

        model = index.model()
        path = pathlib.Path(model.filePath(index))

        if not path.exists():
            return

        # Build the context menu
        menu = QMenu()
        open_as_menu = QMenu()

        open_dir = menu.addAction("Enter folder")
        open_as_menu.setTitle('Open as...')
        # add actions to the menu

        menu.addSeparator()
        menu.addMenu(open_as_menu)
        menu.addSeparator()
        open_in_explorer = menu.addAction("Open in Explorer")
        menu.addSeparator()
        delete_action = menu.addAction("Delete")

        # Disable actions that are usable in certain conditions
        if path.is_dir():
            open_as_menu.setDisabled(True)

        if path.is_file():
            open_dir.setDisabled(True)

        # Define actions
        action = menu.exec_(self._ui.tree_view.mapToGlobal(pos))

        if action == delete_action:
            try:
                if path.is_dir():
                    rm_tree(path)
                else:
                    path.unlink(missing_ok=True)
            except Exception as e:
                logger.debug(e)

        if action == open_in_explorer:
            os.startfile(path.__str__())  # Open folder in Explorer

        if action == open_dir:
            self.set_root_path(path)

    @staticmethod
    def handle_double_click(index):
        """
        By double-click on a file, the FileViewer will try to open the file with a default format.
        :param index: Selection index
        :return: None
        """
        if index.isValid():
            model = index.model()
            file_path = pathlib.Path(model.filePath(index))

            if file_path.is_file():
                match file_path.suffix:
                    case "set_file_extension_here":
                        pass
                    case other:  # default
                        logger.debug("No default format found, please specify format -> open with explorer")
                        os.startfile(file_path.__str__())

    def button_click(self) -> None:

        # expand all
        if self.sender() == self._ui.btn_expand_all:
            self._ui.tree_view.expandAll()
            self._ui.tree_view.repaint()

        # collapse all
        if self.sender() == self._ui.btn_collapse_all:
            self._ui.tree_view.collapseAll()
            self._ui.tree_view.repaint()

        # select path
        if self.sender() == self._ui.btn_select_path:
            path = QFileDialog.getExistingDirectory(self, "Open Directory...", self._root_path.__str__())

            if path != "":
                self.set_root_path(path)

        # level up
        if self.sender() == self._ui.btn_level_up:
            self.set_root_path(self._root_path.parent)

        # context menu
        if self._ui.tree_view.selectedIndexes():
            items = self._ui.tree_view.selectedIndexes()[0]
            path = pathlib.Path(self._file_model.filePath(items))

            # add actions to the menu
