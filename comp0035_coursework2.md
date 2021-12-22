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
It is a 4-step process:
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
**:two:Login Page**
**:three:External User Home Page**
**:four:Internal User Home Page**
**:five:DashBoard**
**:six:Reports/News**
**:seven:DashBoard Editing Page**
**:eight:Reports/News Editing Page**
**:nine:Profile Page**
### Application structure
#### :o: UML class diagram for this web app

#### :o: UML sequence diagrams for this web app
**The sequence diagram for the external users**

**The sequence diagram for the internal users**

### Relational database design

## Testing
### Choice of unit testing library

### Tests
The tests should be in a separate and appropriately named file/directory.

### Test results
Provide evidence that the tests have been run and the results of the tests (e.g. screenshot).


## Weekly progress reports

### Report 1
What I did in the last week:
-Learned how to choose suitable methods to identify requirements, specify requirements and prioritize requirements. 
-Started on choosing to brainstorm for the identification requirements for the coursework.
-Learned the stages taken to create wireframes for the user interface design (thorough understanding of UI and UX). 

What I plan to do in the next week:
-Will go through the detailed criteria of coursework 2.  
-I plan to learn the standard UML diagrams for application design.

Issues blocking my progress (state ‘None’ if there are no issues):
-A bit confused about the concept of UML. 

### Report 2
What I did in the last week:
-I earned Application Design and Interface Design. 
-Moreover, I started drafting the UML diagrams (sequence diagram/ class diagram) for the web app I designed. 

What I plan to do in the next week:
-I plan to start learning database design and code quality with the lecture recording provided. 
-After that, I will start drawing the relational database diagram for the coursework.

Issues blocking my progress (state ‘None’ if there are no issues):
-I have no question in particular. 

### Report 3
What I did in the last week:
-I have learned the database design methods, and how to examine the code quality. 
-I then developed an ER diagram to represent the relations between all databases for this web app. 
What I plan to do in the next week:
-I plan to finalize the first draft of the requirement and application design parts of coursework 2. 
-Then I will start on the testing part.

Issues blocking my progress (state ‘None’ if there are no issues):
-I have no question in particular.

### Report 4
What I did in the last week:
-I have done the requirements and done the sequence diagrams for the web app. I also made progress on the testing script. 

What I plan to do in the next week:
-I will finalize the application design part for the coursework. I will also learn how to generalize reports on the testing. 

Issues blocking my progress (state ‘None’ if there are no issues):
-I am still a bit confused about the testing report bit. 

## References
1.
2.
3.
