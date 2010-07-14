import sys 
import pycassa

def profile_update(request):
   client = pycassa.connect()
   users = pycassa.ColumnFamily(client, 'HOPE2010', 'Users')
   users.insert("test",{"test": "test", 
			"test": "test"})
