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

    # Assume the volume of the mixture is the sum of the two crude volume.
    volume = volume1 + volume2
    v_portion1 = volume1 / volume
    v_portion2 = volume2 / volume
    mass = volume1 * profile1['Absolute Density (kg/m3)'] + volume2 * profile2['Absolute Density (kg/m3)']
    m_portion1 = volume1 * profile1['Absolute Density (kg/m3)'] / mass
    m_portion2 = volume2 * profile2['Absolute Density (kg/m3)'] / mass
    
    # Calculating the phiscial properties of the mixture. (x_pred) 
    density = mass / volume
    gravity = v_portion1 * profile1['Gravity (&degAPI)'] + v_portion2 * profile2['Gravity (&degAPI)']
    sulphur =  m_portion1 * profile1['Sulphur (wt%)'] + m_portion2 * profile2['Sulphur (wt%)']
    mcr =  m_portion1 * profile1['MCR (wt%)'] + m_portion2 * profile2['MCR (wt%)']
    sediment = m_portion1 * profile1['Sediment (ppmw)'] + m_portion2 * profile2['Sediment (ppmw)']
    tan = m_portion1 * profile1['TAN (mgKOH/g)'] + m_portion2 * profile2['TAN (mgKOH/g)']
    salt = v_portion1 * profile1['Salt (ptb)'] + v_portion2 * profile2['Salt (ptb)']
    nickel = m_portion1 * profile1['Nickel (mg/kg)'] + m_portion2 * profile2['Nickel (mg/kg)']
    vanadium = m_portion1 * profile1['Vanadium (mg/kg)'] + m_portion2 * profile2['Vanadium (mg/kg)']
    c2 = v_portion1 * profile1['C2 Ethane (vol%)'] + v_portion2 * profile2['C2 Ethane (vol%)']
    c3 = v_portion1 * profile1['C3 Propane (vol%)'] + v_portion2 * profile2['C3 Propane (vol%)']
    c4i = v_portion1 * profile1['iC4 iso-Butane (vol%)'] + v_portion2 * profile2['iC4 iso-Butane (vol%)']
    c4n = v_portion1 * profile1['nC4 n-Butane (vol%)'] + v_portion2 * profile2['nC4 n-Butane (vol%)']
    c5i = v_portion1 * profile1['iC5 iso-Pentane (vol%)'] + v_portion2 * profile2['iC5 iso-Pentane (vol%)']
    c5n = v_portion1 * profile1['nC5 n-Pentane (vol%)'] + v_portion2 * profile2['nC5 n-Pentane (vol%)']
    c6 = v_portion1 * profile1['C6 Hexanes (vol%)'] + v_portion2 * profile2['C6 Hexanes (vol%)']
    c7 = v_portion1 * profile1['C7 Heptanes (vol%)'] + v_portion2 * profile2['C7 Heptanes (vol%)']
    c8 = v_portion1 * profile1['C8 Octanes (vol%)'] + v_portion2 * profile2['C8 Octanes (vol%)']
    c9 = v_portion1 * profile1['C9 Nonanes (vol%)'] + v_portion2 * profile2['C9 Nonanes (vol%)']
    c10 = v_portion1 * profile1['C9 Nonanes (vol%)'] + v_portion2 * profile2['C9 Nonanes (vol%)']

    x_pred_array = [density, gravity, sulphur, mcr, sediment, tan, salt, nickel, vanadium,
                    c2, c3, c4i, c4n, c5i, c5n, c6, c7, c8, c9, c10]
    x_pred = {}
    for i, key in enumerate(list(profile1.keys())[:-1]):
        x_pred[key] = x_pred_array[i]
    return x_pred