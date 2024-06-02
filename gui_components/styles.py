import pathlib

style_dark_01 = """
QWidget {
    color: #F2F2F2;
    font: 10pt "Segoe UI";
}

/* Title on top bar */
#titleRightInfo {
    padding-left: 10px;
    text-align: left;
    color: white;
    font: 8.5pt "Segoe UI";
}

#appLogo {
    background-color: #2B2D30;
    background-image: url(:/collection 2/16x16_1/cil-4k.png);
    background-position: center;
    background-repeat: no-repeat;
}

/* Top Bar */
#topBar{
    background-color: #2B2D30;
    border: 1px solid rgb(30, 31, 34);
}


/* bgApp frame */
#bgApp {
    background-color: #1E1F22;
    border-bottom: 1px solid #1E1F22;
    border-left: 1px solid #1E1F22;
    border-right: 1px solid #1E1F22;
}

/* Left Menu */
#leftMenu {
    background-color: #2B2D30;
    border-bottom: 1px solid #1E1F22;
    border-left: 1px solid #1E1F22;
    border-right: 1px solid #1E1F22;
}

#extraLeftMenuFrame {
    background-color: #2B2D30;
    border-bottom: 1px solid #1E1F22;
    border-left: 1px solid #1E1F22;
    border-right: 1px solid #1E1F22;
}


#titleLeftApp { 
    font: 63 12pt "Segoe UI Semibold"; 
}
#titleLeftDescription { 
    font: 8pt "Segoe UI";  
    color: #F2F2F2;
}

/* MENUS */
#topMenu .MenuButton {
    background-position: center;
    background-repeat: no-repeat;
    border: none;
    background-color: transparent;
    text-align: left;
    margin: 5px;
    border-radius: 5px;
}
#topMenu .MenuButton:hover {
    background-color: #505354;
}
#topMenu .MenuButton:pressed {
    background-color: #3574F0;
    color: #F2F2F2;
}
#bottomMenu .MenuButton {
    background-position: left center;
    background-repeat: no-repeat;
    border: none;
    border-left: 20px solid transparent;
    background-color:transparent;
    text-align: left;
    padding-left: 44px;
}
#bottomMenu .MenuButton:hover {
    background-color: rgb(40, 44, 52);
}
#bottomMenu .MenuButton:pressed {
    background-color: #FFC90E;
    color: #F2F2F2;
}


/* Top Buttons */
#topBarButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }
#topBarButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }
#topBarButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }


/* Bottom Bar */
#bottomBar {
    background-color: #2B2D30;
}
#bottomBar QLabel {
    font-size: 11px;
    color: rgb(113, 126, 149);
    padding-left: 10px;
    padding-right: 10px;
    padding-bottom: 2px;
}

#contentFrame QPushButton {
    border: 2px solid #343b48;
    border-radius: 5px;
    padding: 5px;
}
#contentFrame QPushButton:hover {
    background-color: rgb(57, 65, 80);
    border: 2px solid rgb(61, 70, 86);
}
#contentFrame QPushButton:pressed {
    background-color: rgb(35, 40, 49);
    border: 2px solid rgb(43, 50, 61);
}

#contentFrame QPushButton:disabled {
	border: 2px solid rgb(43, 50, 61);
	color: grey;
}


/* Tooltip */
QToolTip {
	color: #ffffff;
	background-color: rgba(33, 37, 43, 180);
	border: 1px solid rgb(44, 49, 58);
	background-image: none;
	background-position: left center;
    background-repeat: no-repeat;
	border: none;
	border-left: 2px solid  #FFC90E;
	text-align: left;
	padding-left: 8px;
	margin: 0px;
}

QProgressBar {
    border-top: 0px solid #343b48;
    border-left: 2px solid #343b48;
    border-right: 0px solid #343b48;
    border-bottom: 2px solid #343b48;
    background-color: rgb(33, 37, 43);
    text-align: right;
    margin-right: 2em;
}

QProgressBar::chunk {
    background-color: #FFC90E;
}

/* QTabWidget */
QTabWidget::pane {
	background: #2c313c;
	border-bottom-left-radius: 5px;
	border-bottom-right-radius: 5px;
	border-top-right-radius: 5px;
	border-top-left-radius: 0px;
	border: 2px solid #1E1F22;
	padding: 0px;
}

QTabBar::tab {
	background: #1E1F22;
	border: 2px solid #1E1F22;
	padding: 4px;
	padding-left: 10px;
	padding-right: 10px;
	border-top-left-radius: 5px;
    border-top-right-radius: 5px;
	margin-bottom: -3px;
}

QTabBar::tab:selected {
	background: rgb(44, 49, 58);
  	margin-bottom: -3px;
	padding: 5px;
	padding-left: 10px;
	padding-right: 10px;
	border-top-left-radius: 5px;
	border-top-right-radius: 5px;
  	border: 2px solid #1E1F22;
}

/* QTreeView */
QTreeView {
	background-color: none;
	border-radius: 5px;
	border: 1px solid #1E1F22;
}

/* QTableWidget */
QTableWidget {
	background-color: #2c313c;
	padding: 10px;
	border-radius: 5px;
	gridline-color: rgb(44, 49, 58);
	border: 1px solid #1E1F22;
}
QTableWidget::item{
	border-color: #2c313c;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: #2c313c;
}
QTableWidget::item:selected{
	background-color: #FFC90E;
}

QHeaderView {
	border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QHeaderView::section{
	background-color: #1E1F22;
	max-width: 25px;
	border: 1px solid rgb(44, 49, 58);
	border-style: none;
    border-bottom: 1px solid #2c313c;
    border-right: 1px solid #2c313c;
}
QTableWidget::horizontalHeader {
	background-color: #1E1F22;
}
QHeaderView::section:horizontal
{
    border: 1px solid #1E1F22;
	background-color: #1E1F22;
	padding: 3px;
}

QHeaderView::section:vertical
{
    border: 1px solid #2c313c;
}

/* QTableView */
QTableView {
	background-color: #2c313c;
	padding: 10px;
	border-radius: 5px;
	gridline-color: rgb(44, 49, 58);
	border: 1px solid #1E1F22;
}
QTableView::item{
	border-color: #2c313c;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: #2c313c;
}
QTableView::item:selected{
	background-color: #FFC90E;
}
QTableView::horizontalHeader {
	background-color: #1E1F22;
}
QTableView::indicator {
    border: 3px solid #343b48;
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: #2c313c;
}
QTableView::indicator:hover {
    border: 3px solid rgb(58, 66, 81);
}
QTableView::indicator:checked {
    background: 3px solid #343b48;
	border: 3px solid #343b48;
	background-image: url(:/collection 2/16x16_1/cil-check-alt.png);
}

/* LineEdit */
QLineEdit {
    background-color: #2B2D30;
    border-radius: 5px;
    border: 2px solid #1E1F22;
    padding: 5px;
    selection-color: #F2F2F2;
    selection-background-color: #214283;
}
QLineEdit:hover {
	border: 2px solid #404758;
}
QLineEdit:focus {
	border: 2px solid rgb(91, 101, 124);
}

/* QTextEdit */
QTextEdit {
    background-color: #2B2D30;
	border-radius: 5px;
	border: 2px solid #1E1F22;
	selection-color: #F2F2F2;
	selection-background-color: #FFC90E;
}

/* PlainTextEdit */
QPlainTextEdit {
	background-color: #2B2D30;
	border-radius: 5px;
	padding: 10px;
	selection-color: #F2F2F2;
	selection-background-color: #FFC90E;
}
QPlainTextEdit  QScrollBar:vertical {
    width: 8px;
 }
QPlainTextEdit  QScrollBar:horizontal {
    height: 8px;
 }
QPlainTextEdit:hover {
	border: 2px solid #404758;
}
QPlainTextEdit:focus {
	border: 2px solid rgb(91, 101, 124);
}

/* ScrollBars */
QScrollBar::handle:horizontal:hover {
    background-color: #FFC90E;
}

QScrollBar::add-line:horizontal:hover, QScrollBar::sub-line:horizontal:hover {
    background-color: #FFC90E;
}

QScrollBar::add-page:horizontal:hover, QScrollBar::sub-page:horizontal:hover {
    background-color: #FFC90E;
}

QScrollBar:horizontal {
    border: none;
    background: #343b48;
    height: 8px;
    margin: 0px 21px 0 21px;
    border-radius: 0px;
}
QScrollBar::handle:horizontal {
    background: #C88E00;
    min-width: 25px;
    border-radius: 4px
}
QScrollBar::add-line:horizontal {
    border: none;
    background: #343b48;
    width: 20px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
    border: none;
    background: #343b48;
    width: 20px;
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
     background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
     background: none;
}

 
QScrollBar:vertical {
    border: none;
    background: #343b48;
    width: 8px;
    margin: 21px 0 21px 0;
    border-radius: 0px;
}

QScrollBar::handle:vertical:hover {
    background-color: #FFC90E;
}

QScrollBar::add-line:vertical:hover, QScrollBar::sub-line:vertical:hover {
    background-color: #FFC90E;
}

QScrollBar::add-page:vertical:hover, QScrollBar::sub-page:vertical:hover {
    background-color: #FFC90E;
}

QScrollBar::handle:vertical {
    background: #C88E00;
    min-height: 25px;
    border-radius: 4px
}
 QScrollBar::add-line:vertical {
     border: none;
    background: #343b48;
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }
 QScrollBar::sub-line:vertical {
	border: none;
    background: #343b48;
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }
 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
     background: none;
 }

 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
     background: none;
 }

/* CheckBox */
QCheckBox::indicator {
    border: 3px solid #343b48;
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: #2c313c;
}
QCheckBox::indicator:hover {
    border: 3px solid rgb(58, 66, 81);
}
QCheckBox::indicator:checked {
    background: 3px solid #343b48;
	border: 3px solid #343b48;
	background-image: url(:/collection 2/16x16_1/cil-check-alt.png);
}

QCheckBox:disabled {
	color: grey;
}

/* RadioButton */
QRadioButton::indicator {
    border: 3px solid #343b48;
	width: 15px;
	height: 15px;
	border-radius: 10px;
    background: #2c313c;
}
QRadioButton::indicator:hover {
    border: 3px solid rgb(58, 66, 81);
}
QRadioButton::indicator:checked {
    background: 3px solid rgb(94, 106, 130);
	border: 3px solid #343b48;
}

/* ComboBox */
QComboBox{
    background-color: #2B2D30;
    border-radius: 5px;
    border: 2px solid #1E1F22;
    padding: 5px;
    padding-left: 10px;
}
QComboBox:hover{
	border: 2px solid #404758;
}
QComboBox::drop-down {
	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: 25px;
	border-left-width: 3px;
	border-left-color: rgba(39, 44, 54, 150);
	border-left-style: solid;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;
	background-image: url(:/collection 2/16x16_1/cil-arrow-bottom.png);
	background-position: center;
	background-repeat: no-reperat;
 }
QComboBox QAbstractItemView {
	color:  #F2F2F2;
	background-color: #1E1F22;
	padding: 10px;
	selection-background-color: #26282E;
}

/* ComboBox */
QSpinBox{
    background-color: #2B2D30;
    border-radius: 5px;
    border: 2px solid #1E1F22;
    padding: 5px;
    padding-left: 10px;
    selection-background-color: #214283;
}
QSpinBox:hover{
	border: 2px solid #404758;
}
QSpinBox::drop-down {
	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: 25px;
	border-left-width: 3px;
	border-left-color: rgba(39, 44, 54, 150);
	border-left-style: solid;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;
	background-image: url(:/collection 2/16x16_1/cil-arrow-bottom.png);
	background-position: center;
	background-repeat: no-reperat;
 }
QSpinBox QAbstractItemView {
	color:  #FFC90E;
	background-color: #1E1F22;
	padding: 10px;
	selection-background-color: #214283;
}

QDoubleSpinBox{
	background-color: #2B2D30;
	border-radius: 5px;
	border: 2px solid #1E1F22;
	padding: 5px;
	padding-left: 10px;
}
QDoubleSpinBox:hover{
	border: 2px solid #404758;
}
QDoubleSpinBox::drop-down {
	subcontrol-origin: padding;
	subcontrol-position: top right;
	width: 25px;
	border-left-width: 3px;
	border-left-color: rgba(39, 44, 54, 150);
	border-left-style: solid;
	border-top-right-radius: 3px;
	border-bottom-right-radius: 3px;
	background-image: url(:/collection 2/16x16_1/cil-arrow-bottom.png);
	background-position: center;
	background-repeat: no-reperat;
 }
QDoubleSpinBox QAbstractItemView {
	color:  #FFC90E;
	background-color: #1E1F22;
	padding: 10px;
	selection-background-color: #214283;
}

/* Sliders */
QSlider::groove:horizontal {
    border-radius: 5px;
    height: 20px;
	margin: 0px;
	background-color: #343b48;
}
QSlider::groove:horizontal:hover {
	background-color: #373e4c;
}
QSlider::handle:horizontal {
    background-color: #C88E00;
    border: none;
    height: 20px;
    width: 15px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:horizontal:hover {
    background-color: #FFC90E;
}
QSlider::handle:horizontal:pressed {
    background-color: #FFC90E;
}

QSlider::groove:vertical {
    border-radius: 5px;
    width: 20px;
    margin: 0px;
	background-color: #343b48;
}
QSlider::groove:vertical:hover {
	background-color: #373e4c;
}
QSlider::handle:vertical {
    background-color: #C88E00;
	border: none;
    height: 20px;
    width: 15px;
    margin: 0px;
	border-radius: 5px;
}
QSlider::handle:vertical:hover {
    background-color: #FFC90E;
}
QSlider::handle:vertical:pressed {
    background-color: #FFC90E;
}

/* CommandLinkButton */
QCommandLinkButton {
	color: rgb(0, 170, 255);
	font-size: 15px;
}
QCommandLinkButton:hover {
	color: rgb(0, 170, 255);
	background-color: #2c313c;
}
QCommandLinkButton:pressed {
	color: #FFC90E;
	background-color: rgb(52, 58, 71);
}

/* QGroupBox */
QGroupBox {
    color: rgb(90, 102, 125);
	border: 1px solid #343b48;
	border-radius: 5px;
}
"""


def get_stylesheets() -> list:
    return [style_dark_01]
