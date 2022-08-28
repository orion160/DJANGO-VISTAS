from datetime import datetime

from variables.logic.variables_logic import get_variable
from ..models import Measurement

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(var_pk):
    variable = Measurement.objects.get(pk=var_pk)
    return variable

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = get_variable(new_var["variable"])
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.save()
    return measurement

def create_measurement(var):
    variable = get_variable(var["variable"])
    now = datetime.now()
    measurement = Measurement(variable=variable, value=var["value"], unit="unit", place=var["place"], dateTime=now)
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()