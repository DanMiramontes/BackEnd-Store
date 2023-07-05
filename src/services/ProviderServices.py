from src.database.db import connetcion_DB
from src.models.Providers import Providers


class ProviderServices():
    @classmethod
    def index_provider(cls):
            try:
                connection = connetcion_DB()
                providers = []
                with connection.cursor() as cursor:
                    cursor.execute('call store.sp_index_providers()')
                    resultset = cursor.fetchall()
                    for row in resultset:
                         provider = Providers(name=str(row[1]),full_address=str(row[2]),id=int(row[0]),created_at=str(row[3]))
                         providers.append(provider.to_json())
                connection.close()
                return providers
            except:
                 return None
    @classmethod
    def show_provider(cls,id): 
            try: 
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_show_provider(%s)',(id))
                    row = cursor.fetchall()[0]
                    provider = Providers(name=str(row[1]),full_address=str(row[2]),id=int(row[0]),created_at=str(row[3]))
                    result  = provider.to_json()
                conection.close()
                return result
            except:
                 return None

    @classmethod       
    def create_provider(cls,provider): 
            try: 
                name = provider.name[0]
                full_address = provider.full_address

                print(name,full_address)
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_create_providers(%s, %s)',(name,full_address))
                    row = cursor.fetchall()
                    conection.commit()
                conection.close()
                if row is True:
                     return True
                else: 
                     return None
            except:
                 return None
    
    @classmethod       
    def update_provider(cls,id,provider): 
            try: 
                name = provider.name[0]
                full_address = provider.full_address

                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_update_provider(%s,%s,%s);',(id,name, full_address))
                    row = cursor.fetchall()
                    conection.commit()
                conection.close()
                if row is True:
                     return True
                else: 
                     return None
            except:
                 return None
    
    @classmethod       
    def delete_provider(cls,id): 
            try: 
                conection = connetcion_DB()
                with conection.cursor() as cursor:
                    cursor.execute('call store.sp_delete_provider(%s)',(id))
                    row = cursor.fetchall()
                    conection.commit()
                conection.close()
                if row is True:
                     return True
                else: 
                     return None
            except:
                 return None
    