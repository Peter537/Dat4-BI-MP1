# Dat4-BI-MP1

# Table of contents

1. [Data sources](#data-sources)
2. [Counter Strike 2, players over time](#counter-strike-2-players-over-time)
3. [Covid infections Denmark](#covid-infections-denmark)
4. [Electrical grid coverage](#electrical-grid-coverage)

## Data sources

[Counter Strike players (.xlsx)](https://steamdb.info/app/730/charts/)

[Covid infection data (.csv)](https://www.kaggle.com/datasets/georgesaavedra/covid19-dataset/data)

[Electrical grid coverage (.xml)](https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS?view=chart) {

    Two cut-offs from this bigger file into the smaller: ZimbabweData.xml || ComorosData.xml

}

## Counter Strike 2, players over time

Steam measures the amount of players playing Counter Strike. The website "Steam DB" stores these measurements and allows user from Steam access to the data. The data then contains the date, how many players and the average of players.

The data is not always consistent, there is missing data values and the way it is measured is changing.

### Relevant Python files

[cs-players workbook](./cs-players.ipynb)

[xlsx loader](./xlsxloader.py)

## Covid infections Denmark

Every single day a lot of metrics are being collected for the Covid-19 pandemic, and in this dataset there is every single country, but we have decided to cut all countries other than Denmark.

### Relevant Python files

[denmark-covid-workbook](./denmark-covid-data.ipynb)

## Electrical grid coverage

A big datasource showing percentage-access to electricity per country/area. In this dataset i will firstly sort, fill and visualise one dataframe and then compare it to another.

Aspects of this project:

basic data-manipulation, data-filling, python-coding (made a xml-file loader), data analysis in form of comparison

### Relevant Python files

[WorldBank Org](./ElectricalData.ipynb)

[xml file loader](./xmlloader.py)
