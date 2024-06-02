import logging
import sys

from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QLabel, QCheckBox, QWidget, QLineEdit, QSpinBox, QRadioButton,
                             QComboBox, QSlider)
from PyQt5.QtCore import QDir, Qt

from gui_components.windows import MainWindow, MenuButton
from gui_components.widgets.filesystem import FileSystemViewer
from gui_components.widgets.line_editor import LineEditor
from gui_components.widgets.content_box import ContentBox

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    #main_window.setWindowTitle("")

    line_editor_content = ContentBox()

    line_editor_widget = LineEditor("example/example_line.json", line_editor_content)

    main_window.add_content_widget(line_editor_content)

    fs_widget = FileSystemViewer(QDir.currentPath())

    # compose testwidget
    cb = QCheckBox("Test")
    led = QLineEdit("test")
    sp = QSpinBox()
    rb = QRadioButton("TEst")
    cbox = QComboBox()
    cbox.addItems(["test1", "test2", "test3"])

    slider = QSlider()
    slider.setOrientation(Qt.Horizontal)
    slider.setRange(0, 100)
    slider.setValue(50)
    # set hand cursor
    slider.setCursor(Qt.PointingHandCursor)

    test_layout = QVBoxLayout()
    test_layout.addWidget(cb)
    test_layout.addWidget(QLabel("Home"))
    test_layout.addWidget(led)
    test_layout.addWidget(sp)
    test_layout.addWidget(rb)
    test_layout.addWidget(slider)
    test_layout.addWidget(cbox)

    fs_widget_content_widget = QWidget()
    fs_widget_content_widget.setLayout(test_layout)

    # add widgets to main window menu
    main_window.add_navigation_widgets([line_editor_widget, fs_widget])
    main_window.add_content_widgets([line_editor_content, fs_widget_content_widget])

    # add buttons with associated widgets
    main_window.add_menu_button(
        MenuButton("", menu_widget=fs_widget, content_widget=fs_widget_content_widget, icon_url="/collection 1/16x16/icon_1_16x16_76.png"), selected=True
    )
    main_window.add_menu_button(
        MenuButton("", menu_widget=line_editor_widget, content_widget=line_editor_content, icon_url="/collection 1/16x16/icon_2_16x16_59.png"),
                                selected=False,
    )

    # w.setStyleSheet(get_stylesheets()[0])

    logger.debug("Test")

    sys.exit(app.exec())
