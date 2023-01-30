import pandas as pd

df_profile = pd.read_csv("data/crude_profile.csv")

def calculate_properties(name1, volume1, name2, volume2):
    """
    Function that calculates and returns the phisical properties of mixture as a dictionary

    Args:
        name1: the name of the crude 1. The upper case matters.
        volume1: the volume of the crude 1 added - unit liters.
        name2: the name of the crude 2. The upper case matters.
        volume2: the volume of the crude 2 added - unit liters.
    Returns:
        The array of the phisical properies of the mixture. (x_pred)
    """
    profile1 = df_profile[df_profile['Name']==name1].iloc[0, :].to_dict()
    profile2 = df_profile[df_profile['Name']==name2].iloc[0, :].to_dict()
    
    x_pred = {}

    # Assume the volume of the mixture is the sum of the two crude volume.
    volume = volume1 + volume2
    v_portion1 = volume1 / volume
    v_portion2 = volume2 / volume
    mass = volume1 * profile1['Absolute Density (kg/m3)'] + volume2 * profile2['Absolute Density (kg/m3)']
    m_portion1 = volume1 * profile1['Absolute Density (kg/m3)'] / mass
    m_portion2 = volume2 * profile2['Absolute Density (kg/m3)'] / mass
    
    # Calculating the phiscial properties of the mixture. (x_pred) 
    x_pred['Absolute Density (kg/m3)'] = mass / volume
    x_pred['Gravity (&degAPI)'] = v_portion1 * profile1['Gravity (&degAPI)'] + v_portion2 * profile2['Gravity (&degAPI)']
    x_pred['Sulphur (wt%)'] =  m_portion1 * profile1['Sulphur (wt%)'] + m_portion2 * profile2['Sulphur (wt%)']
    x_pred['MCR (wt%)'] =  m_portion1 * profile1['MCR (wt%)'] + m_portion2 * profile2['MCR (wt%)']
    x_pred['Sediment (ppmw)'] = m_portion1 * profile1['Sediment (ppmw)'] + m_portion2 * profile2['Sediment (ppmw)']
    x_pred['TAN (mgKOH/g)'] = m_portion1 * profile1['TAN (mgKOH/g)'] + m_portion2 * profile2['TAN (mgKOH/g)']
    x_pred['Salt (ptb)'] = v_portion1 * profile1['Salt (ptb)'] + v_portion2 * profile2['Salt (ptb)']
    x_pred['Nickel (mg/kg)'] = m_portion1 * profile1['Nickel (mg/kg)'] + m_portion2 * profile2['Nickel (mg/kg)']
    x_pred['Vanadium (mg/kg)']  = m_portion1 * profile1['Vanadium (mg/kg)'] + m_portion2 * profile2['Vanadium (mg/kg)']
    x_pred['C2 Ethane (vol%)'] = v_portion1 * profile1['C2 Ethane (vol%)'] + v_portion2 * profile2['C2 Ethane (vol%)']
    x_pred['C3 Propane (vol%)'] = v_portion1 * profile1['C3 Propane (vol%)'] + v_portion2 * profile2['C3 Propane (vol%)']
    x_pred['iC4 iso-Butane (vol%)'] = v_portion1 * profile1['iC4 iso-Butane (vol%)'] + v_portion2 * profile2['iC4 iso-Butane (vol%)']
    x_pred['nC4 n-Butane (vol%)'] = v_portion1 * profile1['nC4 n-Butane (vol%)'] + v_portion2 * profile2['nC4 n-Butane (vol%)']
    x_pred['iC5 iso-Pentane (vol%)'] = v_portion1 * profile1['iC5 iso-Pentane (vol%)'] + v_portion2 * profile2['iC5 iso-Pentane (vol%)']
    x_pred['nC5 n-Pentane (vol%)'] = v_portion1 * profile1['nC5 n-Pentane (vol%)'] + v_portion2 * profile2['nC5 n-Pentane (vol%)']
    x_pred['C6 Hexanes (vol%)'] = v_portion1 * profile1['C6 Hexanes (vol%)'] + v_portion2 * profile2['C6 Hexanes (vol%)']
    x_pred['C7 Heptanes (vol%)'] = v_portion1 * profile1['C7 Heptanes (vol%)'] + v_portion2 * profile2['C7 Heptanes (vol%)']
    x_pred['C8 Octanes (vol%)'] = v_portion1 * profile1['C8 Octanes (vol%)'] + v_portion2 * profile2['C8 Octanes (vol%)']
    x_pred['C9 Nonanes (vol%)'] = v_portion1 * profile1['C9 Nonanes (vol%)'] + v_portion2 * profile2['C9 Nonanes (vol%)']
    x_pred['C10 Decanes (vol%)'] = v_portion1 * profile1['C10 Decanes (vol%)'] + v_portion2 * profile2['C10 Decanes (vol%)']

    return x_pred