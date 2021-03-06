# Coursework 1

## Technical information
### Repository URL
Please add the URL to your repository below, then delete this instruction text.
[Repository](https://github.com/ucl-comp0035/coursework-1-Rose-Pip)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!

## Selection of project methodology
### Methodology (or combination) selected
scrum

### Selection criteria and justification of selection
Here is the criteria for the project methodology selection (ordered from most important to the least important for this particular software project development):
1. Team members’ relevant experience and depth of knowledge:Is it suitable for software developers with little or no experience with software engineering and data science process models?

2. Suitability for the team size:Is it suitable for a small team (<10 people)?

3. The ease to adapt the methodology:The ease for non-experienced team member to adapt the methodology.

4. Volatility in the requirements for the software: quite volatile (real -time mapping, more functions might be added).

5. Level of complexity of the requirements for the software: real-time visuals (real-time data such as longtitude and latitude should be available as well)

Justification:
Scrum is a framework for developing, delivering, and sustaining products in a complex environment, with an initial emphasis on software development, although it has been used in other fields including research, sales, marketing and advanced technologies. It is designed for teams of ten or fewer members, who break their work into goals that can be completed within time-boxed iterations, called sprints, no longer than one month and most commonly two weeks. 
Scrum is a framework used for app development, delivery and maintenance of the app product. With scrum structures, team members progress in time-boxed daily meetings of 15 minutes or less, which is called daily scrums (a form of stand-up meeting). At the end of the sprint, the team holds two further meetings: the sprint review which demonstrates the work done to stakeholders to elicit feedback, and sprint retrospective which enables the team to reflect and improve. With high frequency of meeting, constant discussions and improvements and short lifetime of each small sprint. It is very sensity to any required change/ errors/ misunderstanding between team members. Therefore, it very effective for volatile requirements in our case. Moreover, it is ideal for small development team to produce an app in a short period. The scrum method, despites its efficiency, does not have a complex work flow, and therefore is beginner-friendly. 
Overall, to develop a web app that contains highly volatile requirements in a small team within a relatively short time period, scrum is the ideal framework. 

## Definition of the business need
### Problem definition
It is predicted that the population of Great London area will increase to up to 3 million people. Thus, an effective and efficient urban environmental protection project will is vital to help the city stay healthy and liveable as the population becomes larger.

London City Hall is the headquarters of the Greater London Authority (GLA), which comprises the Mayor of London and the London Assembly [1]. This authority has an ongoing **Urban Greening** project to improve the environment in the Great London area. One of the actions taken in this project is **tree planting** in the Great London area. **Tree planting** helps to improve the poor air quality and soil quality in the urban areas via removing and storing harmful chemicals (such as CO2, SO2, Lead)[3]. The 'Urban Greening' project also aims to Mitigating the impact of global warming on the weather in London and to increase the sustainability of the local economy with a decrease (or even elimination) in CO2 footprint[2]. 

The London City Hall would like to examine the effectiveness of the **tree planting** action under the **Urban Greening** project, in which way they can seek for improvements in their tree planting strategies in the future (such as which borough needs more regreening, and which tree species is the most suitable options, etc). However, it is financially impossible and extremely inefficient for the London City Hall to send employees to manually process the urban tree datasets to estimate the real-time distribution of trees, growth rate of quantity of trees and other characteristics of trees in all London boroughs. Therefore, it is necessary to automate the data analysis and visualisation process to generate informative results, which enables the London City Hall to establish strategic moves in the future regarding the current stage of the **tree planting** action. All data and visuals will be open to the UK citizens according to the transparency policies. 

### Target audience
London City Hall - Use the web app to examine the effectiveness of their tree planting action, and to seek for improvements in their greening strategies constantly. Citizens are alse encouraged to use the web app. 
**Persona**
![Persona](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/image/Screen%20Shot%202021-11-12%20at%2015.52.11.png)

### Suggested web app
1. It has an interface for the users to log in the collected data of urban trees, and the data processing stage is fully automated.
2. Dynamic charts and dataset tables based on real-time logged-in data that reflect the characteristics of trees in the London Boroughs. 
3. A real-time map, where the user can zoom in to view the specific longitude and latitude of trees in the borough they are interested in. 
4. The legends on the tree distribution map demonstrate the total amount of trees recorded in each borough (it is a dynamic legend, where the boroughs are ranked according to the quantity of trees in that region). 

### Questions to be answered using the dataset
**1.The quantity of the most common tree species in the Great London area?**
The answer to this question, combined with the records of the quantity of planted seeds and saplings of each species, can help the City Town Hall to estimate which are the species most likely to survive and grow healthily with the weather and environmental conditions in the Great London area. Therefore, they will invest more into planting these specific species for higher greening rate in the future. 

**2. Is the quantity of trees increasing through urban greening project?**
By calculating the average annual growth(or decrease) of tree quantity in each borough from **2018 to 2021**, the City Town Hall can examine the effectiveness of their action in these boroughs in the 2018-2021 period. 


## Data preparation and exploration
**This section is composed of three stages. In the first stage (early stage exploration), NaN is spotted and type of each column is generated. I decided to replace NaN with either integer 0 or 'not recorded', depending on the type of each column. If the column is numerical (i.e. Int64 and float64), then replace NaN with 0. If the column in other form, replace NaN with 'not recorded'. The second stage would be data preparaton, where data cleaning took place to replace NaN, remove any potential outliers and transfer the dataset into proper forms for any future data analysis. The third stage is to do data analysis and visualisations to explore any informative trends or generate any usdeful information for the London City Hall's problems.**

### :white_check_mark: Early stage exploration (exploration of data characteristics before data preparation)
[data_exploration](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/data_exploration.py)

At this stage, the information of planted trees in the Great London area was imported in forms of pandas dataframes into the python environment. The NaN cells and columns were spotted, and the types of cell values in each column in all dataframes were recognised.

**The types presented are:**
- numerical: Int64, float64
- strings and numerical combined: Object 


### :white_check_mark: Data preparation
[Data Preparation](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/data_preparation.py)

Since it is already known that the types of column values are either numerial(Int64, float64) or non-numerical (mixed type). Therefore, a function **remove_nan(df)** was built in the python script, which places NaN cells to either number 0 in the numerical-type columns, or a string "not recorded" in the mixed-type columns. This is for the unity of data type in all columns. 

Moreover, the empty columns and columns that would not be used for the data exploration stage are dropped, to speed up the running process, and to simplify the dataframe rearranging in the next stage. 

*** Note that, the longtitude and latitude columns will be vital when it comes to enabling the real-time tree distribution map to spot the accurate longtitude and latitude values of trees in the final web app product. So do other dropped columns for other web-app functionalities. They are dropped for now, but will be analysed later when coming across the web-app design.***

### :white_check_mark: Prepared data set
The links below will direct to the raw data sets. A zip file of the extremely big data set is presented in the original data set folder, in case the csv file failed to function or had any incorrect information. 

[Original data set](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/tree/master/data)
[Prepared data set](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/tree/master/prepared_data)


### :white_check_mark: Data exploration
[Further Data Exploration](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/data_exploration_2.py)

The prepared data set can be analysed further to get some informative results (either numerical values or visualisations). For the current stage, the most urgent problem for the London City Hall is to examine the effectiveness of their **tree-planting** action, and what strategic moves they can take in the near future. 

The exploration stage initiated with the analysis of the quantity distribution of different tree species in the Great London area. The five most common ones are shown here (the data set logged in the system in 2021 is the most recent one available):

**Please refer to the output in the python script**


The exploration stage then processed to the comparison of the quantity of trees in the Great London boroughs in 2018 and 2021 (latest logged-in data), from which the average annual growth rate of trees (greening rate) in each borough ( in the 2018-2021 period) can be estimated. Moreover, the bar chart shows the gap of quantity of trees between different boroughs. 

![Bar chart of trees distribution in the Great London Borough](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/image/dataplot.png)

It can be observed that City of London is the least greened region with the lowest quantity of trees in both 2018 and 2021. Bothe **City of London** and **TFL** regions suffered from decrease in the quantity of trees in the 2018-2021 period. The tree-planting action has to be enhanced specially in **City of London** region. 

## Weekly progress reports

### Report 1
What I did in the last week:
1. The criteria for the methodology selection is:

The technical backgrounds of the teammates 
The expected lifetime for the deployment of the web app (depends on the scenario your team is in, for instance, the clients would like to get the final product in three months)
The functionalities of the web app 
2. With this criteria in mind, I made my conclusions:

The team members are from non-programming backgrounds 
The lifetime of the web app is yet to be determined depending on the persona of the clients 
The functionalities of the web app for the tree map are not : 1. map visuals of tree characteristics; 2. blogs and forums 3. data visuals to see trends and to extract useful environmental information
3. To meet the criteria:
the methodology Scrum is chosen, because it enables a small, cross-functional, self-managing team to deliver fast. 

What I plan to do in the next week:
1. I would like to finish editing the data visualisation python script to explore useful information from the data set I am allocated with. In my case, I would like to plot a correlation diagram between the size of open spaces and the availability of trees in the region, to see the impact of the availability of open space on the quantity of trees. 


Issues blocking my progress (state ‘None’ if there are no issues):
1. I have carefully read the specification and cloned the repository to the local IDE. However, I was not too sure about where to list the data visuals. I would like to ask for suggestions in the next tutorial session. 

### Report 2
What I did in the last week:
1. I learned how to develop a problem statement and persona with clear logics and in standard format. 

2. I have listed a few personas that might be interested to visit the web app I developed (the people who cared about the local environment and regreening of the local regions)

What I plan to do in the next week:
I will do data ETL and develop visuals and graphs based on the persona and the problem statement. 

Issues blocking my progress (state ‘None’ if there are no issues):
1. no pending question for this week. 

### Report 3
What I did in the last week:
1. Learned Pandas Library 

2. learned how to import data to the python environment 

3. started on data cleaning and processing 

What I plan to do in the next week:
1. complete the first draft of my cw report. 

Issues blocking my progress (state ‘None’ if there are no issues):
No particular this week. 

### Report 4
What I did in the last week:
1. finalsing coursework1

What I plan to do in the next week:
fix the python extension, and improve the submitted coursework1. 

Issues blocking my progress (state ‘None’ if there are no issues):
3. my python scripts were gone for some reasons, and my python extension failed to work (greyed out). 

## References
1.“Town Hall.” Wikipedia, 31 July 2020, en.wikipedia.org/wiki/City_Hall.
2.London City Hall. (2015). Urban Greening. [online] Available at: https://www.london.gov.uk/what-we-do/environment/parks-green-spaces-and-biodiversity/urban-greening.
3.Benefits of Urban Trees A guide by GreenBlue Urban. (n.d.). [online] Available at: https://greenblue.com/wp-content/uploads/2016/05/Benefits-of-Urban-Trees.pdf [Accessed 12 Nov. 2021].
