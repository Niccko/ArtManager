import sys  
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QRunnable, QThreadPool, Qt, QTimer, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtGui import QPixmap
import interface.design as design
from utilities.folder_hashing import folder_hashing
from interface.interface_utils import Runnable, PercentageWorker
import os
from utils import *
from environment import *
from pprint import pprint

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.doubles_list = []
        self.doubles_index = -1
        self.btn_source_path.clicked.connect(lambda: self.set_folder_path("source"))
        self.btn_target_path.clicked.connect(lambda: self.set_folder_path("target"))
        self.btn_compute_source.clicked.connect(lambda: self.run_task(self.compute_hashes, path_type = "source"))
        self.btn_compute_target.clicked.connect(lambda: self.run_task(self.compute_hashes, path_type = "target"))
        self.lst_doubles_src.currentRowChanged.connect(self.__get_double_info)
        self.lst_doubles_trg.currentRowChanged.connect(self.__get_double_info)
        self.tbl_doubles_info.currentItemChanged.connect(self.__update_image)

        self.percentage_worker = PercentageWorker()
        self.percentage_worker.percentageChanged.connect(self.progressBar.setValue)

    def set_folder_path(self, container_type):
        container = self.txt_source_path if container_type.lower() == "source" else self.txt_target_path
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            folders = dialog.selectedFiles()
            if folders:
                container.setText(folders[0])
            self.run_task(self.__update_meta_info, path_type = container_type)
        
    def __update_meta_info(self, path_type):
        self.lbl_status.setText(f"Loading {path_type} meta")
        path = self.txt_source_path.toPlainText() if path_type.lower() == "source" else self.txt_target_path.toPlainText()
        meta_container = self.lbl_src_meta_status if path_type.lower() == "source" else self.lbl_trg_meta_status
        fh = folder_hashing(path)
        hashes = fh.load_hashes()
        if not hashes:
            return
        meta_container.setText(f"Meta info\nCount: {len(hashes)}")

        doubles_lst = self.lst_doubles_src if path_type.lower() == "source" else self.lst_doubles_trg
        doubles_lst.clear()
        self.doubles_list = [x for x in hashes.values() if len(x)>1]
        doubles_lst.addItems([str(x) for x in self.doubles_list])
        self.lbl_status.setText("")

    def keyPressEvent(self, e):
        # отработать символ внутри поля ввода
        k = e.key()
        super().keyPressEvent(e)
        selected_file = self.tbl_doubles_info.currentItem()
        if not selected_file:
            return
        os.remove(selected_file.text())
        self.__get_double_info(self.doubles_index)
        
        
    def __delete_doubles(self):
        comp_doubles = []

        for i in self.doubles_list:
            sim_list = calculate_similarity([x.path for x in i])
            for j in sim_list:
                if j[2] < SIMILARITY_THRESHOLD and j[0] not in comp_doubles:
                    comp_doubles.append(j[0])
        pprint(comp_doubles)

    def __get_double_info(self, item_index):
        self.doubles_index = item_index
        self.tbl_doubles_info.setRowCount(0)
        ind = 0
        if len(self.doubles_list) < item_index - 1:
            return
        for file in self.doubles_list[item_index]:
            if not os.path.exists(file.path):
                continue
            self.tbl_doubles_info.insertRow(ind)
            self.tbl_doubles_info.setItem(ind, 0, QtWidgets.QTableWidgetItem(file.path))
            self.tbl_doubles_info.setItem(ind, 1, QtWidgets.QTableWidgetItem(f"{file.res[0]}x{file.res[1]}"))
            ind+=1

    def __update_image(self, item):
        if not item:
            return
        pxp = QPixmap(item.text()).scaled(self.lbl_image.width(), self.lbl_image.height(), aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl_image.setPixmap(pxp)


    def compute_hashes(self, path_type):
        self.lbl_status.setText(f"Updating {path_type}")
        path = self.txt_source_path.toPlainText() if path_type.lower() == "source" else self.txt_target_path.toPlainText()
        if not path:
            self.lbl_status.setText(f"{path_type} path is not specified")
            return
        fh = folder_hashing(path)
        self.percentage_worker.start_task(fh.invalidate_hashes)
        self.__update_meta_info(path_type)
        self.lbl_status.setText("")

    def run_task(self, task, **kwargs):
        pool = QThreadPool.globalInstance()
        runnable = Runnable(task, **kwargs)
        pool.start(runnable)

     

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main() 