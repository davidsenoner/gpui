from PyQt5.QtCore import QSettings, QDir


class AppSettings:

    APP_SETTINGS_FILE = 'settings.ini'

        #border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(37, 183, 188, 255), stop:0.5 rgba(85, 170, 255, 0));
    MENU_SELECTED_STYLESHEET = """
        background-color: rgb(60, 60, 60);
        """

    @classmethod
    def get_current_path(cls) -> str:
        settings = QSettings(AppSettings.APP_SETTINGS_FILE, QSettings.IniFormat)
        return settings.value("current_directory", QDir.currentPath()).__str__()

    @classmethod
    def set_current_path(cls, path: str):
        settings = QSettings(AppSettings.APP_SETTINGS_FILE, QSettings.IniFormat)
        settings.setValue("current_directory", path)