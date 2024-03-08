import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import resources_rc  # Import the compiled resources file

class KidneyTumorDetection(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi("Koushik\Kidney _Tumor.ui", self)

        # Connect button actions to slots
        self.upload_button.clicked.connect(self.upload_image)
        self.predict_button.clicked.connect(self.predict_image)
        self.exit_button.clicked.connect(self.close)

        # Set the background image visible
        pixmap = QPixmap(":/Images/background.jpg")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

    def upload_image(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QPixmap(fileName)
            self.preview.setPixmap(pixmap)
            self.preview.setScaledContents(True)

    def predict_image(self):
        # Check if an image has been uploaded
        if self.preview.pixmap() is None:
            QMessageBox.warning(self, "Warning", "Please upload an image before predicting.")
            return

        # Placeholder for model prediction code
        # You should replace this with your actual model prediction logic
        # For now, let's assume it sets a dummy result
        result = "Dummy Prediction"
        self.result.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KidneyTumorDetection()
    window.show()
    sys.exit(app.exec_())
