import json
import sys
import logging

from PyQt5.QtWidgets import QTreeView, QApplication, QHeaderView, QWidget, QGridLayout, QMenu, QLabel
from PyQt5.QtCore import QFileInfo, Qt, pyqtSignal

from gui_components.basis.models.tree import TreeModel
from gui_components.basis.models.dict_list_model import DictListModel
from gui_components.widgets.load_type import LoadWidget, LineWidget

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)-11s - %(levelname)-7s - %(message)s",
)


# CustomTreeView class

class LineEditorTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        action_modify = contextMenu.addAction("Modify item")
        action_delete_item = contextMenu.addAction("Delete item")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == action_modify:
            index = self.currentIndex()
            logger.debug(f"Modify row: {index.row()}")
        elif action == action_delete_item:
            index = self.currentIndex()
            logger.debug(f"Delete row: {index.row()}")



class LineEditor(QWidget):
    # on_clicked signal
    item_selected = pyqtSignal(QWidget)

    def __init__(self, path, content_widget=None):
        super().__init__()

        self._content_widget = content_widget

        with open(path) as f:
            doc = json.load(f)


        # self.tree_model = TreeModel(headers=["Line"], data=doc)
        self.tree_model = DictListModel(headers=["Line", "ID"], data=doc)
        treeview = LineEditorTreeView()
        treeview.setModel(self.tree_model)
        treeview.repaint()
        treeview.selectionModel().selectionChanged.connect(self.on_clicked)

        layout = QGridLayout()
        layout.addWidget(treeview)

        self.setLayout(layout)

    def set_content_widget(self, content_widget):
        self._content_widget = content_widget

    def get_content_widget(self):
        return self._content_widget


    def on_clicked(self, index):

        item = index.indexes()[0].internalPointer()

        decr = item.data(0)

        if decr == "Line":
            self._content_widget.set_content(LineWidget())
        elif decr == "Motor":
            self._content_widget.set_content(LoadWidget())




