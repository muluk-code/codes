import pydocumentdb

ENDPOINT = ""
MASTERKEY = ""
CONNECTION = ""
DEFAULT_DB = ""
DEFAULT_COLL = ""
SEP = "_________________________________________________________________________________________________"
SEP2 = "	_______________________________________________________"
dict_test= {
          }
list_dict_test=[
       ]
def conection(opt):
	def test():
		con = "NOMBRE CONNECCION PRUEBA"
		print(str(con))
    ENDPOINT = 'Ruta Endpoint coneccion test'
		MASTERKEY = 'Master Key coneccion test'
		DEFAULT_DB = 'Base de Datos coneccion test'
		DEFAULT_COLL = 'Colección coneccion test'
		diccon = {"ENDPOINT":'',"MASTERKEY":'',"CONNECTION":""}
		diccon['ENDPOINT'] = ENDPOINT
		diccon['MASTERKEY'] = MASTERKEY
		diccon['DEFAULT_DB'] = DEFAULT_DB
		diccon['DEFAULT_COLL'] = DEFAULT_COLL
		diccon['CONNECTION'] = str(con)
		return diccon
	def coneccion1():
		con = "NOMBRE CONNECCION 1"
		print(str(con))
		ENDPOINT = 'Ruta Endpoint coneccion 1'
		MASTERKEY = 'Master Key coneccion 1'
		DEFAULT_DB = 'Base de Datos coneccion 1'
		DEFAULT_COLL = 'Colección coneccion 1'
		diccon = {"ENDPOINT":'',"MASTERKEY":'',"CONNECTION":""}
		diccon['ENDPOINT'] = ENDPOINT
		diccon['MASTERKEY'] = MASTERKEY
		diccon['DEFAULT_DB'] = DEFAULT_DB
		diccon['DEFAULT_COLL'] = DEFAULT_COLL
		diccon['CONNECTION'] = str(con)
		return diccon
	def coneccion2():
		con = "NOMBRE CONNECCION 2"
		print(str(con))
		ENDPOINT = 'Ruta Endpoint coneccion 2'
		MASTERKEY = 'Master Key coneccion 2'
		DEFAULT_DB = 'Base de Datos coneccion 2'
		DEFAULT_COLL = 'Colección coneccion 2'
		diccon = {"ENDPOINT":'',"MASTERKEY":'',"CONNECTION":""}
		diccon['ENDPOINT'] = ENDPOINT
		diccon['MASTERKEY'] = MASTERKEY
		diccon['DEFAULT_DB'] = DEFAULT_DB
		diccon['DEFAULT_COLL'] = DEFAULT_COLL
		diccon['CONNECTION'] = str(con)
		return diccon
	connection_op = {"0":test,"1":coneccion1,"2":coneccion2}
	return connection_op[opt]

#Configuración -> cambiar número de opcion segun diccionario -connection_op- para adecuar la conección deseada
end = conection("2")
dict_connect = end()
ENDPOINT = dict_connect['ENDPOINT']
MASTERKEY = dict_connect['MASTERKEY']
CONNECTION = dict_connect['CONNECTION']
DEFAULT_COLL = dict_connect['DEFAULT_COLL']
DEFAULT_DB = dict_connect['DEFAULT_DB']
