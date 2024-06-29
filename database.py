from sqlalchemy import create_engine

user = "usyjg9uwry5exrbl"
password = "wf2aTSai8MRWWi9k72kf"
host = "btkti2pqypdid2flxpsz-mysql.services.clever-cloud.com"
port = 3306
dbname = "btkti2pqypdid2flxpsz"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}")


