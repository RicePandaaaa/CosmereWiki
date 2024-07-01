from DataTypes import character, item, material
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea

import csv, os, sys

class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the main window
        super(MainWindow, self).__init__()
        uic.loadUi('UI/mainUI.ui', self)
        self.setWindowTitle("CosmereWiki")

        # Initialize the data
        self.materials = {}

        self.init_mats()

        # Connect home page buttons to appropriate functions
        self.matsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Connect allomancy basic metals to appropriate functions
        self.allo_metals_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Brass.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Brass"))
        self.Bronze.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Bronze"))
        self.Copper.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Copper"))
        self.Iron.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Iron"))
        self.Pewter.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Pewter"))
        self.Steel.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Steel"))
        self.Tin.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Tin"))
        self.Zinc.clicked.connect(lambda: self.load_mat_data(self.allo_metals_text, "Zinc"))
        
        # Ensure the scroll area is set up correctly
        self.allo_metals_scroll.setWidgetResizable(True)

    def init_mats(self):
        # Directory information
        mats_directory = "_Materials/"

        # Load all the materials files
        for mat_root, _, mat_file_names in os.walk(mats_directory):
            # Search for csv files
            for mat_file_name in mat_file_names:
                if mat_file_name.endswith('.csv'):
                    file_path = os.path.join(mat_root, mat_file_name)

                    # Open the file for parsing
                    with open(file_path, mode='r', newline='', encoding='utf-8') as mat_file:
                        reader = csv.reader(mat_file, delimiter="|")
                        
                        # Parse and store data
                        mat_name = None
                        for row in reader:
                            if row[0] == "name":
                                mat_name = row[1]
                                self.materials[mat_name] = {}
                                
                            self.materials[mat_name][row[0]] = row[1]

    def load_mat_data(self, text_label, mat_name):
        """
        Change the appropriate text label to display the information for the
        desired material
        """

        # Get the data
        data = self.materials[mat_name]
        data_list = []

        # Transfer into a formatted string
        for mat_info_label in data:
            data_list.append(f"{mat_info_label.upper()}: {data[mat_info_label]}")
        data_string = "\n\n".join(data_list)

        # Set the text to be the created string
        text_label.setText(data_string)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
