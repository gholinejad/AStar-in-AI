from tkinter import *
from PIL import Image
from time import *
import timeit
import random
# import dictionary for graph 
from collections import defaultdict
# queue using queue module 
from queue import *
import math

import sys
import gc



#garbage collection
gc.collect()

# function for adding edge to graph 
graph2 = defaultdict(list) 


def addEdge2(graph,u,v): 
	graph[u].append(v) 

# definition of function 
def generate_edges2(graph): 
	edges = [] 

	# for each node in graph 
	for node in graph: 
		
		# for each neighbour node of a single node 
		for neighbour in graph[node]: 
			
			# if edge exists then append 
			edges.append((node, neighbour)) 
	return edges





# '1' means a city
def initmap(row):
    global randx,randy
    global City_List
    global Start,Goal
    

    
    for i in range(row):
          tmp = Label(text= str(City_List[i]),image = g_icon,compound='center' )
          lab1.append(tmp)
          
    for i in range(row):
        if (i==0):
                randx.append(random.randint(200,700))
                randy.append(random.randint(100,100))
        else:
                f = True
                while(f):
                        f = False
                        trax = random.randint(0,1500)
                        tray = random.randint(0,720)
                        for k in range(len(randx)):
                                #print ('sh',i,'\tshk',k,'\tranx',randx[k],'\trany',randy[k],'\ttrax',trax,'\ttray',tray)
                                if((randx[k]-40 < trax < randx[k]+40) or (randy[k]-40 < tray < randy[k]+40)):
                                        f = True
                                        break
                randx.append(trax)
                randy.append(tray)

                addEdge2(graph2,City_List[i-1],City_List[i]) 

                w.create_line(randx[i]+25, randy[i]+25,randx[i-1]+25, randy[i-1]+25)
                
                if(i==2 ):
                        w.create_line(randx[i]+25, randy[i]+25,randx[i-2]+25, randy[i-2]+25)
                        addEdge2(graph2,City_List[i-2],City_List[i]) 

                if(i>3):
                       w.create_line(randx[i]+25, randy[i]+25,randx[i-3]+25, randy[i-3]+25)
                       addEdge2(graph2,City_List[i-3],City_List[i]) 


                w.pack(fill=BOTH, expand=1)

        lab1[i].place(x=randx[i],y=randy[i])
  











#main

#initializing       
maps = []
randx = []
randy = []
Start = ''
Goal = ''

rows = 10            #Row number


mygui = Tk()
mygui.title("A* Algorithm in AI Iran Path")
mygui.geometry("1600x900")
w = Canvas(mygui, width=1600, height=900) #Create Canvas for lines between cities in initmap func.

lab1 = [] #for each city in initmap func.

###
g_icon = PhotoImage(file="Src\\tf.png")
###

#####
City_List = ['Sari','Babol','Tehran','Amol','Nour','Royan','Neka','Kish','Babolsar','Shiraz']
CLtmp = City_List.copy()
CRL = random.sample(range(len(CLtmp)),rows)
for i in range(len(City_List)):
        City_List[i] = CLtmp[CRL.pop()]
print('Start From:',City_List[0],'\tGoal:',City_List[rows-1],'\n----------------------------------------')
Start = City_List[0]
Goal  = City_List[rows-1]
#####

initmap(rows)
mygui.update()


print('All Paths:') 
for i in range(len(generate_edges2(graph2))):
        print(generate_edges2(graph2)[i][0], '-->',generate_edges2(graph2)[i][1])
print('------------------------------------------------------------') 
        

# Initializing a queue 
open_queue = PriorityQueue()
sys.setrecursionlimit(10**6) 









def AStar():
        def calhn(node):
                global Goal,City_List
                def calDistance(x1,y1,x2,y2):  
                     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
                     return dist
                return calDistance(randx[City_List.index(node)],randy[City_List.index(node)],randx[City_List.index(Goal)],randy[City_List.index(Goal)])
        def calDistance(x1,y1,x2,y2):  
                     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
                     return dist
        global Start,Goal,City_List
        path = [[Start] for i in range(30)]
        gn = [0 for i in range(30)]
        pcount = 0
        # 0,parent 1,child
        CState = Start
        gmap = generate_edges2(graph2).copy() #make a copy from Graph State Space
        First_Time = True
        while(CState != Goal):
                #### Preparing for first time
                if(First_Time):
                   for i in range(len(gmap)):
                        tmp= []
                        if (gmap[i][0]==CState):
                                tmp = path[pcount].copy()
                                tmp.append(gmap[i][1])
                                path[pcount] = tmp
                                print('Expaded Path:   ',path[pcount])
                                hn = calhn(gmap[i][1])
                                if len(path[pcount])>1:
                                        gn[pcount] = gn[pcount] + calDistance(randx[City_List.index(path[pcount][-2])],randy[City_List.index(path[pcount][-2])],randx[City_List.index(path[pcount][-1])],randy[City_List.index(path[pcount][-1])])
                                elif len(path[pcount])==2:
                                        gn[pcount] = calDistance(randx[City_List.index(Start)],randy[City_List.index(Start)],randx[City_List.index(gmap[i][1])],randy[City_List.index(gmap[i][1])])
                                fn = gn[pcount] + hn
                                print('g(n):',int(gn[pcount]),'\th(n):',int(hn),'\tf(n):',int(fn),'\n----------')
                                open_queue.put((fn,gn[pcount],pcount))
                                pcount = pcount+1
                   First_Time = False
                ####
                else:
                        for i in range(len(gmap)):
                                tmp3= []
                                if (gmap[i][0]==CState):
                                        tmp3 = path[CPath].copy()
                                        tmp3.append(gmap[i][1])
                                        path[pcount] = tmp3
                                        print('Expaded Path:   ',path[pcount])
                                        hn = calhn(gmap[i][1])
                                        if (hn == 0):
                                                final_path = path[pcount]
                                        gn[pcount] = CG + calDistance(randx[City_List.index(path[CPath][-2])],randy[City_List.index(path[CPath][-2])],randx[City_List.index(path[CPath][-1])],randy[City_List.index(path[CPath][-1])])
                                        fn = gn[pcount] + hn
                                        print('g(n):',int(gn[pcount]),'\th(n):',int(hn),'\tf(n):',int(fn),'\n----------')
                                        open_queue.put((fn,gn[pcount],pcount))
                                        pcount = pcount+1

                open_list = list(open_queue.queue).copy()
                print('--------------------\nOpen List(Priority Queue):')
                for j in range(len(open_list)):      
                        print(j+1,'-',path[open_list[j][2]],'\tf(n)=',int(open_list[j][0]))
                o = open_queue.get()
                print('Number 1 Selected.\n------------------------------------------------------------\n------------------------------------------------------------')
                CPath = o[2]
                CState = path[CPath][-1]
                SCState = path[CPath][-2]
                CG = o[1]
                w.create_line(randx[City_List.index(CState)]+25, randy[City_List.index(CState)]+25,randx[City_List.index(SCState)]+25, randy[City_List.index(SCState)]+25,fill='red',width=2)
                w.pack(fill=BOTH, expand=1)
                sleep(1)
                mygui.update()

                


        print('\n------------------------------------------------------------','\nThe Best Path Founded:',final_path,'\n------------------------------------------------------------')
        print('All Paths That Expanded:')
        print('\n[\'',Start,'\']')
        for j in range(len(path)):
                if len(path[j])>1:
                        print(path[j])

        for j in range(len(final_path)):
             if(j>0):   
                w.create_line(randx[City_List.index(final_path[j-1])]+25, randy[City_List.index(final_path[j-1])]+25,randx[City_List.index(final_path[j])]+25, randy[City_List.index(final_path[j])]+25,fill='green',width=5)
                w.pack(fill=BOTH, expand=1)
                mygui.update()
                sleep(2)   

        

AStar()


mygui.update()








mygui.mainloop()





