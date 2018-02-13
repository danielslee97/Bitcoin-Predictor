# Bitcoin-Predictor

From Hackathon at Binghamton, Feb 10, 2018

This program tries to predict whether the price of bitcoin will increase or decrease by using past transaction history from coinmarketcap.com

Program uses a HTML parser, utilizing beautiful soup, and turns the data into a csv file which will be extracted using pandas. 

OUTPUT: Probability of bitcoin prices increasing

ALGORITHM:
1. From the data, get the percent difference between the opening and closing value of all the days and store it into a list
  (Closed - Open) / Open
2. Get the three most current percent difference get the average slope of those three data points
3. Using the recent slope +- epsilon (margin of error), compare it with all subsets of three (in order from the oldest to most current) in the data, except the current. This is to check whether there were similar trends in the past
4. If similar, increment the number_of_matches by 1 and check if it has increased or decreased after that trend
5. If increased, increment the probability_of_increase by 1
6. After going through all the data, find the probability of the this trend increase based on previous similar trends
  probability_increase = probability_of_increase / number_of_matches
7. Output the probability to the user

This was a fun project to program for the hackathon. Of course this can be improved by predicting the predicted price or having an API to constantly get the latest transaction (Not by days as it is now) or programming an AI to do the prediction for us. There are rooms for inprovements but one thing that needs a huge improvement on is on data gathering
