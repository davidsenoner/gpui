import pandas as pd
import os

from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex


class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self,
                 dataframe: pd.DataFrame,
                 parent=None
                 ):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe
        self._split_v_char = None
        self._split_v_pos = None
        self._split_h_char = None
        self._split_h_pos = None
        self._enable_tooltip = None
        self._checkable_column = None
        self._split_data_type = None
        self._data_tooltip_mode = None
        self._colors = {}

    def split_vertical_header_labels(self, char: str = " ", pos: int = 0) -> None:
        """
        Split label string and use one word

        Parameters
        ----------
        char: str
            split string where char has ben found
        pos: int
            use word indexed by pos (use -1 for last split)
        """
        self._split_v_char = char
        self._split_v_pos = pos

    def split_horizontal_header_labels(self, char: str = " ", pos: int = 0) -> None:
        """
        Split label string and use one word
        :param char: split string where char has ben found
        :param pos: use word indexed by pos (use -1 for last split)
        :return: None
        """
        self._split_h_char = char
        self._split_h_pos = pos

    def split_data_type(self, type: str = "basename") -> None:
        """
        Split content data
        :param type: basename - split to basename in case of path
        :return: None
        """
        self._split_data_type = type

    def data_tooltip_mode(self, mode: str = "cell_content") -> None:
        """
        Sets the ToolTip text content to display
        :param mode:
            "cell_content" - Display's the cell content in tooltip
            "column_label" - Display's the columns head name n tooltip
            "row_label" - Display's the row content in tooltip
        :return:
        """
        self._data_tooltip_mode = mode

    def set_checkable_column(self, column: int = 0):
        self._checkable_column = column

    @property
    def data_frame(self):
        return self._dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            if self._checkable_column is not index.column():
                if self._split_data_type is not None:
                    return self.split_data(
                        str(self._dataframe.iloc[index.row(), index.column()])
                    )
                else:
                    return str(self._dataframe.iloc[index.row(), index.column()])

        elif role == Qt.CheckStateRole:
            if self._checkable_column is not None:
                if index.column() == self._checkable_column:
                    if self._dataframe.iloc[index.row(), index.column()]:
                        return Qt.Checked
                    else:
                        return Qt.Unchecked
        elif role == Qt.ToolTipRole:
            if self._data_tooltip_mode is not None:
                match self._data_tooltip_mode:
                    case "cell_content":
                        return str(self._dataframe.iloc[index.row(), index.column()])
                    case "column_label":
                        return str(self._dataframe.columns[index.column()])
                    case "row_label":
                        return str(self._dataframe.columns[index.row()])
            else:
                return ""
        elif role == Qt.BackgroundRole:
            row_index = index.row()
            if row_index in self._colors:
                return self._colors[row_index]
        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                text = str(self._dataframe.columns[section])
                if self._split_h_char is not None and self._split_h_pos is not None:
                    return text.split(self._split_h_char)[self._split_h_pos]
                else:
                    return text

            if orientation == Qt.Vertical:
                text = str(self._dataframe.index[section])
                if self._split_v_char is not None and self._split_v_pos is not None:
                    return text.split(self._split_v_char)[self._split_v_pos]
                else:
                    return text

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.CheckStateRole:
            if self._checkable_column is not None:
                if index.column() == self._checkable_column:
                    if value == 0:
                        self._dataframe.iloc[index.row(), index.column()] = False
                    else:
                        self._dataframe.iloc[index.row(), index.column()] = True

                    self.dataChanged.emit(index, index)
                    return True
                else:
                    return False
            else:
                return False
        elif role == Qt.BackgroundRole:
            self._colors[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.BackgroundRole])
            return True
        return False

    def flags(self, index):
        if index.column() == self._checkable_column and self._checkable_column is not None:
            return Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        else:
            return super().flags(index)

    def split_data(self, data: str) -> str:
        """
        Split a string to basename, usually used for path splitting
        :param data: String to split
        :return: basename of string passed
        """
        if self._split_data_type is not None:
            match self._split_data_type:
                case "basename":
                    return os.path.basename(data)
