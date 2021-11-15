import database.dbInfo as dbInfo
import mysql.connector

def createConnector():
    return mysql.connector.connect(
        host=dbInfo.host,
        user=dbInfo.user,
        password=dbInfo.password,
        database=dbInfo.database,
        port=dbInfo.port,
        collation=dbInfo.collation
    )


def getAllVinhTest():
    mydb = createConnector()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('SELECT * FROM `vinh_test`')
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult


def setNewLinkGroup(linkGroup):
    mydb = createConnector()
    mycursor = mydb.cursor()
    sql = "INSERT INTO groupReport (linkGroup, `status`) VALUES (%s, %s)"
    val = (linkGroup, "Pre-pending")
    mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
    return True


def status(x):
    switcher = {
        0: 'Pre-pending',
        1: 'Pending',
        2: 'True',
        3: 'False'
    }
    return switcher.get(x, "nothing")


def statusKey(x):
    switcher = {
        'Pre-pending': 0,
        'Pending': 1,
        'True': 2,
        'False': 3
    }
    return switcher.get(x, "nothing")


def modifyLinkGroup(idGroup, st, idUser):
    st = status(st)
    mydb = createConnector()
    mycursor = mydb.cursor()
    sql = "UPDATE groupReport SET status = %s, idUser = %s, reviewTime = NOW() WHERE id = %s"
    val = (st, idUser,idGroup)
    mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
    return True


def getPending():
    mydb = createConnector()
    mycursor = mydb.cursor()

    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM groupReport WHERE status = 'Pending' or status = 'Pre-pending'")
    myresult = mycursor.fetchall()

    mydb.close()
    return myresult


def getUser(username, password):
    mydb = createConnector()
    mycursor = mydb.cursor(dictionary=True)
    sql = 'SELECT * FROM `user` WHERE username = %s and password = %s'
    val = (username, password)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        mydb.close()
        return 0

    mydb.close()
    return myresult[0].get("id")

def getAllPost(id):
    mydb = createConnector()
    mycursor = mydb.cursor(dictionary=True)
    sql = 'SELECT content FROM dataML WHERE idGroup = %s'
    val = (id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    mydb.close()
    return myresult

def addSummary(id, content):
    mydb = createConnector()
    mycursor = mydb.cursor()
    sql = 'UPDATE groupReport SET summary = %s, status = "Pending" WHERE id = %s'
    val = (content, id)
    mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
    return True

def getIdGroup(status):
    mydb = createConnector()
    mycursor = mydb.cursor()
    sql = 'SELECT gr.id FROM groupReport gr WHERE gr.status = %s'
    val = (status, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    mydb.close()
    return myresult

def getReviewedGroup():
    mydb = createConnector()
    mycursor = mydb.cursor(dictionary=True)
    sql = 'SELECT gr.id, gr.linkgroup, gr.status, user.username, gr.reviewTime FROM groupReport gr JOIN user ON user.id = gr.idUser Limit 10'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    mydb.close()
    return myresult

def getInfoReview(idGroup):
    mydb = createConnector()
    mycursor = mydb.cursor(dictionary=True)
    sql = 'SELECT dataML.linkUser, dataML.linkFull FROM groupReport gr JOIN dataML ON dataML.idGroup = gr.id WHERE gr.id = %s AND dataML.linkUser IS NOT NULL AND dataML.linkFull IS NOT NULL'
    val = (idGroup, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    mydb.close()
    return myresult