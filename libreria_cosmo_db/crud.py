import crud_settings as cc
import argparse
import pydocumentdb.document_client as document_client
import styles as st
import json




def items(ID_DATABASE,ID_COLLECTION):
	CLIENT = document_client.DocumentClient(cc.ENDPOINT, {'masterKey': cc.MASTERKEY})
	ID_DATABASE = ID_DATABASE
	ID_COLLECTION = ID_COLLECTION
	DATABASE = 'dbs/'+str(ID_DATABASE)
	COLLECTION = DATABASE + '/colls/' + ID_COLLECTION
	DOCUMENTS = ""
	DB = ""
	OPTION = ""
	OPTION2 = ""
	list_dict_test=[]
	dict_test={}
	#OBJECT = cc.dict_test
	#LIST_OBJECT = cc.list_dict_test
	OBJECT = cc.dict_test
	LIST_OBJECT = cc.list_dict_test
	PATH_OBJECT = ""
	cont_update_items = 0

#DATABASES___________________________________________________________________________
def read_database(self):
	db_query = "select * from r where r.id = '{0}'".format(ID_DATABASE)
	#db_query = "select {'web':r.['Web']} as bgh from r where r.id = '{0}'".format(DOCUMENTDB_DATABASE)
	db = CLIENT.QueryDatabases(db_query)
	print ("DATABASE")
	print ('ObjDB:\n\t{a}\n\nTypeObjDB:\n\t{}'.format(a=db,b=str(type(db))))
	db_link = db
	return db_link

def create_db(ID_DB):
	DB = CLIENT.CreateDatabase({'id': ID_DB})
	return DB
#DATABASES___________________________________________________________________________


#COLLECTIONS___________________________________________________________________________
def read_collection(self):
	DATABASE = read_database()
	collection_query = "select * from r where r.id = '{0}'".format(ID_COLLECTION)
	#coll_query = "select * from r"
	COLLECTION = list(CLIENT.QueryCollections(DATABASE, collection_query))[0]
	print ("COLLECTION")
	print (COLLECTION)
	COLLECTION_RES = COLLECTION['0']
	return COLLECTION_RES

def read_collections(self):
	COLLECTIONS = list(CLIENT.ReadCollection(DATABASE))
	print ("COLLECTION")
	print (COLLECTIONS)
	COLLECTIONS_RES = COLLECTIONS['0']
	return COLLECTIONS_RES

def create_collection(DOCUMENTDB_COLLECTION):
	DB = CLIENT.ReadDatabase(DATABASE)
	options = {
	'offerEnableRUPerMinuteThroughput': True,
	'offerVersion': "V2"
	#'offerThroughput': 400
	}
	COLLECTION = CLIENT.CreateCollection(DB['0'], {'id': DOCUMENTDB_COLLECTION}, options)
	return COLLECTION
#COLLECTIONS___________________________________________________________________________


##DOCUMENTS_______________________________________________________________________
def query_documents(query):
	COLLECTION = read_collection()
	#docs_query = "select * from r"
	documents_query = str(query)
	DOCUMENTS_RES = list(CLIENT.QueryDocuments(COLLECTION, documents_query))
	print ("DOCUMENTS")
	print (str(DOCUMENTS_RES))
	len_documents_res = len(DOCUMENTS_RES)
	if int(len_documents_res) > 0:
		for item_docs in DOCUMENTS_RES:
			iidq = str(str(item_docs['id']).strip())
			if iidq != "":
				#print(item_docs)
				print("Item Id:\n"+item_docs['id']+"\n\nItem Properties:\n"+item_docs)
	else:
		DOCUMENTS_RES = None
	return DOCUMENTS_RES

def search_document_id(id_doc):
	COLLECTION = read_collection()
	document_search = "select * from r.id = '{0}'".format(id_doc)
	#docs_query = str(query)
	SEARCH = list(CLIENT.QueryDocuments(COLLECTION, document_search))[0]
	print ("DOCUMENTS")
	print ("RESULTS:\n"+str(SEARCH_RES))
	len_search_res = len(SEARCH_RES)
	print ("COLLECTION")
	print (coll)
	SEARCH_RES = SEARCH['0']
	return SEARCH_RES

def read_documents(self):
	#do_l = read_collection()
	#print(do_l[0]['id'])
	#COLLECTION = CLIENT.ReadCollection(COLLECTION)
	#docs_query = "select * from r"
	#DOCUMENTS = COLLECTION+ '/docs/'
	DOCUMENTS_RES= list(CLIENT.ReadDocuments(COLLECTION))
	#coll_query = "select * from r"
	#CLIENT.ReadDocument(client,'SalesOrder1')
	len_documents_list = len(DOCUMENTS_RES)
	if int(len_documents_list) > 0:
		print(str(cc.SEP))
		for item_documents_list in DOCUMENTS_RES:
			iird = str(str(item_documents_list['id']).strip())
			if iird != "":
				print(str(cc.SEP2))
				print("Item Id:\n"+str(item_documents_list['id'])+"\n\nItem Properties:\n"+str(item_documents_list))
		
	else:
		DOCUMENTS_RES = None
	print(str(cc.SEP))
	return DOCUMENTS_RES

def update_document(self):
	COLLECTION = read_collection()
	CLIENT.UpsertDocument(COLLECTION,OBJECT)
	print("Updated:\n"+str(OBJECT))
	print("READ.............................................DB")
	read_documents()
	print("READ..............................................END")
def update_documents(self):
	cont_update_items = 0
	print("UPDATED MASIVE PROCESS")
	def udoc(OBJ):
		cont_update_items += 1
		OBJECT = OBJ 
		update_document()
		print("Send Item: "+str(OBJ)+" Update\nItem: "+str(cont_update_items))
	UPDATE_LIST_ITEMS = list(map(udoc, LIST_OBJECT))
	print("len items update"+str(len(UPDATE_LIST_ITEMS)))
def create_document(OBJECT):
	COLLECTION = read_collection()
	CLIENT.CreateDocument(COLLECTION,OBJECT)
	print("READ.............................................DB")
	read_documents()
	print("READ..............................................END")
##DOCUMENTS_______________________________________________________________________
#ANALIZER = argparse.ArgumentParser(description='CRUD AZURE-COSMOS_DB PROCESS')
		#menu Argument
		#ANALIZER_GROUP = ANALIZER.add_mutually_exclusive_group()

		#Cosmo DB variables
def readdocs(ID_DATABASE,ID_COLLECTION):
	items(ID_DATABASE,ID_COLLECTION)
	print("READ.............................................DB")
	resu = read_documents()
	print("READ..............................................END")
	return	resu

#Validate Argument values 


	



#Menu_______________________________________________________________
	
#MENU__________________________________________________________________________________________________



		

if __name__ == '__main__':
	inicio()
