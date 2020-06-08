from PyQt4 import QtCore, QtGui
import sys

def on_clicked():
    f, filter_ = QtGui.QFileDialog.getOpenFileNameAndFilter(
        parent=window,
        caption="Заголовок окна", directory=QtCore.QDir.currentPath(),
        filter="All (*);;Images (*.png *.jpg)",
        initialFilter="Images (*.png *.jpg)")
    print(f, filter_)

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtGui.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec_())