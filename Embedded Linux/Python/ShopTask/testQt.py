import sys
import csv
import random
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Slot

filename = "shop_records.csv"
records = []
recordsFields = ['small', 'medium', 'large', 'price']
mediumPrice = 20
smallPrice = 10
largePrice = 30

with open(filename, 'w+') as csvfile: 
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
        
	# writing the fields 
	csvwriter.writerow(recordsFields) 
	
def writeToFile(records):
  	# writing the data row & could use writerows for multiple rows 
	with open(filename, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(records)

@Slot()
def small_order():
	writeToFile([1, 0, 0, smallPrice])
	

@Slot()	
def medium_order():
	writeToFile([0, 1, 0, mediumPrice])

@Slot()	
def large_order():
	writeToFile([0, 0, 1, largePrice])
	

	
app = QtWidgets.QApplication()
window = QtWidgets.QWidget()
window.setWindowTitle("Coffee")

window.setStyleSheet("background:rgb(162,123,85);")


layoutBtn = QtWidgets.QHBoxLayout()
layoutTitle = QtWidgets.QHBoxLayout()
layoutImgs = QtWidgets.QHBoxLayout()
layoutTotal = QtWidgets.QVBoxLayout()


text = QtWidgets.QLabel("Welcome to The shop!",
						alignment=QtCore.Qt.AlignHCenter)
text.setStyleSheet('color: white; font-size: 18pt; font-family: Courier;')
layoutTitle.addWidget(text)


label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignHCenter)
img = QtGui.QPixmap('sizes.jpg')
label.setPixmap(img)
label.resize(img.width(), img.height())
layoutImgs.addWidget(label)


smallButton = QtWidgets.QPushButton("Small")
smallButton.setStyleSheet("background: white")

mediumButton = QtWidgets.QPushButton("Medium")
mediumButton.setStyleSheet("background: white")

largeButton = QtWidgets.QPushButton("Large")
largeButton.setStyleSheet("background: white")


smallButton.clicked.connect(small_order)
mediumButton.clicked.connect(medium_order)
largeButton.clicked.connect(large_order)

layoutBtn.addWidget(smallButton)
layoutBtn.addWidget(mediumButton)
layoutBtn.addWidget(largeButton)

layoutTotal.addLayout(layoutTitle)
layoutTotal.addLayout(layoutImgs)
layoutTotal.addLayout(layoutBtn)

window.setLayout(layoutTotal)
window.resize(img.width(), img.height())
window.show()
sys.exit(app.exec())


