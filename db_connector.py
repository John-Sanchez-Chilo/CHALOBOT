import mysql.connector as sql 
from arbol import MatrizTree,Node
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize

#esto es para la limpieza

spanish=SpellChecker(language='es')

def correctSentence(text):
    newtext=""
    words=word_tokenize(text)
    for word in words:
        newtext+= spanish.correction(word)
        newtext+=" "
    return newtext
#Estas dos van juntas
#es para limpiar un texto de caracteres extraños
mapeo={
    ord('á'):'a',
    ord('é'):'e',
    ord('í'):'i',
    ord('ó'):'o',
    ord('ú'):'u',
    ord('Â'):'',
    ord('Ã'):'',
    ord('¡'):'á',
    ord('©'):'é',
    ord('Ã'):'í', 
    ord('³'):'ó',
    ord('º'):'ú', 
    ord('‘'):'Ñ',
    ord('±'):'ñ'

}

def clean(text):#aqui puede ingresar string o texto
    text=text.translate(mapeo)
    return text





db=sql.connect(
    host="localhost",
    user="root",
    passwd="admin_1572003_jesc",
    database="chatbot"
)
#id=0, fatherLevel=1, fathernumber=2, question=3,  chatbotQuestion=4, answer=5, link=6 este se usa

cursor = db.cursor()
cursor.execute("SELECT * FROM tree WHERE idtree=1")
r=cursor.fetchall()

firstNode=Node(r[0][3],r[0][5],r[0][6])#el padre de la base de datos solo debe tener
tree=MatrizTree(firstNode)

cursor.execute("SELECT * FROM tree WHERE idtree>1")
r=cursor.fetchall()


#esto es para el chat
pairs=[]

for i in r:
    
    listQuesAns=[i[4]]
    answer=[i[5]]
    listQuesAns.append(answer)
    pairs.append(listQuesAns)
    
    if i[1]>0 and i[2]>0:
        tree.addNode(Node(i[3],i[5],i[6]),i[1],i[2])

