from flask import render_template, url_for, request, redirect
import json, requests
from datetime import timedelta

from Flask_server import db, app, lm
from flask_login import login_user, logout_user, login_required, current_user
from . import models

#########################################################################

# Route pour initialiser la base de données

#########################################################################

@app.route("/init")
def init_db():
    models.init_db()

    return 'Database initialisation done'


#########################################################################
#########################################################################

# GET

# 4 route API par table:

    # - /<table>                    pour récupérer toute la table
    # - /<table>/id=<id>            pour récupérer une ligne particulière
    # - /<table>/column=<column>    pour récupérer une colonne particulière
    # - /<table>/<id>/<column>      pour récupérer une donnée précise

#########################################################################
#########################################################################


#########################################################################

# Routes pour la table advertisement

#########################################################################

@app.route("/advertisement")
def get_ad():
    job_ads = models.Advertisement.query.all()
    res = []
    for ad in job_ads:
        res.append({"ad_id" : ad.ad_id , "title" : ad.title, "companie_siret" : ad.companie_siret, "description" : ad.description, "date" : str(ad.date), "salary" : ad.salary, "adress" : ad.adress, "contract" : ad.contract, "category" : ad.category})
    return json.dumps(res)

@app.route("/advertisement/column=<column>")
def get_ad_column(column):
    table = models.Advertisement.query.all()
    res = []
    for ad in table:
        if column == "date":
           res.append({f"{column}" : str(getattr(ad,column))})
        else:
            res.append({f"{column}" : getattr(ad,column)})
    return json.dumps(res)

@app.route("/advertisement/id=<id>")
def get_ad_line(id):
    table = models.Advertisement.query.all()
    for ad in table:
        if int(id) == int(ad.ad_id):
            return json.dumps({"ad_id" : ad.ad_id , "title" : ad.title, "companie_siret" : ad.companie_siret, "description" : ad.description, "date" : str(ad.date), "salary" : ad.salary, "adress" : ad.adress, "contract" : ad.contract, "category" : ad.category})
    return "No id match found"
        
@app.route("/advertisement/<id>/<column>")
def get_ad_info(id, column):
    table = models.Advertisement.query.all()
    for ad in table:
        if int(id) == int(ad.ad_id):
            return json.dumps({f"{column}" : getattr(ad,column)})
    return "Data not found"    
    
#########################################################################

# Routes pour la table people

#########################################################################


@app.route("/people", methods=['POST', 'GET'])

def get_people():
    peoples = models.People.query.all()
    res = []
    for people in peoples:
        res.append({"id" : people.id,"username" : people.username,"password" : people.password,"email" : people.email,"companie_siret" : people.companie_siret})
    return json.dumps(res)

@app.route("/people/column=<column>", methods=['POST'])
def get_people_column(column):
    table = models.People.query.all()
    res = []
    for people in table:
        res.append({f"{column}" : getattr(people,column)})
    return json.dumps(res)

@app.route("/people/id=<id>", methods=['POST'])
def get_people_line(id):
    table = models.People.query.all()
    for people in table:
        if int(id) == int(people.id):
            return json.dumps({"id" : people.id,"username" : people.username,"password" : people.password,"email" : people.email,"companie_siret" : people.companie_siret})
    return "No id match found"
        
@app.route("/people/<id>/<column>", methods=['POST'])
def get_people_info(id, column):
    table = models.People.query.all()
    for people in table:
        if int(id) == int(people.id):
            return json.dumps({f"{column}" : getattr(people,column)})
    return "Data not found"    

#########################################################################

# Routes pour la table companie

#########################################################################

@app.route("/companie")
def get_companie():
    companies = models.Companie.query.all()
    res = []
    for companie in companies:
        res.append({"companie_siret" : companie.companie_siret, "name" : companie.name, "adress" : companie.adress, "phone" : companie.phone, "logo" : companie.logo, "description" : companie.description})
    return json.dumps(res)

@app.route("/companie/column=<column>")
def get_companie_column(column):
    table = models.Companie.query.all()
    res = []
    for line in table:
        res.append({f"{column}" : getattr(line,column)})
    return json.dumps(res)

@app.route("/companie/id=<id>")
def get_companie_line(id):
    table = models.Companie.query.all()
    for companie in table:
        if int(id) == int(companie.companie_siret):
            return json.dumps({"companie_siret" : companie.companie_siret, "name" : companie.name, "adress" : companie.adress, "phone" : companie.phone, "logo" : companie.logo, "description" : companie.description})
    return "No id match found"
        
@app.route("/companie/<id>/<column>")
def get_companie_info(id, column):
    table = models.Companie.query.all()
    for companie in table:
        if int(id) == int(companie.companie_siret):
            return json.dumps({f"{column}" : getattr(companie,column)})
    return "Data not found"
    
#########################################################################

# Routes pour la table application

#########################################################################

@app.route("/application")
def get_application():
    applications = models.Application.query.all()
    res = []
    for application in applications:
        res.append({"ap_id" : application.ap_id, "ad_id" : application.ad_id,"id" : application.id, "message" : application.message})
    return json.dumps(res)

@app.route("/application/column=<column>")
def get_application_column(column):
    table = models.Application.query.all()
    res = []
    for line in table:
        res.append({f"{column}" : getattr(line,column)})
    return json.dumps(res)

@app.route("/application/id=<id>")
def get_application_line(id):
    table = models.Application.query.all()
    for application in table:
        if int(id) == int(application.ap_id):
            return json.dumps({"ap_id" : application.ap_id, "ad_id" : application.ad_id,"id" : application.id, "message" : application.message})
    return "No id match found"
        
@app.route("/application/<id>/<column>")
def get_application_info(id, column):
    table = models.Application.query.all()
    for application in table:
        if int(id) == int(application.ap_id):
            return json.dumps({f"{column}" : getattr(application,column)})
    return "Data not found"

#########################################################################

# Routes pour la table cv

#########################################################################

@app.route("/cv")
def get_cv():
    cvs = models.Cv.query.all()
    res = []
    for cv in cvs:
        res.append({"cv_id" : cv.cv_id, "id" : cv.id, "diploma" : cv.diploma,"skills" : cv.skills, "hobbies" : cv.hobbies,"phone" : cv.phone,"adress" : cv.adress})
    return json.dumps(res)

@app.route("/cv/column=<column>")
def get_cv_column(column):
    table = models.Cv.query.all()
    res = []
    for line in table:
        res.append({f"{column}" : getattr(line,column)})
    return json.dumps(res)

@app.route("/cv/id=<id>")
def get_cv_line(id):
    table = models.Cv.query.all()
    for cv in table:
        if int(id) == int(cv.cv_id):
            return json.dumps({"cv_id" : cv.cv_id, "id" : cv.id, "diploma" : cv.diploma,"skills" : cv.skills, "hobbies" : cv.hobbies,"phone" : cv.phone,"adress" : cv.adress})
    return "No id match found"
        
@app.route("/cv/<id>/<column>")
def get_cv_info(id, column):
    table = models.Cv.query.all()
    for cv in table:
        if int(id) == int(cv.cv_id):
            return json.dumps({f"{column}" : getattr(cv,column)})
    return "Data not found"


#########################################################################
#########################################################################

# POST

#########################################################################
#########################################################################


#########################################################################

# Création d'un profil

#########################################################################

@app.route("/create_account", methods=['POST'])
def new_account():
    if request.json["companie_siret"] != "None":
        new_user = models.People(username=request.json["username"], password=request.json["password"], email=request.json["email"], companie_siret=int(request.json["companie_siret"], role=None))
    else:
        new_user = models.People(username=request.json["username"], password=request.json["password"], email=request.json["email"], companie_siret=None, role=None)
    db.session.add(new_user)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"companie_siret":"None","email":"c@c.c","password":"cccc","username":"cc"}' http://localhost:5000/create_account

#########################################################################

# Création d'une entreprise

#########################################################################

@app.route("/create_companie", methods=['POST'])
def new_companie():
    new_companie = models.Companie(companie_siret=request.json["companie_siret"], name=request.json["name"], adress=request.json["adress"], phone=int(request.json["phone"]), logo=request.json["logo"], description=request.json["description"])
    db.session.add(new_companie)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"companie_siret":"34860741700048", "name":"Alten", "adress":"40 AVENUE ANDRE MORIZET, 92513 BOULOGNE BILLANCOURT CEDEX", "phone":"0321806491", "logo":"../img/logo.jpg", "description":"Ceci est la description de l'entreprise Alten"}' http://localhost:5000/create_companie

#########################################################################

# Création d'une advertisement

#########################################################################

@app.route("/create_advertisement", methods=['POST'])
def new_advertisement():
    new_advertisement = models.Advertisement(title=request.json["title"], companie_siret=int(request.json["companie_siret"]), description=request.json["description"], date=request.json["date"], salary=request.json["salary"], adress=request.json["adress"], contract=request.json["contract"], id=int(request.json["id"]), category=request.json["category"])
    db.session.add(new_advertisement)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"title":"Offre d'emploi", "companie_siret":34860741700048, "description":"Ceci est la description de l'offre d'emploi", "date":datetime.now(), "salary":1234, "adress":"Adresse du job", "contract":"CDI", "id":0, "category":"engineering"}' http://localhost:5000/create_advertisement

#########################################################################

# Création d'une application

#########################################################################

@app.route("/create_application", methods=['POST'])
def new_application():
    new_application = models.Application(ad_id=int(request.json["ad_id"]), id=int(request.json["id"]), message=request.json["message"])
    db.session.add(new_application)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"ad_id":1, "id":2, "message":"Application message"}' http://localhost:5000/create_application

#########################################################################

# Création d'un cv

#########################################################################

@app.route("/create_cv", methods=['POST'])
def new_cv():
    new_cv = models.Cv(id=int(request.json["id"]), diploma=request.json["diploma"], skills=request.json["skills"], hobbies=request.json["hobbies"], phone=int(request.json["phone"]), adress=request.json["adress"])
    db.session.add(new_cv)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"id":2, "diploma":"Master", "skills":'Mes skills', "hobbies":"Mes hobbies", "phone": "0606060607", "adress": "adresse random, Lille"}' http://localhost:5000/create_cv


#########################################################################
#########################################################################

# DELETE

#########################################################################
#########################################################################


#########################################################################

# Supression d'un profil

#########################################################################

@app.route("/delete_account", methods=['POST'])
def del_account():
    name = str(request.json["name"])
    user = models.People.query.filter_by(username=name).first()
    db.session.delete(user)
    db.session.commit()
    return "Done !"

    # curl -X POST -H "Content-Type: application/json" -d '{"name": "chercheur test num1"}' http://localhost:5000/delete_account

#########################################################################

# Supression d'une entreprise

#########################################################################

@app.route("/delete_companie", methods=['POST'])
def del_companie():
    siret = int(request.json["siret"])
    companie = models.Companie.query.filter_by(companie_siret=siret).first()
    db.session.delete(companie)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"siret": "34860741700048"}' http://localhost:5000/delete_companie

#########################################################################

# Supression d'une advertisement

#########################################################################

@app.route("/delete_advertisement", methods=['POST'])
def del_advertisement():
    id = int(request.json["id"])
    ad = models.Advertisement.query.filter_by(ad_id=id).first()
    db.session.delete(ad)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"id": "1"}' http://localhost:5000/delete_advertisement

#########################################################################

# Supression d'une application

#########################################################################

@app.route("/delete_application", methods=['POST'])
def delete_application():
    id = int(request.json["id"])
    application = models.Application.query.filter_by(ap_id=id).first()
    db.session.delete(application)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"id": "1"}' http://localhost:5000/delete_application

#########################################################################

# Supression d'un cv

#########################################################################

@app.route("/delete_cv", methods=['POST'])
def delete_cv():
    id = int(request.json["id"])
    cv = models.Cv.query.filter_by(cv_id=id).first()
    db.session.delete(cv)
    db.session.commit()
    return 'Done !'
    
    # curl -X POST -H "Content-Type: application/json" -d '{"id": "1"}' http://localhost:5000/delete_cv


#########################################################################
#########################################################################

# UPDATE

#########################################################################
#########################################################################


#########################################################################

# Update d'un profil

#########################################################################

@app.route("/update_people/<id>/<column>/<value>")
def update_people(id,column,value):
    people = models.People.query.filter_by(companie_siret=id).first()
    setattr(people,column,value)
    db.session.commit()
    return 'Done !'

#########################################################################

# Update d'une entreprise

#########################################################################

@app.route("/update_companie/<id>/<column>/<value>")
def update_companie(id,column,value):
    companie = models.Companie.query.filter_by(companie_siret=id).first()
    setattr(companie,column,value)
    db.session.commit()
    return 'Done !'

#########################################################################

# Update d'une advertisement

#########################################################################

@app.route("/update_advertisement/<id>/<column>/<value>")
def update_advertissement(id,column,value):
    advertisement = models.Advertisement.query.filter_by(ap_id=id).first()
    setattr(advertisement,column,value)
    db.session.commit()
    return 'Done !'

#########################################################################

# Update d'une application

#########################################################################

@app.route("/update_application/<id>/<column>/<value>")
def update_application(id,column,value):
    application = models.Application.query.filter_by(ap_id=id).first()
    setattr(application,column,value)
    db.session.commit()
    return 'Done !'

#########################################################################

# Update d'un cv

#########################################################################

@app.route("/update_cv/<id>/<column>/<value>")
def update_cv(id,column,value):
    cv = models.Cv.query.filter_by(cv_id=id).first()
    setattr(cv,column,value)
    db.session.commit()
    return 'Done !'


##########################################################################
#########################################################################

# Routes pour afficher des pages HTML

#########################################################################
#########################################################################


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        res={}
        req2 = request.get_data().decode().replace("'",'"')
        req = req2.replace("%40","@")
        for data in (req.split('&')):
            if str(data.split('=')[0]) != "confirm":
                res[str(data.split('=')[0])] = str(data.split('=')[1])
        if res.get('companie_siret') == None:
            res["companie_siret"] = "None"
        
        requests.post("http://127.0.0.1:5000//create_account",json=res)

        return redirect(url_for('login'))

    else :
        return render_template('signup.html')

@app.route("/signupCompany", methods=['GET', 'POST'])
def signupEnt():
    if request.method == "POST":
        return render_template('signupEntErr.html')
    else :
        return render_template('signupEnt.html')
    

#########################################################################
#########################################################################

# login manager

#########################################################################
#########################################################################

# provide login manager with load_user callback
@lm.user_loader
def load_user(id):
    return models.People.query.get(int(id))

# Logout user
@app.route('/logout')
def logout():
    logout_user()
    if current_user.is_authenticated:
        return 'Not deconnected'
    else:
        return redirect(url_for('home'))

# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():

        if request.method == "POST":

            # assign form data to variables
            username_form = request.form.get('username')
            password_form = request.form.get('password') 

            # filter User out of database through username
            user = models.People.query.filter_by(username=username_form).first()
            
            if user and user.password == password_form:
                login_user(user, remember=True, duration=timedelta(days=1))
                return redirect(url_for('home'))
            else:
                return render_template('loginErr.html')
            
        else:
            return render_template('login.html')
        
@app.route("/info_user")
@login_required
def info():
    return "id: "+str(current_user.id)+ " | username: "+str(current_user.username)+" | password: "+str(current_user.password) + " | role: " + str(current_user.role)

@app.route("/admin")
@login_required
def admin():
    if current_user.role == "admin":
        return render_template('adminpanel.html')
    else:
        return "You're not an dmin sorry"