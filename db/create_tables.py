from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from alembic import context
from config import DATABASE_URL


engine = create_engine(DATABASE_URL.replace("'", "") , echo=True)  # Echo=True для вывода SQL-запросов

Base = declarative_base()

class Candidates(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True)
    fio = Column(String)
    telegram_id = Column(String)
    phone_number = Column(String)
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"), unique=True)
    first_interview_questions = Column(String)
    second_interview_questions = Column(String)
    test_task = Column(String)
    title_of_vacancy = Column(String)

    vacancy = relationship("Vacancies", back_populates="candidates") # Добавили relationship
class Vacancies(Base):
    __tablename__ = "vacancies"
    id = Column(Integer, primary_key=True)
    id_hh= Column(Integer)
    title = Column(String)
    description = Column(String)
    conditions = Column(String)
    requirements = Column(String)
    responsibilities = Column(String)
    interview_questions = Column(String)
    priority = Column(String)
    test_task = Column(String)

    candidates = relationship("Candidates", back_populates="vacancy", cascade="all, delete-orphan") # Вот строка с каскадом

# Создание таблиц в базе данных
def create_tables():
    Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    create_tables()