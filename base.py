from PySide6.QtWidgets import QGridLayout

class MaskLayout(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._maskGrid = [['', '', '', '', ''],
                    ['', '', '', '', ''],
                    ['', '', '', '', ''],
                    ['', '', '', '', ''],
                    ['', '', '', '', ''],
                ]
        
    def configMask(self):

        for local_ in self._maskGrid:
            for i in local_:
                print(i)
