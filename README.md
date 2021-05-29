# Ad Clicker Predictor: Project Overview

In this project, I am using a fake advertisement data set to see if an internet user clicked on an advertisement. Using a Logistic Regression Model, my model will predict whether or not the internet user clicked on an ad based on the features of that user 

## Data Set
This data set contains the following features:

* 'Daily Time Spent on Site': consumer time on site in minutes
* 'Age': cutomer age in years
* 'Area Income': Avg. Income of geographical area of consumer
* 'Daily Internet Usage': Avg. minutes a day consumer is on the internet
* 'Ad Topic Line': Headline of the advertisement
* 'City': City of consumer
* 'Male': Whether or not consumer was male
* 'Country': Country of consumer
* 'Timestamp': Time at which consumer clicked on Ad or closed window
* 'Clicked on Ad': 0 or 1 indicated clicking on Ad

**Target Variable:** Clicked on Ad (0 = did not click, 1 = clicked)

## Code and Resources Used
**Python Version:** Python 3.8
**Packages Used:** pandas, numpy, matplotlib, seaborn, sklearn

## Exploratory Data Analysis
I explored distributions of categorical variables, including my target variable. Below are a few highlights of my visualizations.

[]('https://github.com/darienlizano/Ad_Clicker_Predictor/blob/main/ad_corr_plot.png')

[alt_text]('https://github.com/darienlizano/Ad_Clicker_Predictor/blob/main/internet_plot.png')

[alt_text]('https://github.com/darienlizano/Ad_Clicker_Predictor/blob/main/kde_dist.png')

## Building My Model
My target variable was initially entered in the data set as a dummy variable. I split my data into a training and test data set and saved those as separate csv files. My test and train data were split by a test size of 30%.

For this project, I chose a Logisitic Regression Model due to its high performance in accuracy measurements. 

## Model Performance 
Using a classification report, my model performed with average accuracies of 93% in precision, recall and f1-score.
