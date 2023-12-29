import logging as lg
from datetime import datetime
from flask_login import UserMixin
from Flask_server import db, app


class Companie(db.Model):
    __tablename__ = "Companie"

    companie_siret = db.Column(db.Integer, primary_key=True, nullable=False)

    name = db.Column(db.String(50), nullable=False, unique=True)
    
    adress = db.Column(db.String())
    
    phone = db.Column(db.String(20), default="")
    
    logo = db.Column(db.String(255))
    
    description = db.Column(db.String())

    def __init__(self, companie_siret, name, adress, phone, logo, description):
        self.companie_siret = companie_siret
        self.name = name
        self.adress = adress
        self.phone = phone
        self.logo = logo
        self.description = description

class People(db.Model, UserMixin):
    __tablename__ = "People"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    
    username = db.Column(db.String(50), nullable=False, unique=True)
    
    password = db.Column(db.String(50), nullable=False)
    
    email = db.Column(db.String(50), unique=True)
    
    companie_siret = db.Column(db.Integer, db.ForeignKey('Companie.companie_siret'))

    role = db.Column(db.String())

    def __init__(self, username, password, email, companie_siret, role):
        self.username = username
        self.password = password
        self.email = email
        self.companie_siret = companie_siret
        self.role = role

class Advertisement(db.Model):
    __tablename__ = "Advertisement"

    ad_id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(150), nullable=False)
    
    companie_siret = db.Column(db.Integer, db.ForeignKey('Companie.companie_siret'), nullable=False)
    
    description = db.Column(db.String())
    
    date = db.Column(db.DateTime, default=datetime.now())
    
    salary = db.Column(db.Integer)
    
    adress = db.Column(db.String())
    
    contract = db.Column(db.String(50))
    
    id = db.Column(db.Integer(), db.ForeignKey('People.id'), nullable=False)

    category = db.Column(db.String)

    def __init__(self, title, companie_siret, description, date, salary, adress, contract, id, category):
        self.title = title
        self.companie_siret = companie_siret
        self.description = description
        self.date = date
        self.salary = salary
        self.adress = adress
        self.contract = contract
        self.id = id
        self.category = category

class Application(db.Model):
    __tablename__ = "Application"

    ap_id = db.Column(db.Integer, primary_key=True)
    
    ad_id = db.Column(db.Integer, db.ForeignKey('Advertisement.ad_id'), nullable=False)
    
    id = db.Column(db.Integer, db.ForeignKey('People.id'), nullable=False)
    
    message = db.Column(db.String())

    def __init__(self, ad_id, id, message):
        self.ad_id = ad_id
        self.id = id
        self.message = message

class Cv(db.Model):
    __tablename__ = "Cv"

    cv_id = db.Column(db.Integer, primary_key=True)
    
    id = db.Column(db.Integer, db.ForeignKey('People.id'), nullable=False)
    
    diploma = db.Column(db.String())
    
    skills = db.Column(db.String())
    
    hobbies = db.Column(db.String())    
    
    phone = db.Column(db.String(20))
    
    adress = db.Column(db.String)

    def __init__(self, id, diploma, skills, hobbies, phone, adress):
        self.id = id
        self.diploma = diploma
        self.skills = skills
        self.hobbies = hobbies
        self.phone = phone
        self.adress = adress

def init_db():
    db.drop_all()
    db.create_all()

    companie1 = Companie(companie_siret=34860741700048, name="Alten", adress="40 AVENUE ANDRE MORIZET, 92513 BOULOGNE BILLANCOURT CEDEX", phone="0321806491", logo="../img/logo.jpg", description="Ceci est la description de l'entreprise Alten")
    
    db.session.add(companie1)
    
    people1 = People(username="recruteur test num1", password="password", email="email@test.com", companie_siret=34860741700048, role=None)

    people2 = People(username="chercheur test num1", password="password2", email="email_chercheur@test.com", companie_siret=None, role=None)

    people3 = People(username="admin", password="admin", email="admin@help.com", companie_siret=None, role="admin")

    db.session.add(people1)
    db.session.add(people2)
    db.session.add(people3)

    advertisement1 = Advertisement(title="Offre d'emploi", companie_siret=34860741700048, description="1 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna. Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.", date=datetime.now(), salary=1234, adress="Adresse du job", contract="CDI", id=0, category="engineering")

    advertisement2 = Advertisement(title="Offre d'emploi 2", companie_siret=34860741700048, description="2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna. Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.", date=datetime.now(), salary=2345, adress="Adresse du job", contract="CDD", id=0, category="engineering")

    advertisement3 = Advertisement(title="Offre d'emploi 3", companie_siret=34860741700048, description="3 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit. Ut velit mauris, egestas sed, gravida nec, ornare ut, mi. Aenean ut orci vel massa suscipit pulvinar. Nulla sollicitudin. Fusce varius, ligula non tempus aliquam, nunc turpis ullamcorper nibh, in tempus sapien eros vitae ligula. Pellentesque rhoncus nunc et augue. Integer id felis. Curabitur aliquet pellentesque diam. Integer quis metus vitae elit lobortis egestas. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi vel erat non mauris convallis vehicula. Nulla et sapien. Integer tortor tellus, aliquam faucibus, convallis id, congue eu, quam. Mauris ullamcorper felis vitae erat. Proin feugiat, augue non elementum posuere, metus purus iaculis lectus, et tristique ligula justo vitae magna. Aliquam convallis sollicitudin purus. Praesent aliquam, enim at fermentum mollis, ligula massa adipiscing nisl, ac euismod nibh nisl eu lectus. Fusce vulputate sem at sapien. Vivamus leo. Aliquam euismod libero eu enim. Nulla nec felis sed leo placerat imperdiet. Aenean suscipit nulla in justo. Suspendisse cursus rutrum augue. Nulla tincidunt tincidunt mi. Curabitur iaculis, lorem vel rhoncus faucibus, felis magna fermentum augue, et ultricies lacus lorem varius purus. Curabitur eu amet.", date=datetime.now(), salary=3456, adress="Adresse du job", contract="CDI/CDD", id=0, category="engineering")

    db.session.add(advertisement1)
    db.session.add(advertisement2)
    db.session.add(advertisement3)

    application1 = Application(ad_id=1, id=2, message="Application message")
    application2 = Application(ad_id=2, id=2, message="Application message2")  

    db.session.add(application1)
    db.session.add(application2)

    Cv1 = Cv(id=2, diploma="Master", skills='Mes skills', hobbies='Mes hobbies', phone="0606060606", adress="124 bis route de la feuille, Lille")
    
    db.session.add(Cv1)
    
    db.session.commit()
    lg.warning('Database initialized!')