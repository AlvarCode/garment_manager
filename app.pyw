from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QTableWidget, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt
from interfaces import main, ext_color_window
import sys


class Garment:
    def __init__(self, code = "", name = "", price = 0, sizes = "", category = ""):
        self.code = code
        self.name = name
        self.price = price
        self.sizes = sizes
        self.category = category
        self.colors = []

    def add_color(self, hexcode:str, image_url:str):
        if not self.is_color(hexcode):
            self.colors.append({ "hexcode": hexcode, "image_url": image_url })
            return True
        else:
            send_message("El color ya existe para esta prenda, ingrese otro")
            return False

    def delete_color(self, hexcode:str):
        idx = self.find_color(hexcode)
        if idx > -1:
            self.colors.pop(idx)
        else:
            send_message("El color que ententa eliminar no existe")

    def is_color(self, hexcode:str):
        return True if self.find_color(hexcode) > -1 else False    

    def find_color(self, hexcode:str):
        for i in range(0, len(self.colors), 1):
            if self.colors[i]["hexcode"] == hexcode:
                return i                 
        return -1


class GarmentManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.garments = [
            Garment("HDHKD", "prenda", 15, "X S", "None"),
            Garment()
        ]
        self.current_garment = None
        self.len_current_code = 0

        self.set_current_page(0)
        self.configure_table(self.ui.garments)
        self.configure_table(self.ui.colors)
        self.load_data()
        self.ui.colors.setRowCount(0)

        # clicks event handlers
        self.ui.add_garment_btn.clicked.connect(lambda: self.set_current_page(1))
        self.ui.back_btn.clicked.connect(lambda: self.set_current_page(0))
        self.ui.save_btn.clicked.connect(self.register_garment)
        self.ui.delete_garment_btn.clicked.connect(self.delete_garment)
        self.ui.add_color_btn.clicked.connect(self.add_colors)
        self.ui.delete_color_btn.clicked.connect(self.delete_color)

        self.ui.code.textEdited.connect(self.check_garment_code_format)
        self.ui.garments.cellClicked.connect(self.select_row)
        self.ui.colors.cellClicked.connect(self.select_row)

    def set_current_page(self, idx):
        self.ui.stackedWidget.setCurrentIndex(idx)
        if idx == 1:
            self.current_garment = Garment()
            self.ui.colors.setRowCount(0)
        elif self.current_garment != None:
            self.current_garment = None

    def load_data(self):
        if len(self.garments) > 0:
            self.ui.title.setText(f"Prendas Registradas ({len(self.garments)})")
            self.ui.garments.setRowCount(len(self.garments))

            for i, garment in enumerate(self.garments):
                self.ui.garments.setItem(i, 0, self.create_table_item(garment.code))
                self.ui.garments.setItem(i, 1, self.create_table_item(garment.name))
                self.ui.garments.setItem(i, 2, self.create_table_item(garment.price))
                self.ui.garments.setItem(i, 3, self.create_table_item(garment.sizes))
                self.ui.garments.setItem(i, 4, self.create_table_item(garment.category))

    def create_table_item(self, value):
        item = QTableWidgetItem(str(value))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
        return item

    def register_garment(self):
        code = self.ui.code.text().strip()
        name = self.ui.name.text().strip()
        sizes = self.ui.sizes.text().strip()

        def error(widget:QWidget = None, message = ''):
            if message == '': send_message("Aún hay campos vac[ios]")
            else: send_message(f"{message}")
            if widget != None: widget.setFocus()

        if len(code) != 6:
            error(self.ui.code, "El código está incompleto")
        elif self.is_garment(code):
            error(self.ui.code, "Ya existe otra prenda con el mismo código")
        elif name == '':
            error(self.ui.name)
        elif sizes == '':
            error(self.ui.sizes)
        elif self.current_garment.colors == []:
            error(message=" La prenda no tiene colores")
            self.add_colors()
        else:
            self.current_garment.code = code
            self.current_garment.name = name
            self.current_garment.price = self.ui.price.value()
            self.current_garment.sizes = sizes
            self.current_garment.category = self.ui.category.currentText()

            self.garments.append(self.current_garment)

            # Cleaning
            self.ui.code.clear()
            self.ui.name.clear()
            self.ui.sizes.clear()
            self.current_garment = Garment()
            self.len_current_code = 0

    def delete_garment(self):
        i = self.ui.garments.currentRow()
        if i != -1:
            if send_message("Esta seguro de eliminar esta prenda?", "Si lo hace no habra vuelta atras"):
                self.garments.pop(i)
                self.ui.garments.removeRow(i)
        else:
            send_message("Primero seleccione una fila")

    def add_colors(self):
        def add(hexcode:str, image_url:str):
            if self.current_garment.add_color(hexcode, image_url):
                self.ui.colors.insertRow(len(self.current_garment.colors) - 1)
                self.ui.colors.setItem(len(self.current_garment.colors) - 1, 0, self.create_table_item(hexcode))
                self.ui.colors.setItem(len(self.current_garment.colors) - 1, 1, self.create_table_item(image_url))
                colors_win.image_url.clear()

        colors_win = ext_color_window.EColorWindow()
        colors_win.on_saving_color = add
        colors_win.show()

    def delete_color(self):
        i = self.ui.colors.currentRow()
        if i != -1:
            self.current_garment.colors.pop(i)
            self.ui.colors.removeRow(i)
        else:
            send_message("No hay un color seleccionado para eliminar")

    def check_garment_code_format(self, text:str):
        text = text.upper().strip()

        if text != '':
            if len(text) > self.len_current_code:
                chars = ('0', '9') if len(text) > 2 else ('A', 'Z')
                if not (chars[0] <= text[len(text) - 1] <= chars[1]):
                    text = text[:len(text) - 1]
                
                if len(text) == 2: # Agregando guion separador en el código
                    text += '-'
                elif len(text) == 3 and text[2] != '-':
                    text = text[:2] + '-' + text[2]

            self.ui.code.setText(text)
        self.len_current_code = len(text)

    def is_garment(self, code:str):
        return False if self.find_garment(code) == -1 else True

    def find_garment(self, code:str):
        for i in range(len(self.garments) - 1):
            if self.garments[i].code == code:
                return i
        return -1

    def configure_table(self, table:QTableWidget):
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        table.horizontalHeader().setFixedHeight(30)
        table.verticalHeader().setFixedWidth(20)

    def select_row(self, row:int, column:int): 
        self.sender().selectRow(row)

    def modified_list_handler(self):
        title = "Prendas Registradas"
        if len(self.garments) == 0:
            self.ui.delete_garment_btn.setEnabled(False)
        else:
            title + str(len(self.garments))
            if (len(self.garments) == 1):
                self.ui.delete_garment_btn.setEnabled(False)
        self.ui.title.setText(title)

def send_message(msg:str, info = ""):
    msg_box = QMessageBox()
    if info != "":
        msg_box.setInformativeText(info)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
    msg_box.setText(msg)
    return msg_box.exec() == QMessageBox.StandardButton.Yes


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gm = GarmentManager()
    gm.show()
    app.exec()