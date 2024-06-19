"""
-----------------------------------------------------------------------
This code is the first code I've written to learn very basics of PyQt5
-----------------------------------------------------------------------
Coder:      Talha Ahmad
Email:      talha.code92@gmail.com
Language:   Python 3.12
Dated:      19 June 2024
-----------------------------------------------------------------------
All rights are reserved - (c)
-----------------------------------------------------------------------
Tutorial:   https://www.youtube.com/watch?v=rZcdhles6vQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=1
-----------------------------------------------------------------------
"""

import PyQt5.QtWidgets as widget
import PyQt5.QtGui as gui


class MyWindow(widget.QWidget):     # Class of GUI window
    def __init__(self):
        super().__init__()

        # Window Setting
        self.setWindowTitle("My Window")        # Sets the title of the window
        self.setLayout(widget.QVBoxLayout())    # Setts vertical box layout of the window -- V for Vertical, in QVLayout

        # Label
        label = widget.QLabel("Your Name?")             # Create it
        label.setFont(gui.QFont("Forte", 25))           # Changes the font and size of text of the label
        self.layout().addWidget(label)                  # Add it to the window

        # Entry-box or Input-box
        entry = widget.QLineEdit()      # Create it
        entry.setObjectName("name")     # Set name of the object 'input'
        entry.setText("")               # Set the placeholder
        self.layout().addWidget(entry)  # Add it to the window

        def action():     # Function to change the label when button is clicked
            name = entry.text()     # Get the text from entry button
            if len(name) > 0:
                label.setText(f"Welcome {entry.text()}!")   # Set the text of label
                entry.setText("")   # Set the value of entry box
            else:
                label.setText(f"Plz enter correct name!")   # Warning

        # Button
        button = widget.QPushButton("Confirm")      # Create it
        button.clicked.connect(action)              # take action when button is clicked
        self.layout().addWidget(button)             # Add it to the window

        self.show()     # Show the window


if __name__ == '__main__':
    app = widget.QApplication([])   # Root -- app
    window = MyWindow()     # Object -- window
    app.exec_()     # Execute the app
