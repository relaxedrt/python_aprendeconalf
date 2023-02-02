#https://medium.com/@simone.b/how-to-communicate-with-a-siemens-plc-using-python-3c9c6789d543
import snap7
from snap7 import util
#Creamos el cliente de conexión al plc
client = snap7.client.Client()
#Introducimos la ip del plc
client.connect("192.168.0.1",0,0)
#Checkeamos la conexión, nos devolvera true si estamos conectados
client.get_connected()
#Leemos los datos del DB1 del byte 0 al 3 (Primera doble palabra)
db = client.db_read(1,0,3)
#Leemos el real que hay en esta primera doblepalabra
t = util.get_real(db, 0)
#Leemos el primer booleano que hay en esta primera doble palabra
b = util.get_bool(db,0,0)
print(t)

