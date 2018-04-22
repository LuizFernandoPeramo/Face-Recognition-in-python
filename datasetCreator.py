import cv2
import sqlite3

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def insertOrUpdate(Id, Nome, Sobrenome, Periodo, Professor):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * From Pessoas WHERE ID = " + str(Id) # tirar a str
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        pass
    else:
        cmd = "INSERT INTO Pessoas (ID,Nome,Sobrenome,Periodo,Professor) Values(" + str(Id) + "," + str(
            Nome) + " ," + str(Sobrenome) + "," + str(Periodo) + "," + str(Professor) + ")"
        conn.execute(cmd)
        conn.commit()
        conn.close()


Id = raw_input('Digite o id: ')
nome = raw_input('Digite o nome do Aluno: ')
Sobrenome = raw_input('Digite o sobrenome: ')
Periodo = raw_input('Digite o periodo do Aluno: ')
professor = raw_input('Digite o nome do Professor: ')
insertOrUpdate(id, nome, Sobrenome, Periodo, professor)

sampleNum = 0
cam = cv2.VideoCapture(0)
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(
        gray,
        scaleFactor=1.10,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        # incrementando o numero  de amostra
        sampleNum = sampleNum + 1
        # salvar a face capturada na pasta dataset
        cv2.imwrite("dataSet/User." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Espere por 100 miliseconds
        cv2.waitKey(100)
        cv2.imshow('AO VIVO', im)
        cv2.waitKey(10)
    # Interrompa se o numero da amostra for superior a 30
    if sampleNum > 30:
        break
cam.release()
cv2.destroyAllWindows()
