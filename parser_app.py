import base64
import itertools
import json
import traceback
from random import randint

import numpy as np
import chardet
import jellyfish
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout, QWidget, QLineEdit, QInputDialog, QDialog, \
    QDialogButtonBox, QFormLayout, QTableWidgetItem, QProgressBar, QTreeWidget, QTreeWidgetItem
from scipy.sparse import lil_matrix

from gui import Ui_MainWindow


def zied_similarity(s1, s2):
    delimiters = "/|:"
    dc = {}
    z = 0
    for delimiter in delimiters:
        char_to_count = "l"
        count1 = s1.count(delimiter)
        count2 = s2.count(delimiter)
        x = 1 if count1 == count2 else 0
        z += x

    return z / len(delimiters)


def zied_similarity2(s1, s2):
    delimiters = "/|:"
    dc = {}
    z = 0
    f = 0
    for delimiter in delimiters:
        char_to_count = "l"
        count1 = s1.count(delimiter)
        count2 = s2.count(delimiter)
        x = 1 if count1 == count2 else 0
        if count1 == count2 == 0:
            f -= 1
        z += x

    if len(delimiters) + f == 0:
        return 0
    return z / len(delimiters)


def jaccard(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)


def fuzzy_jaccard(str1, str2, threshold=90):
    # Tokenize the strings
    tokens1 = str1.split()
    tokens2 = str2.split()

    # Compute the Jaccard Index with fuzzy set intersection
    intersection = set()
    union = set()
    for token1 in tokens1:
        for token2 in tokens2:
            if jellyfish.jaro_similarity(token1, token2) >= threshold:
                intersection.add(token1)
                union.add(token1)
                union.add(token2)
    similarity = len(intersection) / len(union)

    return similarity


def centroid_string(strings, similarity_measure=jellyfish.jaro_distance):
    # Compute Jaro distance matrix
    jaro_distances = np.zeros((len(strings), len(strings)))
    for i in range(len(strings)):
        for j in range(len(strings)):
            jaro_distances[i, j] = similarity_measure(strings[i], strings[j])

    # Compute mean Jaro distance for each string
    mean_jaro_distances = np.mean(jaro_distances, axis=1)
    # Choose string with highest mean Jaro distance as centroid
    centroid_index = np.argmax(mean_jaro_distances)
    return strings[centroid_index]


MEASURES = {
    "jaro distance": jellyfish.jaro_similarity,
    "hamming distance": jellyfish.hamming_distance,
    "levenstein distance": jellyfish.levenshtein_distance,
    "zied distance": zied_similarity,
    "zied_similarity2": zied_similarity2,
    "jaccard distance": jaccard,
    "jaccard fuzzy": fuzzy_jaccard,
    "match rating comparison": jellyfish.match_rating_comparison,
}


def average_similarity(strings, algorithm='jaro distance'):
    """
    Computes the average similarity between a list of strings.
    """

    num_pairs = len(strings) * (len(strings) - 1) // 2
    total_similarity = sum(MEASURES[algorithm](a, b) for i, a in enumerate(strings) for b in strings[i + 1:])
    return total_similarity / num_pairs if num_pairs > 0 else 0.0


class AddSubstitutionDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(395, 106)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "original"))
        self.label_2.setText(_translate("Dialog", "substitute"))

    def get_input(self):
        original = self.lineEdit.text()
        substitute = self.lineEdit_2.text()
        return original, substitute


class ParserWindow(Ui_MainWindow):
    def __init__(self):
        super(ParserWindow, self).__init__()

        self.file_path = ""
        self.parser = None
        self.MainWindow = None

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        super().setupUi(MainWindow)

        self.initial_states()
        self.connect_buttons()

    def initial_states(self):

        # Create a progress bar widget
        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignRight)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setMinimum(0)

        # Create a status bar widget and add the progress bar to it
        self.statusbar.addPermanentWidget(self.progress_bar)
        self.statusbar.showMessage("Ready", 0)

        self.reloadButton.setEnabled(False)
        self.substitutionTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        for i in MEASURES:
            if i == "jaro distance":
                continue
            self.similarityMeasureCombobox.addItem(i)

        self.ClustersTreeWidget.setColumnCount(1)
        # Enable drag and drop for the tree widget
        self.ClustersTreeWidget.setDragDropMode(QTreeWidget.InternalMove)

        # Create root item
        self.rootItem = QTreeWidgetItem(self.ClustersTreeWidget, ['Root'])
        self.rootItem.setFlags(self.rootItem.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)

        self.ClustersTreeWidget.addTopLevelItem(self.rootItem)
        self.ClustersTreeWidget.expandAll()

    def connect_buttons(self):
        self.browseButton.clicked.connect(self.open_file_browser)
        self.reloadButton.clicked.connect(self.reload)

        self.addSubstitutionButton.clicked.connect(self.addSubstitution)
        self.deleteSubstitutionButton.clicked.connect(self.deleteSubstitution)
        self.saveSubstitutionsButton.clicked.connect(self.saveSubstitutions)
        self.loadSubstitutionsButton.clicked.connect(self.loadSubstitutions)
        self.applySubstitutionsButton.clicked.connect(self.applySubstitutions)
        self.computeClustersButton.clicked.connect(self.computeClusters)

        self.clustersTableWidget.cellClicked.connect(self.onClusterClick)
        self.deleteClustersButton.clicked.connect(self.onDeleteClusterClick)
        self.freezeButton.clicked.connect(self.onFreezeClick)
        self.loadClustersButton.clicked.connect(self.onLoadClustersClick)
        self.ClustersTreeWidget.itemClicked.connect(self.on_tree_item_clicked)

    def open_file_browser(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*)")
        if file_path is not None:
            self.file_path = file_path
            self.parser = Parser(self.file_path)
            self.filePathLineEdit.setText(self.file_path)
            self.plainTextEdit.setPlainText(self.parser.current_text)
            self.reloadButton.setEnabled(True)

    def reload(self):
        self.parser = Parser(self.file_path)
        self.plainTextEdit.setPlainText(self.parser.current_text)

    def addSubstitution(self):
        dialog = QtWidgets.QDialog(self.MainWindow)
        ui = AddSubstitutionDialog()
        ui.setupUi(dialog)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            original, substitute = ui.get_input()
            row_position = self.substitutionTableWidget.rowCount()
            self.substitutionTableWidget.insertRow(row_position)
            self.substitutionTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(original))
            self.substitutionTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(substitute))

    def deleteSubstitution(self):
        rows = set()
        for item in self.substitutionTableWidget.selectedItems():
            rows.add(item.row())

        for row in sorted(rows, reverse=True):
            self.substitutionTableWidget.removeRow(row)

    def getSubstitutions(self):
        data = []
        for row in range(self.substitutionTableWidget.rowCount()):
            original = self.substitutionTableWidget.item(row, 0).text()
            substitute = self.substitutionTableWidget.item(row, 1).text()
            data.append({"original": original, "substitute": substitute})

        return data

    def saveSubstitutions(self):
        # Get the file name and path using a file browser
        file_name, _ = QFileDialog.getSaveFileName(self.MainWindow, "Save File", "", "JSON Files (*.json)")

        # Convert the table data to a list of dictionaries
        data = self.getSubstitutions()

        # Save the data to a JSON file
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

    def loadSubstitutions(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self.MainWindow, "Load Table", "", "JSON Files (*.json)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as f:
                data = json.load(f)
            self.substitutionTableWidget.setRowCount(0)
            self.substitutionTableWidget.setRowCount(len(data))
            for i, row in enumerate(data):
                original_item = QTableWidgetItem(row['original'])
                substitute_item = QTableWidgetItem(row['substitute'])
                self.substitutionTableWidget.setItem(i, 0, original_item)
                self.substitutionTableWidget.setItem(i, 1, substitute_item)

    def applySubstitutions(self):
        self.parser.substitutions = self.getSubstitutions()
        self.parser.apply_substitutions()
        self.plainTextEdit.setPlainText(self.parser.current_text)

    def computeClusters(self):
        self.parser.compute_clusters(
            similarity_measure=MEASURES[self.similarityMeasureCombobox.currentText()],
            threshold=self.thresholdSpinBox.value() / 100.0,
            window=self.windowSpinBox.value(),
            offset=self.thresholdSpinBox_2.value()
        )
        self.parser.progress.connect(self.update_progress)
        self.parser.finished.connect(self.task_finished)
        self.parser.status.connect(self.update_status)
        self.parser.clusters.connect(self.update_clusters)
        self.parser.start()

    # SIGNAL HANDLERS
    def update_clusters(self):
        self.clusters = {}
        for tmp in self.parser.clustered_dict:
            # if len(cls[tmp]) > 1:
            self.clusters.update({
                tmp: self.parser.clustered_dict[tmp]
            })

        lines = self.parser.current_text.split("\n")
        lines = [f for f in lines if f.strip() != ""]

        row = 0
        self.clustersTableWidget.clearContents()
        self.clustersTableWidget.setRowCount(len(self.clusters))
        for e in self.clusters:
            self.clustersTableWidget.setItem(row, 0, QTableWidgetItem(str(e)))
            self.clustersTableWidget.setItem(row, 1, QTableWidgetItem(""))
            self.clustersTableWidget.setItem(row, 2, QTableWidgetItem(str(len(self.clusters[e]))))
            self.clustersTableWidget.setItem(row, 3, QTableWidgetItem(json.dumps(self.clusters[e])))

            sc = [lines[i] for i in self.clusters[e]]
            score = str(average_similarity(sc, algorithm=self.similarityMeasureCombobox.currentText()))
            self.clustersTableWidget.setItem(row, 4, QTableWidgetItem(score))
            row += 1

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def update_status(self, value):
        self.statusbar.showMessage(value, 0)

    def task_finished(self):
        self.thread = None
        self.statusbar.showMessage('Task finished')

    def onClusterClick(self, row, column):
        try:
            # get the data from the QTableWidget
            data = int(self.clustersTableWidget.item(row, 0).text())

            lines = self.parser.current_text.split("\n")
            lines = [f for f in lines if f.strip() != ""]

            # update the QListView with the data
            model = QtGui.QStandardItemModel()
            ls = []
            for i in self.clusters[data]:
                model.appendRow(QtGui.QStandardItem(lines[i]))
                ls.append(lines[i])

            self.centroidPlainTextEdit.setPlainText(
                centroid_string(ls, self.parser.algorithm).strip()[:self.parser.window])
            self.ExamplesListWidget.setModel(model)
        except:
            traceback.print_exc()

    def onFreezeClick(self):
        try:
            selected_rows = self.clustersTableWidget.selectionModel().selectedRows()
            self.clustersTableWidget.selectionModel().reset()

            lines_to_remove = []
            dc = {}
            for row in reversed(selected_rows):
                cluster_id = self.clustersTableWidget.item(row.row(), 0).text()
                dc.update({
                    cluster_id: json.loads(self.clustersTableWidget.item(row.row(), 3).text())
                })
                lines_to_remove += json.loads(self.clustersTableWidget.item(row.row(), 3).text())
            for row in reversed(selected_rows):
                self.clustersTableWidget.removeRow(row.row())

            lines = self.parser.current_text.split("\n")
            for prime in dc:
                indices = dc[prime]
                self.parser.frozen.update({
                    str(prime) + "_" + str(randint(0, 100)): [lines[i] for i in range(len(lines)) if i in indices]
                })

            lines = [lines[i] if i not in lines_to_remove else "" for i in range(len(lines))]
            lines = [f for f in lines if f.strip() != ""]
            self.parser.current_text = "\n".join(lines)

            self.plainTextEdit.setPlainText(self.parser.current_text)

            self.computeClusters()
        except:
            traceback.print_exc()

    def onDeleteClusterClick(self):
        try:
            selected_rows = self.clustersTableWidget.selectionModel().selectedRows()
            self.clustersTableWidget.selectionModel().reset()
            lines_to_remove = []
            for row in reversed(selected_rows):
                lines_to_remove += json.loads(self.clustersTableWidget.item(row.row(), 3).text())
            for row in reversed(selected_rows):
                self.clustersTableWidget.removeRow(row.row())
            lines = self.parser.current_text.split("\n")
            lines = [lines[i] if i not in lines_to_remove else "" for i in range(len(lines))]
            lines = [f for f in lines if f.strip() != ""]
            self.parser.current_text = "\n".join(lines)

            self.plainTextEdit.setPlainText(self.parser.current_text)

            self.computeClusters()
        except:
            traceback.print_exc()

    def onLoadClustersClick(self):
        while self.rootItem.childCount() > 0:
            child = self.rootItem.takeChild(0)
            del child

        # Add children to root item
        for child in self.parser.frozen:
            child_item = QTreeWidgetItem(self.rootItem, [child])
            # Enable drag and drop for the child items
            child_item.setFlags(child_item.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)

    def on_tree_item_clicked(self, item):
        if item.parent() is not None:
            print("Clicked item: {}".format(item.text(0)))


class Parser(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    clusters = pyqtSignal()

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.encoding = "utf-8"
        self.original_text = ""
        self.current_text = ""
        self.substitutions = []
        self.read_report()

        self.threshold = "0.9"
        self.window = "15"
        self.algorithm = jellyfish.jaro_similarity
        self.offset = 0
        self.similarity_matrix = None
        self.clustered_dict = {}
        self.frozen = {}

    def read_report(self):
        # Open the file in binary mode and read the first few bytes
        with open(self.file_path, 'rb') as f:
            raw_data = f.read(1000)

        # Detect the encoding of the file
        result = chardet.detect(raw_data)
        self.encoding = result['encoding']

        with open(self.file_path, "r", encoding=self.encoding) as f:
            self.original_text = "\n".join([f for f in f.read().split("\n") if f.strip() != ""])
            lines = self.original_text.split("\n")
            n = 500
            first_n_values = lines[:n]
            last_n_values = lines[-n:]
            lines = first_n_values + last_n_values
            self.current_text = "\n".join(lines)

            # self.current_text = "\n".join([f for f in self.original_text.split("\n") if f.strip() != ""])

    def apply_substitutions(self):
        for s in self.substitutions:
            self.current_text = self.current_text.replace(s['original'], s["substitute"])

    def compute_clusters(self, similarity_measure=jellyfish.jaro_similarity, threshold=0.9, window=15, offset=0):
        self.algorithm = similarity_measure
        self.threshold = threshold
        self.window = window
        self.offset = offset

    def run(self):

        self.status.emit(f"Listing primes")
        with open("100k.txt", "r") as f:
            primes = [int(x) for x in f.readlines()]

        lines = self.current_text.split("\n")
        lines = [f for f in lines if f.strip() != ""]
        n = len(lines)
        self.similarity_matrix = lil_matrix((n, n), dtype=float)

        k = 0
        tot = n * n
        self.status.emit(f"Computing sparse matrix")
        self.progress.emit(0)
        cluster_indices = []
        for i, j in itertools.product(range(n), range(n)):
            ln = lines[i].strip()
            ln2 = lines[j].strip()
            similarity = self.algorithm(ln[:self.window], ln2[:self.window])

            if similarity < float(self.threshold):
                similarity = 0
            self.similarity_matrix[i, j] = similarity
            self.similarity_matrix[j, i] = similarity

            k += 1
            if k % 1000:
                self.progress.emit(int(k / tot * 100))

        self.progress.emit(0)
        self.status.emit(f"Computing clusters")
        ls = []
        for i, row_data in enumerate(self.similarity_matrix.rows):
            v = 1
            for j in row_data:
                v = v * primes[j]
            if v > 1:
                ls.append(v)

        self.clustered_dict = {}

        for i, elem in enumerate(ls):
            if elem not in self.clustered_dict:
                self.clustered_dict[elem] = [i]
            else:
                self.clustered_dict[elem].append(i)

        self.clusters.emit()
        self.status.emit(f"Computing clusters finished")
        self.finished.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ParserWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
