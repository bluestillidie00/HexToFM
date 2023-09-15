import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QClipboard, QTextDocument
from win32mica import ApplyMica, MicaTheme, MicaStyle
import sys
import os

class ColorConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()




    def init_ui(self):
        self.setWindowTitle("Hex to FM Colour Converter")
        self.setGeometry(100, 100, 400, 250)
        self.setWindowOpacity(60)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.color_name_label = QLabel("Color Name:")
        self.color_name_text = QLineEdit()

        self.hex_code_label = QLabel("Hex Code (e.g., #RRGGBB):")
        self.hex_code_text = QLineEdit()

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_to_xml)

        self.xml_output_label = QLabel("XML Output:")
        self.xml_output_text = QLineEdit()
        self.xml_output_text.setReadOnly(True)

        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        layout.addWidget(self.color_name_label)
        layout.addWidget(self.color_name_text)
        layout.addWidget(self.hex_code_label)
        layout.addWidget(self.hex_code_text)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.xml_output_label)
        layout.addWidget(self.xml_output_text)
        layout.addWidget(self.copy_button)

        central_widget.setLayout(layout)

    def convert_to_xml(self):
        color_name = self.color_name_text.text()
        hex_code = self.hex_code_text.text()

        try:
            rgb_value = self.convert_hex_to_rgb(hex_code)

            xml_output = f'<colour name="{color_name}" value="rgb({rgb_value})" />'
            self.xml_output_text.setText(xml_output)
        except Exception as e:
            self.xml_output_text.setText(f"Error: {str(e)}")

    @staticmethod
    def convert_hex_to_rgb(hex_code):
        hex_code = hex_code.lstrip("#")

        if len(hex_code) != 6:
            raise ValueError("Invalid hex code length. Please provide a 6-character hex code.")

        red_hex = hex_code[:2]
        green_hex = hex_code[2:4]
        blue_hex = hex_code[4:6]

        red = int(red_hex, 16)
        green = int(green_hex, 16)
        blue = int(blue_hex, 16)

        return f"{red},{green},{blue}"

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.xml_output_text.text())
        QMessageBox.information(self, "Copied", "XML Output copied to clipboard!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = ColorConverterApp()
    main_window.show()
    sys.exit(app.exec_())
