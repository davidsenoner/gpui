import sys
from pathlib import Path
import logging

from PyQt5.QtWidgets import (
    QPushButton, QGraphicsDropShadowEffect, QSizeGrip, QCheckBox,
    QMainWindow, QApplication, QWidget, QSizePolicy, QLabel, QVBoxLayout
)
from PyQt5.QtCore import QDir, QEvent, Qt, QSize, QSettings, QTimer
from PyQt5.QtGui import QIcon, QCursor, QColor

from gui_components.ui.ui_main_window import Ui_MainWindow
from gui_components.styles import get_stylesheets
from gui_components.widgets.custom_grips import CustomGrip
from gui_components.widgets.filesystem import FileSystemViewer
from gui_components.basis.settings import AppSettings

logger = logging.getLogger(__name__)


class MenuButton(QPushButton):
    def __init__(self, label: str, menu_widget: QWidget = None, content_widget: QWidget = None, icon_url: str | Path = None):
        super().__init__(label)

        self._linked_menu_widget = menu_widget
        self._linked_content_widget = content_widget

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMinimumSize(QSize(40, 40))
        self.setMaximumSize(QSize(40, 40))

        if icon_url is not None:
            self.setStyleSheet(f"background-image: url(:{icon_url});")

        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)

    def get_menu_widget(self):
        return self._linked_menu_widget

    def set_menu_widget(self, content: QWidget):
        self._linked_menu_widget = content

    def get_content_widget(self):
        return self._linked_content_widget

    def set_content_widget(self, content: QWidget):
        self._linked_content_widget = content


class MainWindow(QMainWindow):
    def __init__(
            self,
            description: str = ""
    ):
        super().__init__()

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.setWindowTitle(description)  # set custom design title
        self.setStyleSheet(get_stylesheets()[0])  # set stylesheet

        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        self.original_size = self.size()  # set default values
        self.original_pos = self.pos()  # set default values

        settings = QSettings("settings.ini", QSettings.IniFormat)
        self.move(settings.value("pos", self.pos()))

        # reopen maximized if it was maximized before closing app
        if settings.value("maximized", False) == 'true':
            self.showMaximized()
        else:
            self.resize(settings.value("size", QSize(800, 600)))

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # self._ui.bgApp.setGraphicsEffect(self.shadow)

        self.sizegrip = QSizeGrip(self._ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        self.setWindowFlags(Qt.FramelessWindowHint)

        # self.setWindowOpacity(1)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        def saveAndClose(self):
            settings.setValue("size", self.size())
            settings.setValue("maximized", self.isMaximized())
            if not self.isMaximized():
                settings.setValue("pos", self.pos())
            self.close()

        def maximize_restore(self):
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

        def double_click_close_app(event):
            if event.type() == QEvent.MouseButtonDblClick:
                saveAndClose(self)

        def double_click_maximize_restore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(80, lambda: maximize_restore(self))

        def move_window(event):
            if self.isMaximized():
                if event.screenPos().x() > self.original_size.width():
                    self.original_pos.setX(event.globalPos().x() - self.original_size.width() + 200)
                    self.original_pos.setY(0)
                else:
                    self.original_pos = self.pos()

                self.showNormal()

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        def on_release_move(event):
            if event.button() == Qt.LeftButton:
                if event.globalPos().y() == 0:
                    self.showMaximized()
                elif self.pos().y() < 0:
                    self.move(self.pos().x(), -self._ui.appMargins.contentsMargins().top())

        # signals
        self._ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())  # minimize
        self._ui.maximizeRestoreAppBtn.clicked.connect(lambda: maximize_restore(self))  # maximize/normal
        self._ui.closeAppBtn.clicked.connect(lambda: saveAndClose(self))  # close application
        self._ui.appLogo.mouseDoubleClickEvent = double_click_close_app  # close trough double click
        self._ui.titleRightInfo.mouseDoubleClickEvent = double_click_maximize_restore  # maximize/normal
        self._ui.topBarAppLogo.mouseDoubleClickEvent = double_click_maximize_restore  # maximize/normal
        self._ui.titleRightInfo.mouseMoveEvent = move_window  # move window
        self._ui.topBarAppLogo.mouseMoveEvent = move_window  # move window
        self._ui.titleRightInfo.mouseReleaseEvent = on_release_move  # move window
        self._ui.topBarAppLogo.mouseReleaseEvent = on_release_move  # move window

        self.show()  # show application

    def setWindowTitle(self, arg__1: str) -> None:
        self._ui.titleRightInfo.setText(arg__1)  # set custom design title

    def showMaximized(self) -> None:

        self.original_size = self.size()
        self.original_pos = self.pos()

        QMainWindow.showMaximized(self)
        self._ui.appMargins.setContentsMargins(0, 0, 0, 0)
        self._ui.maximizeRestoreAppBtn.setToolTip("Restore")
        self._ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/collection 1/16x16/icon_2_16x16_423.png"))
        self._ui.frame_size_grip.hide()
        self.left_grip.hide()
        self.right_grip.hide()
        self.top_grip.hide()
        self.bottom_grip.hide()

    def showNormal(self) -> None:

        self._ui.appMargins.setContentsMargins(0, 0, 0, 0)
        self._ui.maximizeRestoreAppBtn.setToolTip("Maximize")
        self._ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/collection 1/16x16/icon_2_16x16_422.png"))
        self._ui.frame_size_grip.show()
        self.left_grip.show()
        self.right_grip.show()
        self.top_grip.show()
        self.bottom_grip.show()

        self.hide()
        QMainWindow.showNormal(self)
        self.resize(self.original_size)
        self.move(self.original_pos)
        self.show()

    def add_menu_button(self, button: MenuButton, selected: bool = False) -> None:
        self._ui.topMenuLayout.addWidget(button)

        button.clicked.connect(self._update_button_style)

        if selected:
            button.clicked.emit()  # simulate a button click if default selected

    def add_navigation_widget(self, content: QWidget) -> None:
        self._ui.stackedWidget.addWidget(content)

    def add_navigation_widgets(self, contents: list[QWidget]) -> None:
        for content in contents:
            self._ui.stackedWidget.addWidget(content)

    def add_content_widget(self, content: QWidget) -> None:
        self._ui.stackedWidget_2.addWidget(content)  # add content widget to stackedWidget

    def add_content_widgets(self, contents: list[QWidget]) -> None:
        for content in contents:
            self._ui.stackedWidget_2.addWidget(content)  # add content widget to stackedWidget


    def remove_content_widget(self, content: QWidget, del_linked_button: bool = True) -> None:
        # find linked buttons, remove and delete instance if del_linked_button == True
        if del_linked_button:
            layout = self._ui.topMenuLayout  # layout containing the MenuButton's
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, MenuButton):
                    if widget.get_menu_widget() == content:
                        layout.removeWidget(widget)
                        widget.setParent(None)
                        widget.deleteLater()

        self._ui.stackedWidget.removeWidget(content)  # remove content widget from stackedWidget
        content.setParent(None)
        content.deleteLater()  # delete instance of widget

    def content_widgets(self) -> list:
        ret = []
        for i in range(self._ui.stackedWidget.count()):
            ret.append(self._ui.stackedWidget.widget(i))

        return ret

    def current_content_widget(self) -> QWidget:
        return self._ui.stackedWidget.currentWidget()

    def current_content_index(self) -> int:
        return self._ui.stackedWidget.currentIndex()

    def current_navigation_widget(self) -> QWidget:
        return self._ui.stackedWidget_2.currentWidget()

    def current_navigation_index(self) -> int:
        return self._ui.stackedWidget_2.currentIndex()

    def _update_button_style(self):

        sender = self.sender()
        if not isinstance(sender, MenuButton):
            return

        self._ui.stackedWidget.setCurrentWidget(sender.get_menu_widget())  # set extraLeftMenu stacked widget

        if sender.get_content_widget() is not None:
            self._ui.stackedWidget_2.setCurrentWidget(sender.get_content_widget())

        for button in self._ui.topMenu.findChildren(MenuButton):
            style = button.styleSheet()
            button.setStyleSheet(style.replace(AppSettings.MENU_SELECTED_STYLESHEET, ""))

        sender.setStyleSheet(sender.styleSheet() + AppSettings.MENU_SELECTED_STYLESHEET)

    def resizeEvent(self, event):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    def closeEvent(self, event):
        event.accept()

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            pass
            # print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            pass
            # print('Mouse click: RIGHT CLICK')