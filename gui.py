from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from main import download_playlist  # main.py에서 download_playlist 함수 임포트

class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.url_entry = QLineEdit()
        self.path_button = QPushButton("...")
        self.path_button.setFixedSize(23, 25)
        self.download_button = QPushButton("Download")
        self.path_label = QLabel()

        self.init_ui()

    def init_ui(self):
        
        layout = QGridLayout()
        
        layout.addWidget(QLabel("Please enter URL:"), 0 ,0)
        layout.addWidget(self.url_entry ,0 ,1)
       
        # Add a button for selecting the save path.
        self.path_button.clicked.connect(self.select_path)
        layout.addWidget(self.path_button ,0 ,2)

        # Add a button for downloading.
        self.download_button.clicked.connect(self.start_download)  
        layout.addWidget(self.download_button ,1 ,0)

        # Add a label to display the selected save path.
        layout.addWidget(QLabel("Save Path:"), 2 ,0)
        layout.addWidget(self.path_label ,2 ,1)

        self.setLayout(layout)

    def start_download(self):
        url = str(self.url_entry.text())
        path = str(self.path_label.text())  # Get the selected save path.
        try:
            download_playlist(url, path)  # Pass the save path to your function.
            QMessageBox.information(None,"Success", "Download completed successfully!")
        except Exception as e:
            QMessageBox.critical(None,"Error", f"Failed to download: {str(e)}")

    def select_path(self):
        folder_selected = QFileDialog.getExistingDirectory()
        if folder_selected:
            print(folder_selected)  
            QMessageBox.information(None,"Path Selected", f"Files will be saved to: {folder_selected}")
            self.path_label.setText(folder_selected)  # Display the selected directory in the label.

def start_gui():
    app=QApplication([])
    
    application=Application()
   
    application.setWindowTitle("Playlist Downloader")  # Set window title
   
    application.show()
   
    app.exec_()

if __name__ == "__main__":
   start_gui() 
