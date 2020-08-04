import heapq
import random

def dijkstra(_map, start, end) :
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



place = ['b15', 'b16', 'b2', 'b4', 'b10', 'b18']
# b15 : PC방, b16 : 노래방, b2 : 빵집, b4 : 음식점, b10 : 편의점, b18 : 공원
# a1 : 회재 집, a7 : 접촉자 집, b21 : 연구실

pick_place = random.sample(place, 1)

mymap = {
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

Contact_path = dijkstra(mymap, 'a7', pick_place[0])
My_path = dijkstra(mymap, 'a1', 'b21')

print("Contact Path :" , Contact_path)
print("My Path :" , My_path)

for [pos, time] in Contact_path :
    if [pos, time] in My_path :
        print("Contact! I will recommend another way")  
        del mymap[pos]
        for _pos in mymap.values() :
            if pos in _pos :
                del _pos[pos]

Recommend_path = dijkstra(mymap, 'a1', 'b21')

print("Recommend Path :" , Recommend_path)

# 결과 예시
#Contact Path : [['a7', 0], ['a14', 10], ['a21', 20], ['b7', 30], ['b14', 40], ['b13', 50], ['b12', 60], ['b11', 70], ['b10', 80]]
#My Path : [['a1', 0], ['a2', 10], ['a3', 20], ['a10', 30], ['a17', 40], ['b3', 50], ['b10', 60], ['b11', 70], ['b12', 80], ['b13', 90], ['b14', 100], ['b21', 110]]
#Contact! I will recommend another way
#Recommend Path : [['a1', 0], ['a2', 10], ['a3', 20], ['a10', 30], ['a11', 40], ['a12', 50], ['a19', 60], ['b5', 70], ['b12', 80], ['b13', 90], ['b14', 100], ['b21', 110]]