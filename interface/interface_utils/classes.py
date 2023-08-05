from PyQt5.QtCore import QRunnable, pyqtSignal, pyqtSlot, QObject
from functools import partial

class Runnable(QRunnable):
    def __init__(self, task, **kwargs):
        super().__init__()
        self.task = task
        self.kwargs = kwargs

    def run(self):
        self.task(**self.kwargs)

class PercentageWorker(QObject):
    started = pyqtSignal()
    finished = pyqtSignal()
    percentageChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._percentage = 0

    def __add__(self, other):
        if isinstance(other, float):
            self._percentage += other
            self.percentageChanged.emit(int(self._percentage))
            return self
        

    def __lt__(self, other):
        if isinstance(other, float):
            return self._percentage < other
        

    def start_task(self, callback):
        self._percentage = 0
        wrapper = partial(callback, self)
        self.launch_task(lambda: callback(self))

    @pyqtSlot(object)
    def launch_task(self, wrapper):
        wrapper()
