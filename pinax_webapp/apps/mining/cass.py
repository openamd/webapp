import pycassa
from account.models import get_badge_id

def update_user_field(user,field,value):
    try:
        client = pycassa.connect(['10.254.0.2:9160'])
        users = pycassa.ColumnFamily(client, 'HOPE2010', 'Users')
        time_ = users.insert(get_badge_id(user),{field : value})
        return time_
    except:
        return None

def update_user_fields(user,**kwargs):
    try:
        client = pycassa.connect(['10.254.0.2:9160'])
        users = pycassa.ColumnFamily(client, 'HOPE2010', 'Users')
        time_ = users.insert(get_badge_id(user),kwargs.items())
        return time_
    except:
        return None

def get_user_field(user,field):
    return get_user_fields(user,field)[get_badge_id(user)]

def get_user_fields(user,fields):
    try:
        client = pycassa.connect(['10.254.0.2:9160'])
        users = pycassa.ColumnFamily(client, 'HOPE2010', 'Users')
        return users.get(get_badge_id(user),fields)
    except:
        return None

def get_field_for_users(users,field):
    return get_fields_for_users(users,field)[get_badge_id(user)]

def get_fields_for_users(users,fields):
    try:
        client = pycassa.connect(['10.254.0.2:9160'])
        users = pycassa.ColumnFamily(client, 'HOPE2010', 'Users')
        return users.multiget(map(get_badge_id,users),fields)
    except:
        return None

def get_last_locations(user,n):
        try:
            client = pycassa.connect(['10.254.0.2:9160'])
            location_history = pycassa.ColumnFamily(client, 'HOPE2010', 'LocationHistory')
            res = location_history.get_range(row_count=n,super_column=get_badge_id(user))
            return list(res)
        except:
            return None

def get_zone(x,y,z):
    pass
