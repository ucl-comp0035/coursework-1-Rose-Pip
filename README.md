# Coursework 2

## Definition of the business need
### Problem definition
It is predicted that the population of Great London area will increase to up to 3 million people. Thus, an effective and efficient urban environmental protection project will is vital to help the city stay healthy and liveable as the population becomes larger.

London City Hall is the headquarters of the Greater London Authority (GLA), which comprises the Mayor of London and the London Assembly [1]. This authority has an ongoing **Urban Greening** project to improve the environment in the Great London area. One of the actions taken in this project is **tree planting** in the Great London area. **Tree planting** helps to improve the poor air quality and soil quality in the urban areas via removing and storing harmful chemicals (such as CO2, SO2, Lead)[3]. The 'Urban Greening' project also aims to Mitigating the impact of global warming on the weather in London and to increase the sustainability of the local economy with a decrease (or even elimination) in CO2 footprint[2]. 

The London City Hall would like to examine the effectiveness of the **tree planting** action under the **Urban Greening** project, in which way they can seek for improvements in their tree planting strategies in the future (such as which borough needs more regreening, and which tree species is the most suitable options, etc). However, it is financially impossible and extremely inefficient for the London City Hall to send employees to manually process the urban tree datasets to estimate the real-time distribution of trees, growth rate of quantity of trees and other characteristics of trees in all London boroughs. Therefore, it is necessary to automate the data analysis and visualisation process to generate informative results, which enables the London City Hall to establish strategic moves in the future regarding the current stage of the **tree planting** action. All data and visuals will be open to the UK citizens according to the transparency policies. 

### Target audience
London City Hall - Use the web app to examine the effectiveness of their tree planting action, and to seek for improvements in their greening strategies constantly. Citizens are alse encouraged to use the web app. 
**Sample Persona**
![Persona](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/image/Screen%20Shot%202021-11-12%20at%2015.52.11.png)

## Requirements definition and analysis
**The requirements section is based on the business need section, i.e. the problem definiton and the targeted audience.**
Based on the problem definition and target audience, a context diagram is generated to briefly describe the interaction between the relevant entities with the system of the web app.
![contexflow](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/contextflow.JPG)
### Requirements identification methods
The requirements identification method applied is to identify requirements from users' stories based on brainstorming. In real-life application, surveys and interviews will be combined to generate users' wants and needs (surveys and interviews will take place with ethics approval in London City Hall). However, since no ethics approval is given in this case, no survey or interview is done. All users' stories will solely based on brainstorming and referring to similar web apps. 
### Requirement specification method
The framework chosen for this web app is Scrum to provide an agile application designing process. 
Therefore the **user story methodology** is implied for requirement specification, as it is highly adaptable in agile software development. It demonstrates the types of users and their wants and needs, from which the accpetance criteria are set for the web app design. 
The user story list is constantly updated based on the changes of users' needs and the realisticity of users' needs. A user story list is documented and provided below. 
### Prioritisation method
**MosCoW Method** is a highly suitable prioritisation method for this web app. MosCoW method is a common tool to categorise requirements so that the stakeholders of the web app can come to a common agreement on the most urgent and important requirements.
It is a 4-step process[1]:
**Must have**: The web-app features that must be included, else the web app is meaningless. For instance, Youtube must be able to play videos on the web page. 
**Should have**: The Web-app features that are important but not a must-have. These features differ from the 'Must have' in a way that they can be added in a later released version without impacting the current version. 
**Could have**: The 'could-have' features are the ones that are good to have for th web app, but not necessary nor urgent. For instance, Deliveroo app can add a voice message function to the deilverer chat box so that the customer can choose to leave a quick easy voice message rather than typing. However, this feature is not necessary nor urgent.
**Will not have**: These are the features that will not be added to the web app in the current status to prevent **scope creep** (running out of time and resources because of the forever changing requirements). They might be prioritised in the future released versions, depending on the time and resources given in the future. 
### Documented and prioritised requirements
#### User story table (specified requirements)
![UserStory](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/requirment%20document.JPG)
#### Prioritised requirements 
**Note that in this coursework, the design of the web app mainly focuses on the Must-have and Should-have requirements.**
![Prioritised requirements](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/MosCow.JPG)

## Design
### Structure and flow of the interface
#### :o: Targeted users and main functions  
The web application is designed solely for PC terminal. 
There are two types of users: external users (citizens who do not work at London City Hall) and internal users (staff at London City Hall). It is noticeable that both types of users are the targeted audience stated in the first section. 
The main functions available for the internal users are:
1. For the data analysts at London City Hall, the dashboard editing tools are available to use after login with their authorised staff ID. The dashboard tools are drag-and-drop. 
2. For the project managers at London City Hall working under the Urban Greening Project, the report/news editing tools are available to use after login with their authorised staff ID. The reports/news editing tools are available solely to the project managers on the reports/news editing web page. 
#### :o: The flow of interface
![InterfaceFlow](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/Interface%20flow.JPG)
#### :o: Wireframes of each page 
**:one:Registration Page**
![registration](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/sign-up%20page.JPG)

**:two:Login Page**
![login](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/login%20page%20wireframe.JPG)

**:three:External User Home Page**
![externalhome](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/home%20page%20external%20user.JPG)

**:four:Internal User Home Page**
![internalhome](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/home%20page%20internal%20user.JPG)

**:five:DashBoard**
![dashboard](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/dasboard.JPG)

**:six:Reports/News**
![report](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/report_news.JPG)

**:seven:DashBoard Editing Page**
![dashboardedit](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/dash%20board%20editing%20page.JPG)

**:eight:Reports/News Editing Page**
![reportsedit](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/report_news%20editing.JPG)

**:nine:Profile Page**
![profile](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/profile%20page.JPG)
### Application structure
#### :o: UML class diagram for this web app[2]
![classdiagram](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/class%20diagram.JPG)
#### :o: UML sequence diagrams for this web app[3]
**The sequence diagram for the external users**
![externaluser](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/sequence%20diagram%20(external%20user).JPG)
**The sequence diagram for the internal users**
![internaluser](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/sequence%20diagram%20(internal%20user).JPG)
:warning: Please note that the internal user sequence diagram looks complex. However, it contains four types of processes:
1. registration loop
2. login loop
3. Verified staff (data analysts) editing dashboard
4. Verified staff (project managers) editing reports/news

### Relational database design[4]
![ERD](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/Rose-Pip-editing/Image-cw2/relational%20database.JPG)

## Testing
### Choice of unit testing library is Pytest Library 

### Tests
**:one: [test 1 script](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/tests/test_1_script.py)**
**:two: [test 2 script](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/tests/test_2_script.py)**
**:three: [tested class script](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/python/main.py)**

### Test results
**:one: Test 1 passed due to correct assertion**
![test 1 results](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/Image-cw2/Test%201%20result.png)

**:two: Test 2 failed due to wrong input password**
![test 2 results](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/Image-cw2/Test%202%20result.png)

### Coverage Report of the main script (alternative testing method)
**The commends implied here is python -m pytest --cov=python, where python is the project name. This not only gives the testing results for both tests, but also indicates the testing coverage rate.
Testing coverage rate measures the degree to which the program source code execution achieves when a test is run. High test coverage rate means more of the source code is executed during the test, suggesting that it has a lower probability of containing any undetected bugs compared to the ones with low test coverage rate.The coverage rate of this script is 71%, which means more improvement shall be made to the script[5].**

![coverage report](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/Image-cw2/coverage%20test%201.png)
![coverage report2](https://github.com/ucl-comp0035/coursework-1-Rose-Pip/blob/master/Image-cw2/coverage%20test%202.png)

## Weekly progress reports
### Report 1
What I did in the last week:
-Learned how to choose suitable methods to identify requirements, specify requirements and prioritize requirements. 
-Started on choosing to brainstorm for the identification requirements for the coursework.
-Learned the stages taken to create wireframes for the user interface design (thorough understanding of UI and UX). 

What I plan to do in the next week:
-Will go through the detailed criteria of coursework 2.  
-I plan to learn the standard UML diagrams for application design.

Issues blocking my progress (state ???None??? if there are no issues):
-A bit confused about the concept of UML. 

### Report 2
What I did in the last week:
-I earned Application Design and Interface Design. 
-Moreover, I started drafting the UML diagrams (sequence diagram/ class diagram) for the web app I designed. 

What I plan to do in the next week:
-I plan to start learning database design and code quality with the lecture recording provided. 
-After that, I will start drawing the relational database diagram for the coursework.

Issues blocking my progress (state ???None??? if there are no issues):
-I have no question in particular. 

### Report 3
What I did in the last week:
-I have learned the database design methods, and how to examine the code quality. 
-I then developed an ER diagram to represent the relations between all databases for this web app. 
What I plan to do in the next week:
-I plan to finalize the first draft of the requirement and application design parts of coursework 2. 
-Then I will start on the testing part.

Issues blocking my progress (state ???None??? if there are no issues):
-I have no question in particular.

### Report 4
What I did in the last week:
-I have done the requirements and done the sequence diagrams for the web app. I also made progress on the testing script. 

What I plan to do in the next week:
-I will finalize the application design part for the coursework. I will also learn how to generalize reports on the testing. 

Issues blocking my progress (state ???None??? if there are no issues):
-I am still a bit confused about the testing report bit. 

## References
1.Product plan (2018). What is MoSCoW Prioritization? | Overview of the MoSCoW Method. [online] Productplan.com. Available at: https://www.productplan.com/glossary/moscow-prioritization/.

2.Paradigm, V. (2019). UML Class Diagram Tutorial. [online] Visual-paradigm.com. Available at: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/.

3.Lucidchart (2019). UML Sequence Diagram Tutorial. [online] Lucidchart. Available at: https://www.lucidchart.com/pages/uml-sequence-diagram.

4.SearchDataManagement. (2019). What is entity relationship diagram (ERD)? - Definition from WhatIs.com. [online] Available at: https://searchdatamanagement.techtarget.com/definition/entity-relationship-diagram-ERD.

5.Dorf, R.C. (2018). Computers, Software Engineering, and Digital Devices. [online] Google Books. CRC Press. Available at: https://books.google.co.uk/books?id=jykvlTCoksMC&pg=PT386&lpg=PT386&dq=%22infeasible+path%22+%22halting+problem%22&source=web&ots=WUWz3qMPRv&sig=dSAjrLHBSZJcKWZfGa_IxYlfSNA&hl=en&sa=X&oi=book_result&ct=result&redir_esc=y#v=onepage&q=%22infeasible%20path%22%20%22halting%20problem%22&f=false [Accessed 22 Dec. 2021].
