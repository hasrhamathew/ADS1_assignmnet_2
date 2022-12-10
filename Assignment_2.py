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


coul_sources = coul_sources[['Country Name','1998','2003','2008','2013','2018']]
coul_sources1 = coul_sources.set_index('Country Name').transpose()

print (coul_sources1)
coul_sources2 = coul_sources1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]
                             
print(coul_sources2.dropna(inplace = True))
                            
urban_population = pd.read_csv("Urban_population.csv")
print(urban_population.dropna())
         
urban_population = urban_population[['Country Name','1998','2003','2008','2013','2018']]
urban_population1 = urban_population.set_index('Country Name').transpose()
print (urban_population1)
urban_population2 = urban_population1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]
urban_population2 = urban_population2.transpose()
print(urban_population2)

x = np.arange(len(urban_population2.index))
width = 0.2

fig, ax = plt.subplots(figsize=(13,14))
#bar1 = ax.bar(x - 2*width, urban_population2['1998'], width, label='1998')
bar2 = ax.bar(x - width, urban_population2['2003'], width, label='2003')
bar3 = ax.bar(x, urban_population2['2008'], width, label='2008')
bar4 = ax.bar(x + width, urban_population2['2013'], width, label='2013')
bar5 = ax.bar(x + 2*width, urban_population2['2018'], width, label='2018')

ax.set_ylabel('Ratio')
ax.set_title('URBAN POPULATION', size=12,)
ax.set_xticks(x, urban_population2.index, rotation = 90)
ax.set_xlabel('Country Names')
ax.legend()

#ax.bar_lurban_population2.index(bar1, padding=3)
ax.bar_urban_population2.index(bar2, padding=3)
ax.bar_urban_population2.index(bar3, padding=3)
ax.bar_urban_population2.index(bar4, padding=3)
ax.bar_urban_population2.index(bar5, padding=3)

fig.tight_layout()

plt.show()

years = ['1998','2003','2008','2013','2018']
x = np.arange(len(years))
width = 0.35

plt.figure()
urban_population2.plot(x = 'Index', y = 'years', kind = 'bar' )
plt.title("jjj",fontsize = 12)
plt.xlabel('Country Name')
plt.xticks(rotation = 90)
plt.ylabel('Ratio')
plt.legend(frameon = False, fontsize = 7)
plt.show()

plt.figure(figsize=(13,14)) 
plt.xlabel("Country Name")
plt.ylabel("Ratio")
plt.title("Urban Population",size=20)
plt.bar(urban_population1.index, urban_population1["1998"])
plt.xticks(rotation=90)
plt.savefig('urban.png')
plt.show()

urban_population2 = urban_population1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]


countryNames = ['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']                 


greenhouse_gas = greenhouse_gas[['Country Name','1998','2003','2008','2013','2018']]
greenhouse_gas1 = greenhouse_gas.set_index('Country Name').transpose()
greenhouse_gas = pd.read_csv("greenhouse_gas.csv")
print(greenhouse_gas.dropna())


print (greenhouse_gas1)
greenhouse_gas2 = greenhouse_gas1[['United Arab Emirates','Australia','Pakistan','Brazil',
                             'Switzerland','China','Germany','Spain','United Kingdom',
                              'India','Japan','Croatia','Bangladesh']]
                             
print(greenhouse_gas2.dropna(inplace = True))






