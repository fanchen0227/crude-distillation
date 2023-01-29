# Crude Distillation

When blending two different kinds of oil together, each of the oil's properties (e.g.: sulphur content, density, etc.) are combined via specific rules. One property of particular importance is the Distillation Profile; usually given as a table or a chart of the form:

05% : 45°C
10% : 95°C
20% : 101°C
30% : 140°C
40% : 179°C
50% : 210°C
60% : 225°C
70% : 260°C
80% : 310°C
90% : 330°C
95% : 360°C
99% : 381°C

What this represents is the temperature in °C at which X % of the oil has evaporated; e.g.: for the above table, 50% of the oil has evaporated at 210°C.
In essence, this is a discrete snapshot of a function that takes in percentage, and returns the temperature.

The goal of the project is to create a model which will give an pproximate distillation profile of the mixture of the two oils with specific volumes.

## Methdology

The project is collecting the data from Crude Monitor, covering the 61 crudes of XXX sample profiles from 2013 Jan to 2023 Jan. The crude profile include basic analysis, light ends and simulated distillation. [Here]() is the data exploration profile report.

The idea is to train a ML model to predict the distillation profile based on the feature of basic analysis and light ends. We built the 61 crudes' profile based on the latest sample data. Then we built a function that calculated the features of the mixture based on physical properties. 

With the calculated features of mixture, we can predict the distillation profile. 

## Assumption & Simplification:
### Distillation prediction
1. The stimulated distillation from crude monitor is the actual distillation profile for the crude. The accuracy of the stimulated distillation will affect our model accuracy since we use stimulation as dependent variable.
2. The feature of basic analysis and light ends are sufficient enough to predict the distillation profile. No other features will be added due to availability
3. The purpose of the model is to predict. We don't pay to much on model interpretability.
### Feature calculation of Physical properties
1. The volume of mixture is the sum of the volumes of two crudes. 
2. Gravity of the mixture can be calculated based on the volume.

## Modelling

Y(dependent variable) is the tempareture.
X(independent variable) is the features including: 'Absolute Density (kg/m3)', 'Gravity (&degAPI)', 'Sulphur (wt%)', 'MCR (wt%)', 'Sediment (ppmw)', 'TAN (mgKOH/g)', 'Salt (ptb)', 'Nickel (mg/kg)', 'Vanadium (mg/kg)','C1 Methane (vol%)', 'C2 Ethane (vol%)', 'C3 Propane (vol%)', 'iC4 iso-Butane (vol%)', 'nC4 n-Butane (vol%)',
 'iC5 iso-Pentane (vol%)', 'nC5 n-Pentane (vol%)', 'C6 Hexanes (vol%)', 'C7 Heptanes (vol%)', 'C8 Octanes (vol%)', 'C9 Nonanes (vol%)', 'C10 Decanes (vol%)', '%mass'

training set : testing set = : = 7:3

The random forest model with maximum depth of 12 and 200 estimators is the champion of trained models. Cross validation of hyper-parameter tuning is used for model selection and prevent overfitting. 

The performance in the test set is

Mean absolute error (MAE): 11.004878737436725

Root mean sqaure error (RMSE): 16.138275060676385

R square (r2): 0.9931326280807293

![feature_importance](docs/images/feature.png)

## Deployment

The trained random forest model is compressed and output as a joblib file. The model, crudes profile and feature function in src folder were zipped and deployed in [google cloud function](https://cloud.google.com/functions). We can call the API by using the url that contains crude variables to get the distillation profile line chart of the mixture.

https://northamerica-northeast1-durable-cacao-374303.cloudfunctions.net/crude?name1={name1}&volume1={volume1}&name2={name2}&volume2={volume2}
    
    Args:
        name1: the name of the crude 1. The upper case matters.
        volume1: the volume of the crude 1 added - unit liters.
        name2: the name of the crude 2. The upper case matters.
        volume2: the volume of the crude 2 added - unit liters.

Example:

If we mix 1L of Pembina and 5L of Western Canadian Select, the variables and url will be:

name1 = Pembina

volume1 = 1

name2 = Western_Canadian_Select

volume2 = 5


https://northamerica-northeast1-durable-cacao-374303.cloudfunctions.net/crude?name1=Pembina&volume1=1&name2=Western_Canadian_Select&volume2=5

![line_chart](docs/images/line_chart.png)


# Future Improvment
1. For some crude(eg.[Light Smiley](https://crudemonitor.ca/crudes/crude.php?acr=MSY)), when the mass% receovered reaches some point(eg. 95%), the residule won't further decrease. In this case, the temperature after that points cannot be predicted and should be null. We can build a model to predict what crude will have what threshould point to make the prediction of distillation more accurate.
2. We can try to add features (eg. BTEX) which is not available from Crude Monitor API. Check if it's improving the model.
3. Explore other ML algrithms of prediction and adjust the function of property calculation. 

