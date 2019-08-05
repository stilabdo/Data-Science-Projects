# English Premier League Insights
This project is a part of my data science portfolio of projects.

#### -- Project Status: Completed

### Introduction:

The Premier League (often referred to as the English Premier League `EPL` outside England) is the top level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League `EPL`. Seasons run from August to May with each team playing 38 matches (playing all 19 other teams both home and away). The English Premier League `EPL` with this name started only in February `1992` and the first season of this version was `1992/1993`.

## Project Intro/Objective
The purpose of this project is to get some insights from the EPL by analyzing standing tables.

### Methods Used
* Web Scraping
* Data Visualization

### Technologies
#### Python with jupyter notebook
##### Libiries
* urllip.request
* BeautifulSoup
* Pandas 
* Matplotlib

## Project Description

 The data of this project scraped from an online soccer website that contains Premier League results archives.  which is can be found in this [Link](https://www.worldfootball.net/schedule/eng-premier-league-2018-2019-spieltag/38/).
 
 All EPL seasons included in this project since the debut of this version of the EPL(season 1992/1993 to 2018/2019).
 
 Two tables considered, game-week 13 & game-week 38 (end of the season) for each season.
 
 Attributes:
 * rank &nbsp; : &nbsp; The rank of the club on after certain matches played.
 * team &nbsp; : &nbsp; EPL Club name.
 * matches_played &nbsp; : &nbsp; Number of matches played.
 * wins &nbsp; : &nbsp; Number of wins after the number of matches played.
 * drawns &nbsp; : &nbsp; No of drawns after the number of matches played.
 * losses &nbsp; : &nbsp; No of losses after the number of matches played.
 * goals_for &nbsp; : &nbsp; Goals scored for.
 * goals_against &nbsp; : &nbsp; Goals scored against.
 * goals_diff &nbsp; : &nbsp; Difference b/w goals_for and goals_against.
 * points &nbsp; : &nbsp; Points accumulated after the number of matches played.
 * season &nbsp; : &nbsp; Current season.

## Needs of this project

- Data exploration
- Data processing/cleaning
- Writeup/reporting

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](https://github.com/stilabdo/Data-Science-Projects/blob/master/English-Premier-League-Insights/pl_tables.csv) within this repo.
3. Data processing/transformation scripts are being kept [here](https://github.com/stilabdo/Data-Science-Projects/blob/master/English-Premier-League-Insights/English%20Premier%20League%20Insights.ipynb)


