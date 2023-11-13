import os
from os import environ

API_ID = int(os.environ.get("API_ID", "21748181"))
API_HASH = os.environ.get("API_HASH", "b1d962414e186e0778911f3183feac33")
SESSION = os.environ.get("SESSION")
ADMINS = set(int(x) for x in os.environ.get("ADMINS", "5149183428").split())
TIME = os.environ.get("TIME", None)
GROUPS = [int(admin) for admin in environ.get("GROUPS", "-1002145133110").split()]
