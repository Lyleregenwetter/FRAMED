# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:18:50 2022

@author: Lyle
"""

import pandas as pd
import numpy as np
import random
import sobol_seq 




def shufflethickness(df):
    scalemin = .5
    scalemax = 10
    
    columns=["Wall thickness Bottom Bracket", "Wall thickness Top tube", "Wall thickness Head tube", "Wall thickness Down tube", "Wall thickness Chain stay", "Wall thickness Seat stay", "Wall thickness Seat tube"]
    indices=list(df.index)
#     for i in range(len(df.index)):
#         if i%10!=0:
#             indices.append(df.index[i])
    random.shuffle(indices)
    len_sobol= len(indices)
    sobolvec= sobol_seq.i4_sobol_generate(7, len_sobol)
    thicknesses=geom_resample(scalemin, scalemax, sobolvec)
    thicknesses=pd.DataFrame(thicknesses, columns=columns, index=indices)
    df.update(thicknesses)
    return df

def geom_resample(minval, maxval, perc):
    #Vectorized code to perform FRAMED's tube thickness resampling
    maxval=np.full(np.shape(perc),maxval)
    return np.multiply(np.exp(np.multiply(np.log(np.divide(maxval, minval)),perc)), minval)

def setStays(df):
    for index in df.index:
        if df.loc[index, " CSB_Include"]<=0.5:
            df.loc[index, " CSB OD"]=0
        if df.loc[index, " SSB_Include"]<=0.5:
            df.loc[index, " SSB OD"]=0
    return df
        

def renameCols(df, biked):
    for col in df.columns:
        if col==" CS Length":
            df[col]=biked["CS textfield"]
        if col==" BB Drop":
            df[col]=biked["BB textfield"]
        if col==" Stack":
            df[col]=biked["Stack"]
        if col==" HT Angle":
            df[col]=biked["Head angle"]
        if col==" HT Length":
            df[col]=biked["Head tube length textfield"]
        if col==" SS E":
            df[col]=biked["Seat stay junction0"]
        if col==" ST Angle":
            df[col]=biked["Seat angle"]
        if col==" DT Length":
            df[col]=biked["DT Length"]
        if col==" ST Length":
            df[col]=biked["Seat tube length"]
        if col==" BB OD":
            df[col]=biked["BB diameter"]
        if col==" TT OD":
            df[col]=biked["ttd"]
        if col==" HT OD":
            df[col]=biked["Head tube diameter"]
        if col==" DT OD":
            df[col]=biked["dtd"]
        if col==" CS OD":
            df[col]=biked["csd"]
        if col==" SS OD":
            df[col]=biked["ssd"]
        if col==" ST OD":
            df[col]=biked["Seat tube diameter"]
            
        if col==" BB Thickness":
            df[col]=biked["Wall thickness Bottom Bracket"]
        if col==" TT Thickness":
            df[col]=biked["Wall thickness Top tube"]
        if col==" HT Thickness":
            df[col]=biked["Wall thickness Head tube"]
        if col==" DT Thickness":
            df[col]=biked["Wall thickness Down tube"]
        if col==" CS Thickness":
            df[col]=biked["Wall thickness Chain stay"]
        if col==" SS Thickness":
            df[col]=biked["Wall thickness Seat stay"]
        if col==" ST Thickness":
            df[col]=biked["Wall thickness Seat tube"]
            
        if col==" BB Length":
            df[col]=biked["BB length"]
        if col==" CS F":
            df[col]=biked["Chain stay position on BB"]
        if col==" SS Z":
            df[col]=biked["SSTopZOFFSET"]
        if col==" Material":
            df[col]=biked["MATERIAL"]
        if col==" HT UX":
            df[col]=biked["Head tube upper extension2"]
        if col==" ST UX":
            df[col]=biked["Seat tube extension2"]
        if col==" HT LX":
            df[col]=biked["Head tube lower extension2"]
        if col==" SSB Offset":
            df[col]=biked["SEATSTAYbrdgshift"]
        if col==" CSB Offset":
            df[col]=biked["CHAINSTAYbrdgshift"]
        if col==" Dropout Offset":
            df[col]=biked["Dropout spacing"]
    return df