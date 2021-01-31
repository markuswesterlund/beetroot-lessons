import datetime as date
# import models
from models import version as models_version

# import models.user
from models.user import name as user_name
print("Version:", models_version)
print("User module: ", user_name)
print("Today: ", date.datetime.today())
print("Username: ", user_name)
from models import user
print(user.name, user.name1, user.name2)