from application import app, db
from application.models import Pilot, Ship, PilotShip, AddPilotForm, AddShipForm, AddPilotShipForm
from flask import render_template, redirect, url_for, request

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_pilot', methods=['GET', 'POST'])
def add_pilot():
    form = AddPilotForm()
    if form.validate_on_submit():
        new_pilot = Pilot(name=form.name.data, combat_level=form.combat_level.data)
        db.session.add(new_pilot)
        db.session.commit()
        return render_template('index.html', message="Pilot Added!")
    else:
        return render_template('add_pilot.html', form=form)

@app.route('/pilots')
def pilots():
    pilots = Pilot.query.all()
    return render_template('pilots.html', pilots=pilots)

@app.route('/add_ship', methods=['GET', 'POST'])
def add_ship():
    form = AddShipForm()
    if form.validate_on_submit():
        new_ship = Ship(make=form.make.data, model=form.model.data)
        db.session.add(new_ship)
        db.session.commit()
        return render_template('index.html', message="Ship Added!")
    else:
        return render_template('add_ship.html', form=form)

@app.route('/ships')
def ships():
    ships = Ship.query.all()
    return render_template('ships.html', ships=ships)

@app.route('/add_pilot_ship', methods=['GET', 'POST'])
def add_pilot_ship():
    form = AddPilotShipForm()
    ship = request.form.get('ship_id')
    pilot = request.form.get('pilot_id')
    if form.validate_on_submit():
        new_pilot_ship = PilotShip(ship_name=form.ship_name.data, ship_id=ship, pilot_id=pilot, armament_rating=form.armament_rating.data, skin=form.skin.data)
        db.session.add(new_pilot_ship)
        db.session.commit()
        return render_template('index.html', message="Pilots Ship Added!")
    else:
        return render_template('add_pilot_ship.html', form=form)
    
@app.route('/ship_by_pilot/<int:id>')
def ship_by_pilot(id):
    ships = db.session.query(PilotShip).filter_by(pilot_id=id).all()
    context = db.session.query(Pilot).get(id)
    name = context.name
    return render_template('ship_by_pilot.html', ships=ships, name=name)

@app.route('/update_pilot/<name1>', methods=['GET', 'POST'])
def update_pilot(name1):
    form = AddPilotForm()
    pilot = Pilot(name=name1)

    return render_template('update_pilot.html', pilot=pilot, form=form)


@app.route('/update_pilot2/<old>', methods=['GET', 'POST'])
def update_pilot2(old):
    updated_pilot = db.session.query(Pilot).filter_by(name=old).first()
    # if request.form.get('name'):
    updated_pilot.name = request.form.get('name')
    updated_pilot.combat_level = request.form.get('combat_level')
    db.session.commit()
    return redirect('/pilots')
    # else:
    #     return redirect('/')

@app.route('/update_ship/<make>/<model>', methods=['GET', 'POST'])
def update_ship(make, model):
    form = AddShipForm()
    ship = Ship(make=make, model=model)

    return render_template('update_ship.html', ship=ship, form=form)

@app.route('/update_ship2/<make>/<model>', methods=['GET', 'POST'])
def update_ship2(make, model):
    updated_pilot = db.session.query(Ship).filter_by(make=make, model=model).first()
    # if request.form.get('make'):
    updated_pilot.make = request.form.get('make')
    updated_pilot.model = request.form.get('model')
    db.session.commit()
    return redirect('/ships')
    # else:
    #     return redirect('/')

# @app.route('/update_pilot_ship/<make>/<model>', methods=['GET', 'POST'])
# def update_pilot_ship(make, model):
#     form = AddShipForm()
#     ship = Ship(make=make, model=model)
#     if Ship:
#         return render_template('update_pilot_ship.html', ship=ship, form=form)
#     else:
#         return redirect('/pilots')

# @app.route('/update_pilot_ship2/<make>/<model>', methods=['GET', 'POST'])
# def update_pilot_ship2(make, model):
#     updated_pilot = db.session.query(Ship).filter_by(make=make, model=model).first()
#     if request.form.get('make'):
#         updated_pilot.make = request.form.get('make')
#         updated_pilot.model = request.form.get('model')
#         db.session.commit()
#         return redirect('/pilots')
#     else:
#         return redirect('/')

@app.route('/delete_pilot/<name>')
def delete_pilot(name):
    deleted_pilot = db.session.query(Pilot).filter_by(name=name).first()
    if deleted_pilot:
        db.session.delete(deleted_pilot)
        db.session.commit()
        return redirect('/pilots')
    else:
        return redirect('/pilots')

@app.route('/delete_ship/<make>/<model>')
def delete_ship(make, model):
    deleted_ship = db.session.query(Ship).filter_by(make=make, model=model).first()
    if deleted_ship:
        db.session.delete(deleted_ship)
        db.session.commit()
        return redirect('/ships')
    else:
        return redirect('/ships')

@app.route('/delete_pilot_ship/<int:id>')
def delete_pilot_ship(id):
    deleted_ship = db.session.query(PilotShip).filter_by(id=id).first()
    if deleted_ship:
        db.session.delete(deleted_ship)
        db.session.commit()
        return render_template('index.html', message="Pilots Ship Deleted!")
    else:
        return redirect('/pilots')