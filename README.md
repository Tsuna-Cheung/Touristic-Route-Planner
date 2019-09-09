# Touristic-Route-Planner
This project is the MSc project of University of Birmingham.
* Author: Zhongfang Zhang
* Student ID: 1893956
* MSc in Advanced Computer Science
* Supervisor: Paul Levy
* School of Computer Science
* The University of Birmingham
* September 2019

## Content of Project
* img: This folder holds the images used by the project.
* Reference_img.docx: This file is the reference of images used by the project.
* chinacity_33.csv: Dataset
* moneycost_china33.csv: Dataset
* GUI_TRP.py: The GUI code of the project
* EA_TRP.py: The code of single-objective optimisation evolutionary algorithm
* MOEA_TRP.py: THe code of multi-objective optimisation evolutionary algorithm

## How to run the software
* Run GUI_TRP.py to display the user interface, which is also the entrance of the software.
* Click on the city name in the cities list to get the corresponding city's tourism information.
* Double-click on an attraction in the list of attractions to display a photo of the corresponding attraction.
* Check the checkbox in the city list to select the cities you want to visit.
* After selecting the city, click the ‘’plan your tour’ button to enter the route planning interface.
* Tabs in the route planning interface can be used to switch between different optimisation patterns.
* Click on the drop-down box after the departure city to select the departure city. The selected city will be the starting and ending point of the tour.
* Finally, click on the ‘’plan your tour’ button to run the evolutionary algorithm. Waiting for the computation of the algorithm, the recommended route will be shown in the interface.
