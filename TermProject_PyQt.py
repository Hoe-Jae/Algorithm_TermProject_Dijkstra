import heapq
import random
import sys
from copy import deepcopy
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton, QAbstractScrollArea

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        # b15 : PC방, b16 : 노래방, b2 : 빵집, b4 : 음식점, b10 : 편의점, b18 : 공원
        # a1 : 회재 집, a7 : 접촉자 집, b21 : 연구실
        self.place = ['b15', 'b16', 'b2', 'b4', 'b10', 'b18']
        
        self.mapping = {
                        'a1' : (5, 0),
                        'a2' : (5, 1),
                        'a3' : (5, 2),
                        'a4' : (5, 3),
                        'a5' : (5, 4),
                        'a6' : (5, 5),
                        'a7' : (5, 6),
                        'a8' : (4, 0),
                        'a9' : (4, 1),
                        'a10': (4, 2),
                        'a11': (4, 3),
                        'a12': (4, 4),
                        'a13': (4, 5),
                        'a14': (4, 6),
                        'a15': (3, 0),
                        'a16': (3, 1),
                        'a17': (3, 2),
                        'a18': (3, 3),
                        'a19': (3, 4),
                        'a20': (3, 5),
                        'a21': (3, 6),
                        'b1' : (2, 0),
                        'b2' : (2, 1),
                        'b3' : (2, 2),
                        'b4' : (2, 3),
                        'b5' : (2, 4),
                        'b6' : (2, 5),
                        'b7' : (2, 6),
                        'b8' : (1, 0),
                        'b9' : (1, 1),
                        'b10': (1, 2),
                        'b11': (1, 3),
                        'b12': (1, 4),
                        'b13': (1, 5),
                        'b14': (1, 6),
                        'b15': (0, 0),
                        'b16': (0, 1),
                        'b17': (0, 2),
                        'b18': (0, 3),
                        'b19': (0, 4),
                        'b20': (0, 5), 
                        'b21': (0, 6)
        }
        
        self.mymap = {
                        'a1' : {'a2': 1, 'a8': 1},
                        'a2' : {'a1':1, 'a3':1, 'a9':1},
                        'a3' : {'a2':1, 'a4':1, 'a10':1},
                        'a4' : {'a3':1,'a5':1,'a11':1},
                        'a5' : {'a4':1,'a6':1,'a12':1},
                        'a6' : {'a5':1,'a7':1,'a13':1},
                        'a7' : {'a6':1,'a14':1},
                        'a8' : {'a1':1,'a9':1,'a15':1},
                        'a9' : {'a2':1,'a8':1,'a10':1,'a16':1},
                        'a10': {'a3':1,'a9':1,'a11':1,'a17':1},
                        'a11': {'a4':1,'a10':1,'a12':1,'a18':1},
                        'a12': {'a5':1,'a11':1,'a13':1,'a19':1},
                        'a13': {'a6':1,'a12':1,'a14':1,'a20':1},
                        'a14': {'a7':1,'a13':1,'a21':1},
                        'a15': {'a8':1,'a16':1,'b1':1},
                        'a16': {'a9':1,'a15':1,'a17':1,'b2':1},
                        'a17': {'a10':1,'a16':1,'a18':1,'b3':1},
                        'a18': {'a11':1,'a17':1,'a19':1,'b4':1},
                        'a19': {'a12':1,'a18':1,'a20':1,'b5':1},
                        'a20': {'a13':1,'a19':1,'a21':1,'b6':1},
                        'a21': {'a14':1,'a20':1,'b7':1},
                        'b1' : {'a15':1,'b2':1,'b8':1},
                        'b2' : {'a16':1,'b1':1,'b3':1,'b9':1},
                        'b3' : {'a17':1,'b2':1,'b4':1,'b10':1},
                        'b4' : {'a18':1,'b3':1,'b5':1,'b11':1},
                        'b5' : {'a19':1,'b4':1,'b6':1,'b12':1},
                        'b6' : {'a20':1,'b5':1,'b7':1,'b13':1},
                        'b7' : {'a21':1,'b6':1,'b14':1},
                        'b8' : {'b1':1,'b9':1,'b15':1},
                        'b9' : {'b2':1,'b8':1,'b10':1,'b16':1},
                        'b10': {'b3':1,'b9':1,'b11':1,'b17':1},
                        'b11': {'b4':1,'b10':1,'b12':1,'b18':1},
                        'b12': {'b5':1,'b11':1,'b13':1,'b19':1},
                        'b13': {'b6':1,'b12':1,'b14':1,'b20':1},
                        'b14': {'b7':1,'b13':1,'b21':1},
                        'b15': {'b8':1,'b16':1},
                        'b16': {'b9':1,'b15':1,'b17':1},
                        'b17': {'b10':1,'b16':1,'b18':1},
                        'b18': {'b11':1,'b17':1,'b19':1},
                        'b19': {'b12':1,'b18':1,'b20':1},
                        'b20': {'b13':1,'b19':1,'b21':1},
                        'b21': {'b14':1,'b20':1}
                    }
        
    def init(self):
        
        for i in range(6):
            for j in range(7):
                self.tbMap.setItem(i, j, QTableWidgetItem())
                self.tbMap.item(i, j).setBackground(QColor(255, 255, 255))
        
        self.tbMap.setItem(0, 0, QTableWidgetItem("PC"))
        self.tbMap.setItem(0, 1, QTableWidgetItem("S"))
        self.tbMap.setItem(0, 3, QTableWidgetItem("P"))
        self.tbMap.setItem(0, 6, QTableWidgetItem("L"))
        self.tbMap.setItem(1, 2, QTableWidgetItem("C"))
        self.tbMap.setItem(2, 1, QTableWidgetItem("B"))
        self.tbMap.setItem(2, 3, QTableWidgetItem("F"))
        self.tbMap.setItem(5, 0, QTableWidgetItem("MH"))
        self.tbMap.setItem(5, 6, QTableWidgetItem("CH"))
        
        
    def initUI(self):
        
        self.tbMap = QTableWidget(self)
        self.tbMap.verticalHeader().setVisible(False)
        self.tbMap.horizontalHeader().setVisible(False)
        self.tbMap.resize(240, 145)
        self.tbMap.setRowCount(6)
        self.tbMap.setColumnCount(7)
        self.tbMap.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbMap.resizeColumnsToContents()
        self.tbMap.resizeRowsToContents()
        self.tbMap.move(10, 10)
        
        self.btnInit = QPushButton("Init", self)
        self.btnInit.resize(self.btnInit.sizeHint())
        self.btnInit.clicked.connect(self.init)
        self.btnInit.move(10, 160)
        
        self.btnStart = QPushButton("Start", self)
        self.btnStart.resize(self.btnStart.sizeHint())
        self.btnStart.clicked.connect(self.forward)
        self.btnStart.move(90, 160)
        
        self.btnClose = QPushButton("Close", self)
        self.btnClose.resize(self.btnClose.sizeHint())
        self.btnClose.clicked.connect(self.close)
        self.btnClose.move(170, 160)
        
        self.setGeometry(100, 100, 260, 190)
        self.setWindowTitle("알고리즘 프로젝트")
        self.show()
        
        self.init()
        
    def forward(self):
        
        mymap = deepcopy(self.mymap)
        
        pick_place = random.sample(self.place, 1)

        Contact_path = self.dijkstra(mymap, 'a7', pick_place[0])
        My_path = self.dijkstra(mymap, 'a1', 'b21')
        
        for [pos, time] in Contact_path :
            if [pos, time] in My_path :
                print("Contact! I will recommend another way")  
                del mymap[pos]
                for _pos in mymap.values() :
                    if pos in _pos :
                        del _pos[pos]
                        
        Recommend_path = self.dijkstra(mymap, 'a1', 'b21')    
        
        for path in Contact_path:
            r, c = self.mapping[path[0]]
            self.tbMap.item(r, c).setBackground(QColor(255, 0, 0))
            
        for path in Recommend_path:
            r, c = self.mapping[path[0]]
            self.tbMap.item(r, c).setBackground(QColor(0, 0, 255))           
        
        
    def dijkstra(self, _map, start, end):
        distances = {vertex : [float('inf'), start] for vertex in _map}
        distances[start] = [0, start]
        S = []
        heapq.heappush(S, [distances[start][0], start])

        while S :
            cur_dist, cur_vertex = heapq.heappop(S)
            if distances[cur_vertex][0] < cur_dist :
                continue
            for adjacent, weight in _map[cur_vertex].items() :
                distance = cur_dist + weight
                if distance < distances[adjacent][0] :
                    distances[adjacent] = [distance, cur_vertex]
                    heapq.heappush(S, [distance, adjacent])
        path = end
        path_out = [end]
        while distances[path][1] != start:
            path_out.append(distances[path][1])
            path = distances[path][1]
        path_out.append(start)
        path_out.reverse()

        time_check = []
        for i in range(len(path_out)) :
            time_check.append([path_out[i] , (i * 10)])
            
        return time_check
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())