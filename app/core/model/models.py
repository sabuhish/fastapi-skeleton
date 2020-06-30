from app.factory.db_setup  import Model, BOOLEAN,Integer,String,DateTime, Column



class Test(Model):
    
    __tablename__= "test"

    status  = Column(BOOLEAN,default=False)
  
