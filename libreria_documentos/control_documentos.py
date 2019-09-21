import json,os,bson


class process_elements():
    def update_dict(obj='',obj_n=''):
        val_up = False
        v_obj1 = isinstance(obj_n,(dict))
        v_obj2 = isinstance(obj,(dict))
        if v_obj1 == True and v_obj2 == True:
            l_k_field = obj_n.keys()
            l_v_field = obj_n.values()
            k_obj = l_k_field[0]
            v_obj = l_v_field[0]
            v_obj2 = obj[k_obj]
            v_type = isinstance(obj_n,(type(v_obj2)))
            if v_type == True:
                obj.update({k_obj:v_obj})
                val_up = True
        return val_up

class process_doc():
    def validate_doc(self,path=''):
        val_doc = False
        if path != '':
            val_doc = os.path.isfile(path_docs)
        return val_doc
    def write_doc(self,path='',obj=''):
        w_doc = False
        v_obj = isinstance(obj,(dict))
        if path != '' and v_obj == True:
            try:
                with open(path_doc, 'w') as filew:
                    json.dump(obj, filew,indent=5)
            except:
                w_doc = False
            finally:
                w_doc = True
        return w_doc

    def write_b_doc(self,path='',obj=''):
        w_doc = False
        v_obj = isinstance(obj,(dict))
        if path != '' and v_obj == True:
            try:
                with open(path, 'wb') as filew:
                    filew.write(bson.BSON.encode(obj))
            except:
                w_doc = False
            finally:
                w_doc = True
        return 
    def read_b_doc(self,path=''):
        data = ''
        if path != '':
            try:
                with open(path, 'rb') as filer:
                    data = bson.BSON.decode(filer)
            except:
                w_doc = False
            finally:
                w_doc = True
        return data
        
    def close_doc(self,data):
        json_data.close()
    def read_doc(self,path=''):
        with open(path,'r') as json_data:
            data = json.loads(json_data)
            return data
            
    def back_doc(path_doc,new_path_doc):
        pass
