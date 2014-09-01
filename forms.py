from flask.ext.wtf import Form, Required, Length, Form, TextField, BooleanField, TextAreaField, SelectField, FileField
#from wtforms import TextField, BooleanField
from wtforms.validators import Required
from app.models import User, Town, Landlord

class NewHouseForm(Form):
    name = TextField('name', validators=[Required(), Length(min=0, max=50)])
    postcode = TextField('postcode', validators=[Required(), Length(min=0, max=10)])
    overview = TextField('overview', validators=[Required(), Length(min=0, max=300)])

    # TODO how to only show landlords from this house's town when we don't know what town yet
    _choices = [ (0, "A"), (1, "B") ]
    landlord_id =SelectField('town_id', choices=_choices, validators=[Required()])

# class NewLandlordForm(Form):
#     name = TextField('name', validators=[Required(), Length(min=0, max=50)])
#     website = TextField('postcode', validators=[Required(), Length(min=0, max=50)])
#     # TODO_this is only called on startup - if a new town is added, process must be refreshed
#     _choices=[ (town.id, town.name) for town in Town.query.all() ]
#     town_id =SelectField('town_id', choices=_choices, validators=[Required()])

# class PhotoForm(Form):
#     photo = FileField('Your photo')


