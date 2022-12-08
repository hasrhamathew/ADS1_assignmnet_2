# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:26:32 2022

@author: harsha
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


agriculture = pd.read_csv("Agriculture.csv")
print(agriculture)
print(agriculture.dropna())

agriculture = agriculture[['Country Name','1998','2003','2008','2013','2018']]
agriculture1 = agriculture.set_index('Country Name').transpose()

print (agriculture1)
agriculture2 = agriculture1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                             'India','Japan','Croatia','Bangladesh']]
                             
print(agriculture2)

CO2_emissions = pd.read_csv("CO2_emissions.csv")


CO2_emissions = CO2_emissions[['Country Name','1998','2003','2008','2013','2018']]
CO2_emissions1 = CO2_emissions.set_index('Country Name').transpose()

print (CO2_emissions1)
CO2_emissions2 = CO2_emissions1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                             'India','Japan','Croatia','Bangladesh']]
                             
print(CO2_emissions2)


coul_sources = pd.read_csv("coul_sources.csv")
print(coul_sources.dropna())

coul_sources = coul_sources[['Country Name','1998','2003','2008','2013','2018']]
coul_sources1 = coul_sources.set_index('Country Name').transpose()

print (coul_sources1)
coul_sources2 = coul_sources1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]
                             
print(coul_sources2)
                            
urban_population = pd.read_csv("Urban_population.csv")
print(urban_population.dropna())

urban_population = urban_population[['Country Name','1998','2003','2008','2013','2018']]
urban_population1 = urban_population.set_index('Country Name').transpose()

print (urban_population1)
urban_population2 = urban_population1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]
                             
print(urban_population2.dropna())

greenhouse_gas = pd.read_csv("greenhouse_gas.csv")
print(greenhouse_gas.dropna())

greenhouse_gas = greenhouse_gas[['Country Name','1998','2003','2008','2013','2018']]
greenhouse_gas1 = greenhouse_gas.set_index('Country Name').transpose()

print (greenhouse_gas1)
greenhouse_gas2 = greenhouse_gas1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]
                             
print(greenhouse_gas2.dropna())





