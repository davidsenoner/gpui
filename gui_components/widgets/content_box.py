import sys
import logging
from PyQt5.QtWidgets import QTreeView, QMenu, QWidget, QVBoxLayout, QLabel


class ContentBox(QWidget):
    def __init__(self, content=None):
        super().__init__()
        self.content = content

        self.layout = QVBoxLayout()
        if content:
            self.layout.addWidget(content)
        self.setLayout(self.layout)

    def set_content(self, content):
        if self.content:
            self.layout.removeWidget(self.content)
            self.content.deleteLater()
        self.content = content
        self.layout.addWidget(content)
