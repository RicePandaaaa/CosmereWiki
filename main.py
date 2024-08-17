from DataTypes import character, item, material
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QScrollArea

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
        self.page_indices = {"mainPage": 0, "books": 1, "items": 2}

        # Variables to filter data
        self.category = None
        self.series = None

        # Connect home page buttons to appropriate functions
        self.booksHomeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["mainPage"]))
        self.itemHomeButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["mainPage"]))

        self.charButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["books"]))
        self.matsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["books"]))
        self.speciesButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["books"]))
        self.itemsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["books"]))
        self.keyTermsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["books"]))
        self.plotsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_indices["books"]))

    
    def init_mats(self):
        """
        Parse all the data and prepare the QPushButtons
        """
        # Directory information
        mats_directory = "_Materials/"

        # Load all the materials files
        for mat_root, _, mat_file_names in os.walk(mats_directory):
            # Search for csv files
            for mat_file_name in mat_file_names:
                # Add material category
                category = mat_root.split("/")[-1]
                if category not in self.materials:
                    self.materials[category] = {}

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
                                self.materials[category][mat_name] = {}
                                
                            self.materials[category][mat_name][row[0]] = row[1]

    def make_material_buttons(self):
        pass


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
