from sqlalchemy import create_engine

CONNECTION_STRING = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
engine = create_engine(CONNECTION_STRING, echo=True, future=True)
