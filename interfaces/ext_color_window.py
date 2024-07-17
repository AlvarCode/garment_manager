from PyQt6.QtWidgets import QColorDialog, QDialog, QMessageBox
from PyQt6.QtGui import QColor
try:
    from interfaces import color_window
except ModuleNotFoundError:
    import color_window


class EColorWindow(QDialog, color_window.Ui_AggregationColorWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hexcode.setText("#282b2b")
        self.hexcode.setReadOnly(True)
        self.current_color = QColor.fromRgb(40, 43, 43);
        self.on_saving_color = None

        # Event handlers
        self.color_picker.clicked.connect(self.show_dialog_colors)
        self.image_url.textEdited.connect(lambda: self.image_url.setText(self.image_url.text().strip()))
        self.add_btn.clicked.connect(self.save)

    def show_dialog_colors(self):
        win = QColorDialog(self)
        win.setCurrentColor(self.current_color)
        win.colorSelected.connect(self.set_color)
        win.exec()

    def set_color(self, color: QColor):
        self.current_color = color
        color = color.getRgb()
        color = f"#{format(color[0], '02X')}{format(color[1], '02X')}{format(color[2], '02X')}".lower()
        self.hexcode.setText(color)
        self.color_view.setStyleSheet(f"background-color: {color};")

    def save(self):
        if self.image_url.text() == '':
            msg_box = QMessageBox()
            msg_box.setText("Ingrese la URL de la imagen correspondiente al color")
            msg_box.exec()
            self.image_url.setFocus()
            return
        
        if self.on_saving_color != None:
            self.on_saving_color(self.hexcode.text(), self.image_url.text())
        

if __name__ == '__main__':
    import PyQt6.QtWidgets as qtw
    import sys
    app = qtw.QApplication(sys.argv)
    cw = EColorWindow()
    cw.show()
    sys.exit(app.exec())