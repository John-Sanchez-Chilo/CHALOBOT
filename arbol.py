class MatrizTree():
    def __init__(self,cabeza):
        self.rows=1#esto significa que el padre de todos se encuentra en el nivel 1 y fila 1 para el usuario
        self.columns=1#no se si servira por el momento
        self.matriz=[[cabeza]]
    def addNode(self,Node,row,column):
        if(row+1>self.rows):
            helper=[]
            self.matriz.append(helper)
            self.rows+=1

        con=0
        temp=self.matriz[row-1]#no para el programador
        for j in range (column):
            con+=temp[j].sons

        self.matriz[row].insert(con,Node)
        self.matriz[row-1][column-1].sons+=1
    def getSons(self,answer):#devuelve una lista con las preguntas de los hijos
        sons=[]#almacenar las preguntas de los hijos
        con=0#se encuentras a  la izquierda  del hijo o padre
        fathernivel=0#nivel del padre del q buscamos
        numberSons=0#numeros de hijos del padre q buscamos
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j].respuesta==answer:
                    fathernivel=i
                    numberSons=self.matriz[i][j].sons
                    for k in range(j):
                        con+=self.matriz[i][k].sons
        for i in range(numberSons):
            sons.append(self.matriz[fathernivel+1][i+con].pregunta)
        return sons
    
    def getLinkByAnswer(self,answer):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j].respuesta==answer:
                    return self.matriz[i][j].link
        return None



    def print(self):
        for i in range(self.rows):
            if len(self.matriz[i])==0:
                print("[vacio]")
            else:
                for j in self.matriz[i]:
                    print(j)


class Node():
    def __init__(self, pregunta,respuesta,link):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.link=link
        self.sons=0#numero de hijos q tiene
    def __str__(self):
        return (self.pregunta+" - "+self.respuesta)

