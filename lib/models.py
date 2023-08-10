from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
engine = create_engine('sqlite:///freebies.db')
Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    company_freebies = relationship('Freebie', backref=backref('company'))

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    dev_freebies= relationship('Freebie', backref=backref('dev'))

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id= Column(Integer(), primary_key= True)
    item_name= Column(String())
    value= Column(Integer())
    dev= relationship('Dev', ForeignKey('dev.id'))
    company= relationship('Company', ForeignKey('company.id'))

    def __repr__(self): 
       return f'Freebie(id={self.id},' + \
        f'item_name={self.item_name},' + \
        f'value-{self.value})'
    

