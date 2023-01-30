from model.calculate_properties import calculate_properties

import pandas as pd
import numpy as np
import joblib
import functions_framework
from flask import render_template

# load random forest regressor model
rfg = joblib.load('model/random_forest.joblib')

# Register an HTTP function with the Functions Framework
@functions_framework.http
def predict(request):
    """
    HTTP Cloud Function that returns the html of line chart which shows the distillation profile of the mixture

    Args:
        request (flask.Request): The request object, of which the url contains the variables.
    Returns:
        The HTML of line chart and table of distillation profile.
    """
    name1 = request.args.get('name1').replace('_', ' ')
    volume1 = float(request.args.get('volume1'))
    name2 = request.args.get('name2').replace('_', ' ')
    volume2 = float(request.args.get('volume2'))
    json_y = request.args.get('json_y')
    # get the array of the phisical properies of the mixture.
    x_pred = calculate_properties(name1, volume1, name2, volume2)

    # generate the x_predict. 
    df_x_pred = pd.DataFrame([x_pred]*21)
    mass_list = list(range(0,100,5))
    mass_list.append(99)
    df_x_pred['%mass'] = np.array(mass_list).reshape(21,1)

    # predict and record the result as a dictionary for further consume
    y_predict = rfg.predict(df_x_pred)
    result = {}
    for i, mass in enumerate(mass_list):
        result[mass] = y_predict[i]

    if json_y == 'y':
        return result
    # return the html of line chart that shows the distallation profile of the mixture
    return render_template("line_chart.html",result=result, name1=name1, volume1=volume1, name2=name2, volume2=volume2)