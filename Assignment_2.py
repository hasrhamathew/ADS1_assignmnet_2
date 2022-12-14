# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:26:32 2022

@author: harsha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    """ 
    This function reads data from a csv file and transpose it. In the end we 
    will have two dataframes, one with country names as column and the other
    one with years as column.

    Parameter: file_name

    """

    data = pd.read_csv(file_name)
    data = data[['Country Name', '1990', '1995', '2000', '2005',
                 '2010', '2015', '2019']]
    year_col = data
    year_col.set_index("Country Name")
    country_col = data.transpose()
    return year_col, country_col


def filter_data(data):
    """
    This funtion filters required country names from a list of countries 
    in the dataframe
    """
    data_filter = data[data["Country Name"].isin(country_filter)]
    return data_filter


def bar_plot(df_name, title="", ylabel="", savefigure=""):
    """
    This function produce a bargraph.
    Parameters: df_name, title, ylabel, savefigure
    """
    plt.figure(figsize=(16, 17))
    years = ['2000', '2005', '2010', '2019']
    df_name.plot(x="Country Name", y=years, kind='bar')
    plt.title(title, fontsize=12)
    plt.xlabel('Country Names', fontsize=5)
    plt.xticks(fontsize=5, rotation=45)
    plt.ylabel(ylabel, fontsize=5)
    plt.yticks(fontsize=5)
    plt.legend(frameon=False, fontsize=6)
    plt.savefig(savefigure, bbox_inches="tight", dpi=200)
    plt.show()


def line_plot(df_name, year, countries, xlabel="", ylabel="", title="",
              savefigure=""):
    """
    This function produce a lineplot.
    Parameters: df_name, year, countries, xlabel, ylabel, title, savefigure
    """

    plt.figure(figsize=(16, 17))
    plt.plot(year, df_name[countries], label=countries)
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.title(title, fontsize=20)
    plt.legend(loc="upper right", fontsize=10)
    plt.savefig(savefigure, dpi=200)
    plt.show()


country_filter = ['United Arab Emirates', 'Australia', 'Pakistan',
                  'Switzerland', 'China', 'Germany', 'Spain', 'United Kingdom',
                  'India', 'Japan', 'Croatia']

# Reading the csv files
urban_population, urban_population_transpose = read_file(
    "Urban_population.csv")
co2_emission, co2_emission_transpose = read_file("CO2_emissions.csv")
greenhouse, greenhouse_transpose = read_file("greenhouse_gas.csv")
coal_sources, coal_sources_transpose = read_file("coal_sources.csv")

# Filtering the data
filtered_urban = filter_data(urban_population)
filtered_co2 = filter_data(co2_emission)
filtered = filter_data(greenhouse)

# Setting the index as country name
filtered_greenhouse = filtered.set_index('Country Name')
filtered_greenhouse.index.name = None
filtered = filter_data(coal_sources)
filtered_coal = filtered.set_index('Country Name')
filtered_coal.index.name = None


filtered = filter_data(urban_population)
filtered_pop = filtered.set_index('Country Name')
filtered_pop.index.name = None

# Finding the mean for urban population
urban_population_mean = np.mean(filtered_pop.transpose()[country_filter])

# Calling the functions with proper arguments
bar_plot(filtered_urban, "Urban Population", "Ratio", "urban_population.png")
bar_plot(filtered_co2, "CO2 Emission", "Ratio", "co2_emission.png")
line_plot(filtered_greenhouse.transpose(), filtered_greenhouse.transpose().index,
          country_filter, "Years", "Ratio",
          "Greenhouse Gas Emission", "greenhouse.png")
line_plot(filtered_coal.transpose(), filtered_coal.transpose().index,
          country_filter, "years", "Ratio",
          "Electricity production from coal sources", "coal_sources.png")







