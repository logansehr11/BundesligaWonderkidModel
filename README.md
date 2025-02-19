# Bundesliga Data Analysis

## Author
Logan Sehr

## Purpose
The purpose of this program is to practice my data science and machine learning skills on a topic I am interested in. As someone who has been playing FIFA Career Mode and Football Manager for years, finding wonderkids to bring to your team is a rewarding yet challenging process, especially for hidden gems. This program was made to show how, in a database of players, you can filter to find the players that will be part of the long-term future of your club. I also took inspiration from [TransferMarkt](https://www.transfermarkt.us/), a pioneer in the world of soccer stats and the term market value.

## What Does the Data Mean
The columns of data in focus from the `bundesliga_player.csv` were the player ages, price, and max price. The age and max price were used to calculate an additional feature, the age-to-market-value ratio. This ratio is key to establishing that the lower the age and the higher the max price, the more special the wonderkid. I used a Random Forest Regression model to predict this correlation, as it handles the non-linearity and high-variability of this data extremely well. After training the model on the entire dataset, I ran this prediction on both the entire dataset and a filtered-down dataset of solely the wonderkids (players under 21 years of age).

### How to Mimic This with Any Dataset
This program can be adapted to work with other .csv files, as many datasets regarding player databases in soccer will include the players' age and market value (to some degree, whether it be max price, price, or the mean price from multiple sources).

## What Did the Predictions Reveal
The data revealed the exact pattern I was expecting, with superstars like Jude Bellingham and Jamal Musiala having wonderkid scores beyond any of their counterparts. It was also observed that the accuracy of the overall set was, on average, 20% lower than the accuracy of the wonderkids set. This is most likely due to the age-to-market-value ratio, as older players who do not fall into the small portion of world stars tend to have a lower market value as their age grows close to and beyond 30 years. It could also be said that some superstars, if included with the wonderkids, would not change the accuracy at all, as their wonderkid scores would be equally as high. However, this would go against our goal of looking for potential and longevity, with the parameter of 21 years or younger being crucial in filtering out deceptive results.
