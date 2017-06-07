import uuid
import sae.const
import MySQLdb


def create_card(number):
    for i in range (0,number):
        cardID = str(uuid.uuid4())
        print(cardID)
    return


def insertcode(code,table='app_mccatcivitas.showmethecode'):
    conn = MySQLdb.connect(
        host = sae.const.MYSQL_HOST,
        user = sae.connst.MYSQL_USER,
        passwd = sae.connst.MYSQL_PASS,
        port = int(sae.connst.MYSQL_PORT),
        charset = 'utf8')
    cur = conn.cursor()
    cur.execute("""insert into %s values('%s')"""%(table,code))
    conn.commit()
    cur.close()
    conn.close()

def selectCodes(table='app_mccatcivitas.showmethecode'):
    connection = MySQLdb.connect(
        host=sae.const.MYSQL_HOST,
        user=sae.const.MYSQL_USER,
        passwd=sae.const.MYSQL_PASS,
        port=int(sae.const.MYSQL_PORT),
        init_command='set names utf8')
cur = connection.cursor()
cur.execute("""select * from %s""" % (table))
result = []
rows = cur.fetchall()
for row in rows:
    result.append(str(row[0]))
return result




def cleanUp(table='app_mccatcivitas.showmethecode'):
    connection = MySQLdb.connect(
        host=sae.const.MYSQL_HOST,
        user=sae.const.MYSQL_USER,
        passwd=sae.const.MYSQL_PASS,
        port=int(sae.const.MYSQL_PORT),
        init_command='set names utf8')
    cur = connection.cursor()
    try:
        cur.execute(("""drop table %s""" % (table))
    except Exception as e:
        print e
    connection.commit()
    cur.execute("""create table %s (code char(32) not null primary key)""" % (table))
    connection.commit()
    cur.close()
    connection.close()

def Process():
    cleanUp()
    code = craete_card(10)
    for c in code:
        insertCode(c)
    result = selectCodes()
    return result


