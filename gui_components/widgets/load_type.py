
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar
from gui_components.ui.ui_load_settings import Ui_Load
from gui_components.ui.ui_line_settings import Ui_Line

class LoadWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Load()
        self.ui.setupUi(self)

class LineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Line()
        self.ui.setupUi(self)


