from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import apsw

database_path = "sqlite:///./test.db"
engine = create_engine(database_path, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# connect to the APSW database
apsw_conn = apsw.Connection("test.db")
