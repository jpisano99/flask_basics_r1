__author__ = 'jpisano'
#from datetime import datetime
from my_secrets import passwords

#database configuration settings
database = dict(
    DATABASE = "cust_ref_db",
    USER     = "root",
    PASSWORD = passwords["DB_PASSWORD"],
    HOST     = "localhost"
)

#Smartsheet Config settings
# smartsheet = dict(
#     SMARTSHEET_TOKEN = passwords["SMARTSHEET_TOKEN"]
# )

#application predefined constants
app = dict(
    VERSION   = 1.0,
    GITHUB    = "{url}",
    #DOWNLOAD_FILE='Daily_Bookings_Nexus_9K-91007-test.zip',
)

