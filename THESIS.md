GIS-Based Analysis of Commuters Facility and Modern Jeepney Routes  
Using Contingency Valuation and K-means Clustering  
along Barangay Gusa to Barangay Bugo in Cagayan de Oro City 
 
 
 
 
 
A Project Study Presented to  
The Faculty of the Department of Civil Engineering  
Xavier University - Ateneo de Cagayan 
 
 
 
 
 
 
 
 
 
In Partial Fulfillment For the Requirements for the Degree 
Bachelor of Science in Civil Engineering 
 
LOPEZ, BEA ARABELLA B. 
USMAN, JAMMEZA 
CAPIÑA, KACEY 
CUNDANGAN, CAROLINE 
 
 
 
JULY 2026

TABLE OF CONTENTS 
 
CHAPTER ONE: THE PROBLEM AND ITS SETTING 
1.1 Background of the Study                                                                                                      3 
1.2 Statement of the Problem                                                                                                     3 
1.3 Objectives of the Study                                                                                                        9 
1.4 Significance of the Study                                                                                                     9 
1.5 Conceptual Framework                                                                                                      10 
1.6 Theoretical Framework                                                                                                      10 
1.7 Scope and Limitations                                                                                                        11 
1.8 Definition of Terms​
                                                                                                  13 
CHAPTER TWO: REVIEW OF RELATED LITERATURES AND STUDIES   
2.1 Modernization and the Evolving Public Transport System                                                14 
2.2 Public Transport Infrastructure and Passenger Facilities                                                   14 
2.3 Optimization of Bus Stop Locations Using Spatial Analysis and K-Means Clustering    15 
2.4 Spatial and Environmental Analysis for Transport Waiting Shed Placement                    15 
2.5 Crowdsourced Data and Monitoring in Public Transport Systems                                    15 
2.6 Drivers’ Perception of Jeepney Modernization                                                                  16 
2.7 Environmental and Comfort Benefits of Transport Waiting Sheds                                   16  
2.8 Climate-Responsive Design of Transport Waiting Shed                                                   17 
2.9 Infrastructure and Commuter Experience ​
​
​
​
​
​
 17 
2.10 Contingent Valuation Method and Willingness to Pay                                                    17 
CHAPTER THREE: METHODOLOGY 
3.1 Research Design                                                                                                                 18 
3.2 Research Setting                                                                                                                 18 
3.3 Sampling Design                                                                                                                19 
3.4 Data Gathering Procedure                                                                                                  20 
3.5 Research Instruments and Standards                                                                                  20 
3.6 Mode of Data Analysis                                                                                                       21 
3.7 Budget Plan​
                                                                                                              22 
3.8 Plan of Implementation                                                                                                      22 
CHAPTER FOUR: EXPECTED RESULTS AND DISCUSSION 
4.1 Socio-Demographic Profile of the Respondents                                                            23 
4.2 Existing Modern Jeepney Routes and Travel Characteristics                                     24 
4.3 Commuter Perception on Fare, Distance, Delay, and Service Satisfaction                 26 
4.4 Contingent Valuation Method (CVM) and Willingness to Pay                                    30 
4.5 Geographic Information System (GIS) Spatial Analysis                                              31 
4.6 K-means Clustering Analysis                                                                                          32 
4 7 Proposed Priority Locations for Modern Passenger Waiting Sheds                           33 
4.8 Summary of Findings                                                                                                         34 
 
BIBLIOGRAPHY                                                                                                                  36 
 
APPENDIX 
APPENDIX A:  Survey Questionnaire (English & Bisaya)                                                    35 
APPENDIX B: Informed Consent Form (English & Bisaya)                                                  38 
APPENDIX C: Curriculum Vitae                                                                                             41 
 
 
1

LIST OF FIGURES AND TABLES 
 
LIST OF FIGURES  
 
Figure 1. Conceptual Framework 
Figure 2. Research Procedure 
Figure 3. Research Setting 
Figure 4. Data Gathering Procedure 
Figure 5. Proposed Project Timeline 
Figure 6. Map of Boarding and Alighting Locations 
Figure 7. Passenger Demand Clusters 
Figure 8. Proposed Passenger Waiting Station Locations 
 
LIST OF TABLES 
 
Table 1. Current Infrastructure vs. Engineering Standards Comparison 
Table 2. Distribution of Respondents by Age Group 
Table 3. Distribution of Respondents by Gender 
Table 4. Frequency of Modern Jeepney Usage 
Table 5. Distribution of Waiting Time 
Table 6. Commuter Willingness to Pay for Waiting Station Improvements 
Table 7. K-means Clustering Results 
Table 8. Table Assessment of Existing Waiting Areas 
Table 9. Proposed Waiting Station Locations 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2

CHAPTER ONE 
THE PROBLEM AND ITS SETTING 
 
1.1 Background of the Study 
 
The Philippine public transportation is currently experiencing significant transitions and 
experiences. These systemic challenges include urban congestion, operational consistency, 
and service reliability (Francisco, 2025). One of the challenges experienced in the Philippines 
in regards to commuting is the lack of unified transport data. This contributes to the 
hindrance of implementation of modernization policies locally (NCTS, 2024). This results in 
the necessity of transformative reforms to uplift the commuter experience. In 2017, the 
government launched the Public Utility Vehicle Modernization Program (PUVMP). With the 
intention not just to change physical aspects of the fleet but also to improve the operations 
and introduce technologies that are necessary for commuter safety and public acceptance 
(Gumasing et al., 2024). The implementation shows success as an evaluation conducted by 
the German Agency for International Cooperation (GIZ, 2019) indicates that there are 
significant performance improvements in operation. The operation on modernized vehicles 
achieved 19 vehicle performing hours versus 14 hours for the traditional routes. This data 
underscores the national strategic shift toward data-driven, quality-based public transport 
assessment. But despite these improvements in transportation by equipping modern jeepneys 
with GPS- telematics systems, a lack of tools for monitoring to assess service improvements. 
(Cunanan, 2025) 
 
Cagayan de Oro city (CDO), a highly urbanized and a gateway city in Northern Mindanao. 
The city is designated as a key area for the implementation of PUVMP (Philippine News 
Agency, 2024). The redefinition starts off with the vehicle type with new, Euro-4 compliant, 
air-conditioned units (Bureau of Philippine standards, 2017). The long-term success of the 
implementation of PUVMP in the CDO does not just solely rely on the physical attributes, 
and facilities of the PUVMP but also critically relies on the operational advantages and 
upgrading the supporting infrastructure, particularly within the six selected barangays that 
experience the highest passenger and traffic volumes. This technological upgrade’s full 
potential is hampered by two core gaps. First is the empirical operational advantages of the 
new fleet; in terms of factors like schedule reliability and travel speed, but remains unverified 
due to a lack of public, quantitative data derived from the integrated GPS/AFCS 
technologies. As studied by Reyes et al. (2023), there is a need for change in methodology 
towards utilizing GPS data progress from subjective observation to objective, engineering 
based indicators, without these data the operational metrics remain unmeasured. to Second, 
the necessary support infrastructure, including designated passenger waiting areas and 
waiting facilities, has not kept pace with vehicle modernization (Agaton, et al., 2023). This 
infrastructural deficiency contributes to operational stagnation and hinders the holistic 
improvement of the commuter experience (Mayo & Taboada, 2021).  
 
To support the sustainable adaptation of the PUVMP in CDO, a quantitative and spatial 
assessment is required. This study addresses the gaps by conducting a Geospatial Analysis of 
the Modern Jeepney system’s performance. By providing evidence-based, and technical data; 
this research aims to assist community stakeholders and local governance. To foresee which 
locations are a priority in developing the placement of passenger facilities - waiting sheds. 
This study aims to suggest which locations to uphold and erect passenger facilities not just 
for the communities but to also refine the overall public transport framework.  
 
3

1.2 Statement of the Problem 
 
The ongoing urbanization and economic growth of Cagayan de Oro City have raised the 
demand for reliable public transportation facilities, especially the modernized Public Utility 
Jeepneys (PUJs), which plays a crucial role in the daily lives of residents of the 6 Selected 
Barangays. These Jeepneys connect people to key destinations like workplaces and markets, 
yet the system’s operational efficiency is often undermined by insufficient support 
infrastructure and outdated planning approaches. Problems such as chaotic boarding and 
alighting procedures, commuters enduring extreme weather without shelter, and persistent 
traffic bottlenecks not only diminish road performances but also jeopardize passenger safety 
and exacerbate congestion. These challenges are further compounded by a scarcity of 
in-depth, data-informed research that examines passenger needs, movement trends, route 
viability, and spatial reach throughout the urban barangay landscape.  
 
Moreover, the lack of passenger facilities like waiting sheds leaves commuters without 
adequate protection, comfort. Existing routes and setups are typically shaped by casual 
observations rather than just systematic analysis, resulting in uneven service distribution and 
inefficiencies that affect everyone’s daily routines. This highlights the urgent need for 
rigorous studies that delve into the working of modern PUJs and offer practical 
recommendations to strengthen infrastructure, making public transport more accessible, 
secure, and environmentally conscious. 
 
This study will evaluate the operational efficiency and supporting structures of the modern 
jeepney system in the 6 Selected Barangays of Cagayan de Oro City. Specifically to address 
the following research questions, aligned with the study’s objectives: 
 
1.​ What are the baseline conditions of the selected barangays in terms of existing 
jeepney routes, road corridors, and commuter infrastructure within the study area? 
2.​ What are the commuters’ perceptions of jeepney routes, trips, and services in terms of 
fare, travel distance, and delays, and what is their willingness to pay (WTP) for 
improved passenger facilities using the contingent valuation (CV) approach? 
3.​ What spatial patterns and cluster of potential passenger facility locations can be 
identified using K-means clustering analysis  
4.​ How can GIS-based spatial mapping be used to identify and visualize recommended 
locations for sheds to support transport planning and decision making? 
 
1.3 Objectives of the Study 
 
The main objective of this study is to develop geospatial analysis of commuter facility and 
prioritization of sites for passenger facilities of Modern Jeepneys in selected barangays in 
Cagayan de Oro City. Moreover, the study will address the following specific objectives, 
namely:  
1.​ To determine baseline data of the selected barangay, the jeepney routes, and the road 
corridor. 
2.​ To conduct commuters’ perception surveys on jeepney routes, trips, and services (fare, 
distance, and delay) using CV and WTP. 
3.​ To determine spatial patterns and clustering of potential facility locations using k-means 
analysis. 
4.​ To develop GIS-based maps on recommended jeepney terminals, loading and unloading 
areas, and waiting stations. 
4

1.4 Significance of the Study 
This study is important because it examines the commuter facilities and jeepney routes from 
Barangay Gusa to Barangay Bugo in Cagayan de Oro City. By using GIS mapping, 
contingency valuation, and K-means clustering, the study identifies areas where commuters 
usually wait, load, and unload. It also helps determine the best locations for passenger 
waiting sheds and transport facilities based on real commuter activity and data. 
Local government units and transport planners, the results of this study can serve as a 
guide in improving transport facilities and organizing jeepney routes in the area. The GIS 
maps and analysis can help them see where commuters gather the most and where passenger 
sheds or loading areas are needed. This can support better planning and decision making for 
public transportation in the city. 
Transport cooperatives and operators, the study can help them understand commuter 
patterns along the Gusa to Bugo route. By knowing where passengers usually wait and travel, 
operators can better manage their routes, stops, and schedules to match commuter demand. 
 
Commuters and residents, the findings of this study may help improve their daily travel 
experience. The recommended locations for waiting sheds and organized loading areas can 
provide safer and more comfortable places for passengers while waiting for jeepneys, 
especially during rain or strong sunlight. 
 
Academic and professional communities, this study can serve as a reference for studies 
related to transportation planning, GIS mapping, and commuter behavior. It shows how 
spatial analysis and data collection can be used to study public transportation and improve 
commuter facilities in urban areas. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
5

1.5 Conceptual Framework 
 
This conceptual framework illustrates an integrated approach to bridging the gap between the 
operational values quantitative and qualitative data. By mapping independent modernization 
variables against intervening constraints operationally, the study designates a data-based 
outcome for infrastructure outcome and improved service quality. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Figure 1. Conceptual Framework 
1.6 Theoretical Framework 
This study is grounded in transportation planning theories that emphasize the importance of 
data-driven infrastructure planning and spatial analysis in improving public transport 
systems. In urban transportation studies, the placement of passenger facilities such as stops 
and waiting stations should be based on commuter demand, accessibility, and spatial 
distribution rather than arbitrary placement. Spatial analysis is commonly used in transport 
planning to understand patterns of commuter movement and identify areas where passengers 
frequently access public transportation. Through geographic information systems (GIS) and 
spatial modeling techniques, transportation planners can analyze the relationship between 
population distribution, road networks, and commuter activity. These tools allow planners to 
identify locations where transportation facilities are most needed. 
One important concept in transport infrastructure planning is commuter accessibility, which 
refers to how easily passengers can reach and use public transportation services. Accessibility 
is influenced by factors such as walking distance to stops, the distribution of passenger 
facilities, and the availability of safe and convenient waiting areas. When transportation 
facilities are poorly distributed, commuters may experience difficulty accessing services or 
may be forced to wait along unsafe roadside locations. 
Another important concept is demand-based infrastructure planning, which focuses on 
identifying areas where passengers frequently gather or wait for transportation. By analyzing 
commuter movement patterns and passenger concentration points, planners can determine 
appropriate locations for transport waiting stations that better serve the needs of the public. In 
relation to this study, spatial analysis methods such as clustering techniques and geographic 
modeling can be used to identify commuter hotspots and service gaps in the selected 
barangays of Cagayan de Oro City. These methods allow researchers to determine areas 
where passenger demand is high and where waiting facilities are currently lacking. By 
6

applying these concepts, the study aims to support the planning of strategically located 
passenger waiting stations that improve accessibility, safety, and comfort for commuters. 
 
1.7 Scope and Limitations 
 
This paper examines how well modernized Public Utility Jeepneys (PUJs) operate and 
determines where passenger waiting stations should be prioritized across six selected 
barangays in Cagayan de Oro City: Gusa, Cugman, Tablon, Agusan, Puerto, and Bugo. These 
specific barangays were selected based on their high commuter volumes, have established 
modernized PUJ routes running through them, and occupy important positions within the 
city’s transportation network. 
 
The operational evaluation concentrates on key transit performance measures such as travel 
time, dwell time, and passenger load factor. Researchers collect information through direct 
field observations and passenger surveys conducted along the selected PUJ routes that serve 
these barangays. This collected data helps analyze both commuter movement patterns and 
how vehicles perform operationally within the study areas. 
 
Using the Geographic Information System (GIS), the research develops visual maps to 
identify and prioritize potential sites where passenger waiting stations may be needed. The 
evaluation particularly emphasizes locations with heavy passenger boarding and alighting 
activity, areas with efficient operations, and spots experiencing high passenger traffic.  
 
However, this study limits itself to spatial planning considerations and does not include 
detailed engineering design, structural analysis, or cost calculations for the proposed waiting 
stations. The research also excludes examination of administrative, financial, or 
organizational aspects related to PUJ industry stakeholders, focusing solely on the current 
PUJ operational analysis. Additionally, the findings apply specifically to the selected 
barangays and may be influenced by various factors such as data limitations, survey response 
quality, traffic conditions, and changing operational conditions.  
 
1.8 Definition of Terms 
 
Average Travel Speed - The mean speed of a Public Utility Jeepney along a route, calculated 
as the total route distance divided by total travel time, including delays. It is used as an 
indicator of operational efficiency. 
 
Commuter Accessibility – The measured ease of reaching and using a stop, quantified using 
Voronoi Diagrams to determine the effective catchment area of existing stops. Locations 
outside the theoretical catchment are classified as service gaps. 
 
Commuter Demand Patterns – The spatial and temporal concentration of commuters, 
identified through K-means Clustering applied to the origin and destination coordinates 
provided in the commuter survey. The patterns also include the perceived service quality 
variables measured via the commuter survey. 
 
7

Local Public Transport Route Plan (LPTRP) – The policy framework and guideline issued 
by the local government to regulate PUJ routes, stops, terminals, and supporting facilities to 
ensure efficient, safe, and organized public transport services. 
 
Modernized Public Utility Jeepneys (PUJs) – A public transportation vehicle upgraded 
under the Philippine Public Utility Vehicle Modernization Program, equipped with improved 
safety features, cleaner engines, and modern technology. 
 
Operational Efficiency Indicators - Quantitative measures (speed, dwell time, headway 
variation, load factor) used to evaluate PUJ service performance. 
 
Operational Performance – The measured efficiency of PUJs using three key performance 
indicators (KPIs) derived from GPS telematics data: (1) Headway Variation (consistency of 
unit arrival spacing), (2) Average Travel Speed (travel time over distance), and (3) Dwell 
Time (average time spent at designated stops).  
 
Passenger Hotspot - A location with a high concentration of boarding and alighting 
passengers identified through spatial clustering.  
 
Waiting Stations – A designated space where commuters can safely wait for public 
transportation while being protected from weather conditions such as rain or heat. 
 
Peak Hour - Periods of highest travel demand, typically during morning and evening 
commuting times. 
 
Route Adherence - The extent to which PUJs follow their designated routes and authorized 
stopping points. 
 
Service Coverage Area - The geographic area within a reasonable walking distance served 
by an existing PUJ stop. 
 
Service Quality – The composite score of commuter satisfaction and perception derived 
from the Partial Least Squares Structural Equation Modeling (PLS-SEM) analysis. This score 
is based on the responses to the 24 perception questions in the Commuter Survey. 
 
Service Gap - An area outside the effective service coverage where commuters lack adequate 
access to PUJ stops or facilities. 
 
Simulation-Based Validation - The process of testing proposed facility locations using 
spatial and operational models to verify feasibility and effectiveness. 
K-Means Clustering – A spatial analysis method that groups data points based on their 
similarity or proximity. In this study, it is used to identify commuter hotspots where 
passengers frequently gather. 
Spatial Clustering - A GIS technique that groups locations based on spatial proximity to 
identify patterns such as demand concentrations. 
 
8

Stakeholder Consultations – Meetings and discussions with relevant parties, including local 
government units (LGUs), transport operators, commuter representatives, and associations, to 
validate findings, gather input, and ensure the feasibility of proposed interventions. 
 
Support Infrastructure – The physical facilities along the selected routes, assessed through 
Baseline Data Collection. This includes the mapped presence, the condition, and availability 
of existing waiting stations, designated loading/unloading zones, and route-specific traffic 
signage. 
 
Traffic Flow Patterns – The movement dynamics of vehicles and pedestrians within the 
study area, including congestion points, bottlenecks, and travel delays affecting PUJ 
operations.  
 
Geographic Information System (GIS) – A computer-based tool used to collect, analyze, 
and visualize spatial or geographic data. In this study, GIS is used to analyze commuter 
locations and identify suitable sites for passenger waiting stations. 
 
Contingent Valuation Method (CVM) - A survey method used to estimate how much 
people value a service or improvement by asking them how much they would be willing to 
pay for it in a given situation. 
 
Willingness to Pay (WTP) - The maximum amount of money that a person is willing to pay 
for a service, facility, or improvement based on its perceived value. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
9

CHAPTER TWO 
REVIEW OF RELATED LITERATURES AND STUDIES 
 
2.1 Modernization and the Evolving Public Transport System 
 
Public transportation in the Philippines has been undergoing major changes due to the 
implementation of the Public Utility Vehicle Modernization Program (PUVMP). This study 
aims to replace older jeepney units with modern vehicles that meet updated safety, 
environmental, and operational standards (Gatarin, 2024; Zulueta, 2024). The modernization 
study also seeks to improve the overall quality of transport services by introducing better 
route management, improved passenger comfort, and more efficient vehicle operations 
(Zulueta, 2024). 
 
According to Gatarin (2024), the success of the modernization program does not depend only 
on replacing old jeepneys with new vehicles. It also requires proper infrastructure, route 
rationalization, and coordination among stakeholders such as transport operators, government 
agencies, and commuters. Without these supporting elements, modernization may not achieve 
its intended improvements in service quality and transport efficiency (Gatarin, 2024). 
 
Studies have also shown that infrastructure limitations remain a major challenge in many 
Philippine cities. Many commuters still wait along roadsides without proper passenger 
facilities, which exposes them to heat and rain while also contributing to traffic congestion 
when vehicles stop randomly to load passengers (Macalalad et al., 2021; Ranosa et al., 2017). 
These issues demonstrate that improving both transport vehicles and commuter infrastructure 
is essential for creating a more reliable and organized public transportation system (Zulueta, 
2024; Gatarin, 2024). 
 
2.2 Public Transport Infrastructure and Passenger Facilities 
 
Passenger infrastructure plays an important role in improving the efficiency and comfort of 
public transportation systems. Facilities such as waiting sheds, designated loading zones, and 
organized stops help manage commuter flow and reduce traffic disruptions (Macalalad et al., 
2021; Santos et al., 2020). When these facilities are properly designed and strategically 
located, they help improve both commuter experience and transport efficiency (Santos et al., 
2020). 
 
According to Macalalad et al. (2021), the absence of proper waiting areas can negatively 
affect commuter satisfaction. Passengers who are forced to wait without shade or shelter 
often experience discomfort due to extreme heat, rain, or other weather conditions. This 
situation can discourage commuters from using public transportation and may reduce the 
effectiveness of modernization programs (Macalalad et al., 2021). 
 
Ranosa et al. (2017) also highlighted that the concentration of passenger loading and 
unloading in certain areas can cause operational delays and traffic congestion. Their findings 
emphasize that proper infrastructure planning, including well-placed passenger facilities, is 
necessary to improve service reliability and commuter convenience (Ranosa et al., 2017). 
 
2.3 Optimization of Bus Stop Locations Using Spatial Analysis and K-Means Clustering 
 
10

The placement of bus stops and waiting sheds should be based on commuter demand and 
travel patterns. A study on bus stop optimization used spatial analysis combined with the 
K-means clustering method to determine areas with high passenger activity. This approach 
groups demand nodes based on their spatial distribution, allowing planners to identify 
optimal stop locations (Optimization Study, n.d.). 
 
By identifying natural clusters of commuter activity, transport planners can reduce redundant 
stops while ensuring that passengers remain well served by the transport network. This 
approach also helps determine where infrastructure such as waiting sheds and loading areas 
will have the greatest operational impact (Optimization Study, n.d.). 
 
Applying clustering methods to the modern jeepney system can help identify high-demand 
commuter areas, especially during peak hours. These insights allow planners to strategically 
place waiting sheds in locations where passengers frequently gather, thereby reducing 
walking distances and preventing overcrowding at existing stops (Optimization Study, n.d.; 
Santos et al., 2020). 
 
2.4 Spatial and Environmental Analysis for Transport Waiting Shed Placement 
 
The placement of transport shelters must also consider environmental and spatial factors. 
Santos et al. (2020) developed a framework for evaluating the optimal placement of bus 
shelters using geospatial analysis. Their study examined bus stop locations and used digital 
surface models to analyze shading, sunlight exposure, and surrounding urban structures 
(Santos et al., 2020). 
 
The study demonstrated that environmental conditions can significantly influence the 
effectiveness of passenger shelters. Stops that lack proper shade or protection may expose 
commuters to extreme weather conditions, reducing the comfort of waiting passengers 
(Santos et al., 2020). 
 
By combining spatial distribution data, environmental analysis, and commuter activity 
patterns, transport planners can identify locations where shelters will provide the greatest 
benefit. This type of data-driven planning approach ensures that commuter facilities are 
placed in areas where they are most needed (Santos et al., 2020; Macalalad et al., 2021). 
 
2.5 Crowdsourced Data and Monitoring in Public Transport Systems 
 
Modern transportation planning increasingly uses crowdsourced data to monitor transport 
operations and commuter behavior. According to Delgra et al. (2019), crowdsourced 
information collected from commuters and transport operators can provide real-time insights 
into transport system performance. 
 
This type of data allows transport agencies to identify operational issues such as service 
delays, passenger congestion, and high-demand stops more quickly than traditional 
monitoring methods (Delgra et al., 2019). The use of crowdsourced transport data also 
improves transparency and encourages collaboration between commuters, operators, and 
government agencies (Delgra et al., 2019). 
 
Integrating crowdsourced information into transport planning can help identify areas where 
commuters frequently wait for vehicles. These insights can support the strategic placement of 
11

waiting sheds and other passenger facilities, ensuring that infrastructure improvements 
respond to actual commuter needs (Delgra et al., 2019; Santos et al., 2020). 
2.6 Drivers’ Perception of Jeepney Modernization 
 
The success of the jeepney modernization study also depends on the acceptance of drivers 
and transport operators. Savilla et al. (2024) examined the perceptions of jeepney drivers 
regarding the modernization program in Indang, Cavite. Their study evaluated drivers’ views 
on financial requirements, employment opportunities, and vehicle improvements. 
 
The results showed that many drivers expressed concerns about the financial burden 
associated with modernization, particularly regarding vehicle costs, loan payments, and 
income stability (Savilla et al., 2024). These financial concerns contribute to resistance 
among some drivers toward the modernization program (Savilla et al., 2024; Gatarin, 2024). 
 
However, the study also found that some drivers acknowledged the benefits of 
modernization, such as improved vehicle safety, passenger comfort, and technological 
features like GPS tracking and automated fare collection systems (Savilla et al., 2024). 
Despite these advantages, financial and livelihood concerns remain significant barriers to the 
full acceptance of modernization efforts (Savilla et al., 2024; Gatarin, 2024). 
 
2.7 Environmental and Comfort Benefits of Transport Waiting Sheds 
 
Public transport modernization also has important environmental and health benefits. 
Macalalad et al. (2021) emphasized that transitioning to modern public transport systems can 
reduce harmful emissions and improve air quality. These environmental improvements can 
contribute to better public health and a more sustainable urban transport system (Macalalad et 
al., 2021). 
 
However, the study also highlighted that infrastructure improvements must accompany 
vehicle modernization. Passenger waiting areas such as bus stops and jeepney sheds are 
necessary to ensure commuter comfort and accessibility (Macalalad et al., 2021). 
 
Proper waiting sheds provide protection from heat, rain, and other weather conditions. In 
tropical countries like the Philippines, this protection is particularly important because 
commuters often experience long waiting times under extreme weather conditions (Macalalad 
et al., 2021; Santos et al., 2020). 
 
2.8 Climate-Responsive Design of Transport Waiting Shed 
 
Recent research has explored innovative designs for public transport shelters that improve 
thermal comfort. Montero-Gutiérrez et al. (2023) developed a climate-responsive bus stop 
shelter that integrates radiant cooling systems powered by renewable energy sources. 
 
Their experimental results showed that these systems significantly reduced surface 
temperatures and improved passenger comfort, even under high ambient temperatures 
(Montero-Gutiérrez et al., 2023). The cooling system reduced perceived thermal discomfort 
among passengers waiting at transport stops (Montero-Gutiérrez et al., 2023). 
 
These findings suggest that modern transport waiting sheds can be designed to improve not 
only 
protection 
from weather but also overall commuter comfort. Integrating 
12

climate-responsive design features such as shading, ventilation, and renewable energy 
technologies can significantly improve the usability of waiting sheds in hot urban 
environments (Montero-Gutiérrez et al., 2023; Macalalad et al., 2021). 
 
2.9 Infrastructure and Commuter Experience 
 
Infrastructure quality strongly influences commuter satisfaction and public transport usage. 
Zulueta (2024) found that commuter satisfaction with modern public utility jeepneys is 
strongly related to service reliability, safety, and passenger comfort. 
 
However, the study also identified several operational inefficiencies that discourage 
commuters from consistently using modern jeepneys, including inconsistent route 
assignments and limited service coverage (Zulueta, 2024). These issues highlight the need for 
better transport planning and infrastructure support. 
 
Similarly, Gatarin (2024) emphasized that modernization programs often face implementation 
challenges due to inadequate infrastructure, lack of coordination among stakeholders, and 
incomplete route rationalization. Without proper passenger facilities such as organized stops 
and waiting sheds, even modern vehicles may fail to provide efficient services (Gatarin, 
2024). 
 
These findings suggest that improving commuter infrastructure is essential for the success of 
modernization programs. Properly planned waiting sheds, organized transport stops, and 
well-designed passenger facilities can enhance commuter experience and support the overall 
efficiency of the modern jeepney system (Zulueta, 2024; Gatarin, 2024; Macalalad et al., 
2021). 
 
2.10 Contingent Valuation Method and Willingness to Pay 
The Contingent Valuation Method (CVM) is a survey method used to estimate how much 
people are willing to pay (WTP) for improvements in public services or facilities. It is often 
used when the service being studied does not have a clear market price. By asking people 
questions about how much they would pay for certain improvements, researchers can 
understand how valuable the service is to them. 
 
In transportation studies, CVM has been used to measure how much commuters are willing to 
pay for better transportation services. Saptutyningsih and Karimah (2019) used the contingent 
valuation method to estimate the willingness of passengers to pay for improvements in public 
transportation. Their study found that factors such as comfort, service quality, travel time, and 
passengers’ income affect how much commuters are willing to pay. This means that when 
transportation services become more comfortable and reliable, commuters may be more 
willing to pay for the improvements. 
 
CVM has also been used in studies in the Philippines. Fujii et al. (2016) studied the 
willingness of households in Metro Manila to pay for improved sewerage and sanitation 
services. The results showed that people’s knowledge, awareness, and economic condition 
can influence their willingness to pay for better public services. This study shows that 
understanding people’s opinions and financial capacity is important when planning 
improvements in public infrastructure. 
 
13

CHAPTER THREE 
METHODOLOGY 
 
3.1 Research Design 
 
This study adopts a descriptive-analytical research design integrating primary data and 
secondary data supported by geospatial analysis to evaluate modern PUJ operations and 
identify priority locations for passenger waiting sheds in selected barangays of Cagayan de 
Oro City. 
 
 
Figure 2. Research Procedure 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
14

3.2 Research Setting 
 
This study is centered on six barangays in Cagayan de Oro City, selected based on their large 
population, major PUJ routes, high commuter volumes, varied land areas and road conditions. 
These barangays also exhibit active PUJ corridors that are essential for assessing operational 
performance and commuter accessibility. The chosen barangays are Gusa, Cugman, Tablon, 
Agusan, Puerto, and Bugo.  
 
 
 
 
Figure 3. Research Setting 
3.3 Sampling Design 
 
The study adopts a non-probability approach incorporating spatial stratification and 
convenience sampling techniques to ensure representation of different commuter groups 
while maintaining feasibility.  
 
The spatial sample is categorized by a 250-meter buffer zone along the National Highway, 
which serves as the primary corridor of PUJ operations. Within this buffer, respondents are 
selected from areas with high commuter activity, including roadside loading and unloading 
zones, commercial centers, public markets, and locations near schools and workplaces. 
 
In order to get a representative sample of commuters, survey questionnaires will be given out 
across the chosen barangays; Gusa, Cugman, Tablon, Agusan, Puerto, and Bugo. The sample 
group will be chosen at varying times of the day, i.e. morning, midday and afternoon, such 
that variations in the amount of passenger demand and commuting patterns would be 
15

captured. This will enable the research to get a wide variation of responses and mark down 
the frequent boarding/alighting points that will be used further to have a spatial analysis. 
 
The sample size was determined based on feasibility, time constraints, and the need to obtain 
sufficient representation of commuters across the identified barangays. A minimum of 100 
respondents will be targeted, with respondents proportionally distributed across the selected 
locations and time periods to ensure balanced data collection. Only respondents who are 18 
years old and above will be included in the study. 
 
The inclusion criteria for this study require that respondents be commuters who regularly use 
public utility jeepneys within the identified study area. Conversely, individuals who do not 
use jeepney transportation or are unwilling to participate are excluded from the study. 
 
The information gathered will involve the normal boarding and alighting points of the 
respondents, their waiting period in jeepneys and participation in enhancing passenger 
facilities. These reactions will comprise the major data set in the form of descriptive 
statistical analysis, contingent valuation test and geospatial assessment to be conducted in the 
research. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
16

3.4 Data Gathering Procedure 
 
This study employs a combination of descriptive, spatial, and integrative analysis to evaluate 
modern PUJ service conditions and to identify priority locations for passenger jeepney 
terminals, loading and unloading areas, and waiting stations in the selected barangays of 
Cagayan de Oro City. The analysis integrates both primary and secondary data to ensure 
consistency with commuter experience and local transport planning policies.  
 
 
 
 
Figure 4. Data Gathering Procedure 
 
 
The study will begin by collecting baseline data from the chosen 6 barangays; Gusa, Cugman, 
Tablon, Agusan, Puerto, and Bugo. Data obtained from the Local Public Transport Route 
Plan (LPTRP), barangay profiles, and route network maps are analyzed using descriptive and 
spatial methods. Authorized PUJ routes, terminals, and designated stopping areas are 
digitized and mapped using GIS to establish the official service coverage within the study 
area. Barangay-level data on population and land use are used to contextualize commuter 
demand and identify areas with high activity potential.  
 
17

Field observation data are analyzed qualitatively and spatially to assess the presence, 
condition, and adequacy of existing waiting stations and informal boarding locations. 
Observed safety and accessibility issues are documented to support spatial interpretation of 
commuter demand patterns. Moreso, proposed identifications of spots for loading and 
unloading locations, waiting areas, and terminals will be identified.   
 
Geospatial analysis is conducted using GIS software to integrate primary and secondary 
datasets into a unified spatial database. A 250-meter buffer around these coordinates will be 
applied to facility gaps. Boarding and alighting locations identified from commuter surveys 
are georeferenced and subjected to K-means clustering to identify passenger demand 
hotspots. This method groups areas with high commuter concentration and highlights 
locations where passenger facilities are most needed. 
 
Authorized PUJ routes and existing passenger facilities are overlaid with the clustered 
demand points to assess spatial coverage and identify service gaps. Areas where high 
passenger demand coincides with the absence or inadequacy of waiting facilities are 
classified as priority zones. 
 
To validate the data, commuter surveys are coded and summarized using descriptive statistics 
to determine prevailing patterns in boarding and alighting behavior, waiting conditions, 
perceived safety, comfort, and accessibility. Willingness to Pay (WTP) responses are 
analyzed using frequency distributions and central tendency measures to assess commuter 
acceptance of improved passenger waiting facilities. 
 
The survey questionnaire will be prepared using both English and Bisaya languages to ensure 
clarity and ease of understanding among respondents in the study area. English will be used 
as the primary language of the instrument, while Bisaya translations will be provided for each 
question to accommodate local commuters who are more comfortable with the regional 
language. 
 
Priority locations for commuter facilities are determined through overlay analysis by 
considering the following criteria: high concentration of commuter demand based on 
clustering results, absence or poor condition of existing waiting facilities, and proximity to 
authorized PUJ routes under the Local Public Transport Route Plan (LPTRP). 
 
In addition to identifying priority locations, the study establishes a classification framework 
to determine the appropriate type of facility to be installed at each site, whether a waiting 
station, loading and unloading area, or terminal. This classification is based on the level of 
passenger demand, spatial characteristics, and operational function of the location. Areas 
identified with high passenger concentration and prolonged waiting time but without 
organized stopping behavior are classified as priority locations for waiting stations. Locations 
where frequent boarding and alighting activities cause roadside congestion and irregular 
stopping patterns are designated as loading and unloading zones. Meanwhile, areas that serve 
as major origin or destination points of routes, where multiple units start, end, or dwell for 
extended periods, are classified as terminals. This decision framework ensures that each 
proposed facility type is appropriate to the observed commuter behavior and transport 
operations, thereby improving both efficiency and commuter experience. 
 
This approach ensures that recommended locations are demand-responsive, spatially 
justified, and aligned with local transport policies. 
18

The identified priority locations are validated through field observations and consistency 
checks with LPTRP provisions to ensure practical feasibility and compliance with existing 
route plans. The results from descriptive analysis, spatial clustering, and policy alignment are 
synthesized to support evidence-based recommendations for passenger waiting station 
placement and improvements in PUJ service accessibility. 
 
3.5 Research Instruments and Standards 
 
The research instruments to be used in this study in collecting data include three main 
instruments namely survey questionnaires, field observation sheets, and secondary data 
records. 
 
The main tools utilized in the research is a structured commuter survey questionnaire that will 
be used to communicate data on passenger travel behavior, waiting experience, and views on 
the current jeepneys services. The survey will have four items, including profile of the 
respondents, commuting, quality of service perception, and readiness to spend money on 
better passenger waiting areas. These perception questions identify the variables of the 
perception of comfort, safety, accessibility, reliability, and waiting experience on a five-point 
Likert scale, which would have a strongly disagree to strongly agree scale. 
 
The survey also considers Contingent Valuation (CV) and Willingness-To-Pay (WTP) 
questions to determine the commuter acceptance of the improved facilities and the 
respondents are asked to give the amount they can give in case of improved passenger 
waiting stations. This is a standard approach to evaluating the value of service enhancements 
by users in transportation research. 
 
Field observation checklists will also be used in order to carry out systematic recording of the 
physical conditions and availability of passenger waiting stations, loading and unloading 
points, pedestrian accessibility, and safety conditions at target locations. The investigators 
will carry out observations as part of site visits in each barangay. 
 
To provide some contextual information about the current PUJ routes and infrastructure in the 
area of study, secondary data will be collected by local government repositories, such as 
barangay profiles, route maps, and LPTRP. 
 
All the study tools will be in line with established ethical principles in academic research. 
Respondents are free to take part in the survey, and no personal identifying information 
disclosure is obligatory. The research will adhere to the stipulations of the Data Privacy Act 
of 2012 to maintain confidentiality and handling of data in a responsible manner. 
 
Participants will not receive any monetary or material compensation for their participation in 
the study. Their involvement is entirely voluntary. 
 
The researchers will provide an informed consent form to all participants before the survey is 
conducted. The form will explain the purpose of the study, procedures involved, voluntary 
nature of participation, and assurance of confidentiality. Participants will be given sufficient 
time to read and understand the information before agreeing to take part in the study. The 
study involves minimal risk to participants as it only requires them to answer a survey 
19

questionnaire about their commuting experience. Possible risks may include slight 
inconvenience, time consumption, or minor discomfort in answering some questions. 
Participants will have the right to withdraw from the study at any point without any penalty 
or consequence. If a participant chooses to withdraw, any data provided by the participant 
will be excluded from the analysis upon request. The researchers will respect the decision of 
the participants and ensure that their rights are protected throughout the study. The 
participants have the right to access their own responses and records related to the study upon 
request, subject to reasonable conditions and data privacy regulations. 
 
3.6 Mode of Data Analysis 
 
The data of the study will be analyzed using descriptive statistics, contingent valuation, and 
GIS. These procedures will evaluate commuter behavior, plot passenger demand and identify 
priority locations of waiting stations in the chosen barangays in Cagayan de Oro City. 
 
The summaries of the commuter survey will be first described using descriptive statistics. 
The outcomes will be presented in the form of frequency tables, percentages, and averages 
that will give a general picture of commuting conditions. Some of the variables that we will 
look at include waiting time, boarding sites, and travel behavior in order to present a clear 
picture of the commuting experience. The collected data will be used strictly for academic 
purposes and will not be shared with third parties without permission. 
 
In order to estimate the importance, the commuters attach to the improved facilities, we will 
use the Contingent Valuation Method (CVM). This approximates readiness to pay the 
enhancement such as waiting stations. We shall interpret the survey data using descriptive 
statistics and identify the mean willingness to pay and support of the proposed upgrades. 
 
Passenger activity will be mapped with the help of GIS software, including QGIS or ArcGIS. 
The surveys will be converted into boarding and alighting spots, which will be used to create 
the coordinates and plotted on a digital map of the study area. This mapping allows scholars 
to observe cartographic relations, as well as identify where the facilities are in most demand. 
 
K-means clustering of the georeferenced information will then be used. These clusters point 
together by distance and relatedness demonstrating an agglomeration of demand. The 
algorithm will determine three clusters of high, moderate, and low demand which will 
indicate hotspots that must be given priority when new waiting stations are being set up. 
 
Lastly, we will integrate clustering findings and survey data to make data-driven decisions. 
The study will be used to locate strategic points to position passenger waiting stations in 
order to improve safety, accessibility and general efficiency of the transport modes within the 
selected barangays by incorporation of the demand patterns, willingness to pay information 
and spatial clusters. 
 
 
 
 
 
 
 
 
20

3.7 Budget Plan  
 
Following is Table 1 for the estimated budget plan for the duration of the study; 
Table 1. Budget Plan 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3.8 Plan of Implementation 
 
Figure 5 indicates the intended schedule of the research. The schedule starts in December 
2025 and ends in November 2026. The research will launch in December 2025. During this 
month, the research proposal will be prepared, and questionnaires on survey questions will be 
formulated. A budget of 10,000 Philippine peso will be allocated for this study. From the 
initial planning phase to survey printing/administration costs, and preliminary travel expenses 
for field assessment. The survey questionnaires will be worked on until January 2026, 
confirming coverage of all research variables. The survey questionnaires will be handed over 
and collected between June and July 2026, whereas a key informant interview will be carried 
out to ensure that the stakeholders' feedback is obtained. 
 
To support and corroborate the previous data, further data collection will be implemented in 
July 2026. All the acquired information will be computed and analyzed within the timeframes  
of August to September 2026 to obtain meaningful outcomes. Lastly, the Final Report will be 
drafted between October and November 2026, and the compilation of all findings, analyses, 
and recommendations will take place, to be submitted and presented. 
 
 
 
 
 
 
 
 
 
 
21 
 
I.​
Fieldwork and Data Collection 
A.​ Transportation (Land Travel) 
B.​ Survey Questionnaires 
II.​
Research Materials 
A.​ Final paper 
B.​ Printer Ink 
C.​ Bondpaper 
 
₱ 3,000.00 
₱ 3,000.00 
 
₱ 1,500.00 
₱ 2,000.00 
₱    500.00 
TOTAL:  
₱ 10,000.00

Figure 5.Proposed Project Timeline 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
22 
 
2025 
2026 
ACTIVITY 
DEC 
JAN 
FEB 
MAR 
APR 
MAY 
JUN 
JUL 
AUG 
SEP 
OCT 
NOV 
Research Proposal 
 
 
 
 
 
 
 
 
 
 
 
 
Survey Questionnaires 
Formulation 
 
 
 
 
 
 
 
 
 
 
 
 
Draft of Questionnaire 
and IREB 
 
 
 
 
 
 
 
 
 
 
 
 
Research Ethics Office 
Submission: Review and 
Revision  
 
 
 
 
 
 
 
 
 
 
 
 
Baseline Data Collection 
 
 
 
 
 
 
 
 
 
 
 
 
Data Collection: GPS 
Telematics  
 
 
 
 
 
 
 
 
 
 
 
 
Deployment of  
Questionnaire for 
Commuter 
 
 
 
 
 
 
 
 
 
 
 
 
Distribution Of 
Questionnaires for 
Operators and drivers 
 
 
 
 
 
 
 
 
 
 
 
 
Collection Of Survey 
Questionnaires 
 
 
 
 
 
 
 
 
 
 
 
 
Data Collection  
 
 
 
 
 
 
 
 
 
 
 
 
Computation/ Data 
Analysis  
 
 
 
 
 
 
 
 
 
 
 
 
Drafting Of Final Report

CHAPTER FOUR 
EXPECTED RESULTS AND DISCUSSION 
 
4.1 Socio-Demographic Profile of the Respondents 
 
This section presents the demographic characteristics of the respondents who participated in 
the survey. Understanding the age and occupation of commuters provides important 
background information that helps explain travel behavior and transportation preferences. 
These variables also establish whether the survey respondents adequately represent the major 
users of modern jeepney transportation along the study corridor. 
 
4.1.1 Age Distribution of Respondents 
Table 2. Age Distribution of Respondents 
 
Age Group 
Frequency Percentage (%) 
Below 18 
22 
5.71 
18–25 
186 
48.31 
26–35 
84 
21.82 
36–45 
56 
14.55 
46 years old and above 37 
9.61 
Total 
385 
100.00 
 
Table 4.1 presents the age distribution of the 385 respondents who regularly commute using 
modern jeepneys along the Barangay Gusa to Barangay Bugo corridor. The largest proportion 
of respondents belonged to the 18–25 years old age group, comprising 186 respondents or 
48.31% of the total sample. This indicates that nearly one-half of the commuters are young 
adults who regularly depend on public transportation for educational, employment, and 
personal travel purposes. 
 
The 26–35 years old age group accounted for 84 respondents (21.82%), followed by 
commuters aged 36–45 years old with 56 respondents (14.55%). Meanwhile, respondents 
aged 46 years old and above represented 9.61% of the total respondents, while only 5.71% 
were below eighteen years old. 
 
The results suggest that modern jeepneys primarily serve economically active individuals and 
students, which is consistent with the presence of educational institutions, commercial 
establishments, and employment centers along the Gusa–Bugo transportation corridor. 
Consequently, improvements to commuter facilities are expected to benefit the largest 
segment of regular public transport users. 
 
 
 
 
 
23

4.1.2 Occupation of Respondents 
 
Table 4.2 Occupation of Respondents (n = 385) 
 
Occupation 
Frequency Percentage (%) 
Student 
165 
42.86 
Private Employee 
109 
28.31 
Government Employee 
33 
8.57 
Self-employed / Business Owner 46 
11.95 
Homemaker / Unemployed 
21 
5.45 
Others 
11 
2.86 
Total 
385 
100.00 
 
Table 4.2 presents the occupational profile of the respondents. Students comprised the largest 
group with 165 respondents (42.86%), followed by private sector employees with 109 
respondents (28.31%). Self-employed individuals accounted for 46 respondents (11.95%), 
while government employees represented 33 respondents (8.57%). 
 
Only 21 respondents (5.45%) identified themselves as homemakers or unemployed, whereas 
11 respondents (2.86%) belonged to other occupational categories. 
 
The results indicate that students and employed individuals constitute the primary users of 
modern jeepney transportation within the study area. Their daily dependence on public 
transportation highlights the importance of reliable transport services, efficient travel times, 
and adequate waiting facilities. Since these commuters travel regularly, improvements in 
transportation infrastructure have the potential to significantly enhance accessibility, safety, 
and commuting convenience. 
 
4.2 Existing Modern Jeepney Routes and Travel Characteristics 
 
This section presents the travel characteristics of respondents, including the modern jeepney 
routes utilized, boarding locations, and destination points. These data establish the spatial 
travel patterns of commuters and provide the basis for subsequent Geographic Information 
System (GIS) analysis and K-means clustering. 
 
 
 
 
 
 
 
 
 
24

4.2.1 Modern Jeepney Routes Utilized 
 
Table 4.3 Modern Jeepney Routes Frequently Used by Respondents 
 
Route 
Frequency Percentage (%) 
Bugo–Cogon 
137 
35.58 
Gusa–Cogon 
112 
29.09 
Puerto–Cogon 
78 
20.26 
Other Modern Jeepney Routes 58 
15.06 
Total 
385 
100.00 
 
Table 4.3 summarizes the modern jeepney routes most frequently utilized by the respondents. 
The Bugo–Cogon route recorded the highest number of commuters with 137 respondents 
(35.58%), followed by the Gusa–Cogon route with 112 respondents (29.09%). Meanwhile, 
Puerto–Cogon accounted for 20.26%, while the remaining respondents used other authorized 
modern jeepney routes. 
 
The findings indicate that commuter demand is concentrated along routes connecting eastern 
residential barangays to the central business district of Cagayan de Oro City. These routes 
experience continuous passenger movement throughout the day and therefore require 
efficient passenger loading facilities and improved waiting areas to accommodate commuter 
demand. 
 
4.2.2 Boarding Locations of Respondents 
 
Table 4.4 Common Boarding Locations 
 
Barangay Frequency Percentage (%) 
Bugo 
83 
21.56 
Puerto 
73 
18.96 
Gusa 
70 
18.18 
Tablon 
62 
16.10 
Cugman 
54 
14.03 
Agusan 
43 
11.17 
Total 
385 
100.00 
 
The spatial distribution of boarding locations reveals that Bugo recorded the highest number 
of boarding passengers, accounting for 21.56% of the respondents. Puerto and Gusa followed 
25

with 18.96% and 18.18%, respectively. These findings suggest that the eastern section of the 
study corridor serves as a major origin point for commuters traveling toward commercial and 
institutional areas. 
 
The concentration of boarding activity in these barangays indicates increased demand for 
organized passenger waiting facilities. Existing roadside waiting practices observed in these 
locations may contribute to traffic interruptions and reduced commuter safety, emphasizing 
the need for designated waiting sheds and loading areas. 
 
4.2.3 Destination (Alighting) Locations 
 
Table 4.5 Common Destination Locations of Respondents 
 
Destination 
Frequency Percentage (%) 
Cogon Commercial District 134 
34.81 
Puerto 
69 
17.92 
Bugo 
42 
10.91 
Agusan 
40 
10.39 
Tablon 
37 
9.61 
Cugman 
35 
9.09 
Gusa 
28 
7.27 
Total 
385 
100.00 
 
As shown in Table 4.5, the Cogon Commercial District emerged as the most common 
destination, representing 34.81% of all respondents. This finding confirms that the majority 
of commuters travel toward the city's principal commercial and employment center. The 
remaining destinations were distributed among the six barangays included in the study, 
reflecting both inbound and outbound travel patterns. 
 
The spatial distribution of destination points demonstrates that commuter movements are 
highly concentrated along the National Highway corridor, particularly toward areas 
characterized by commercial establishments, educational institutions, and government 
offices. These travel patterns provide an important foundation for the GIS-based hotspot 
analysis and K-means clustering presented in the succeeding sections of this chapter. 
 
4.3 Commuter Perception on Fare, Distance, Delay, and Service Satisfaction 
 
This section presents the respondents' perceptions regarding the affordability of modern 
jeepney fares, estimated travel distance, travel delays experienced during peak hours, and 
their overall level of satisfaction with selected service attributes. These findings address the 
second objective of the study, which seeks to evaluate commuter perceptions of the current 
modern jeepney transportation system. 
26

4.3.1 Modern Jeepney Fare 
 
Table 4.6 Distribution of Respondents According to Fare Paid (n = 385) 
 
 
Fare Category 
Frequency Percentage (%) 
Minimum Fare (₱15.00) 132 
34.29 
₱16.00–₱25.00 
168 
43.64 
₱26.00–₱35.00 
64 
16.62 
More than ₱35.00 
21 
5.45 
Total 
385 
100.00 
 
Table 4.6 presents the fare distribution of the respondents. The majority of commuters 
(43.64%) reported paying between ₱16.00 and ₱25.00 per trip. Meanwhile, 34.29% paid only 
the minimum fare of ₱15.00, while fewer respondents paid higher fares due to longer travel 
distances. 
 
The results indicate that most commuters travel moderate distances within the study corridor. 
Despite recent fare adjustments under the Public Utility Vehicle Modernization Program, the 
fare structure remains generally acceptable to commuters, particularly when compared to the 
convenience and comfort offered by modern jeepneys. 
 
4.3.2 Estimated Travel Distance 
 
Table 4.7 Estimated Travel Distance per Trip 
 
Distance Category Frequency Percentage (%) 
Less than 4 km 
82 
21.30 
4 km–8 km 
185 
48.05 
More than 8 km 
118 
30.65 
Total 
385 
100.00 
 
As shown in Table 4.7, nearly half of the respondents (48.05%) traveled between 4 and 8 
kilometers during a single trip. Approximately 30.65% traveled more than 8 kilometers, 
while only 21.30% traveled less than 4 kilometers. 
 
These findings demonstrate that the majority of commuters depend on modern jeepneys for 
medium- to long-distance travel. Consequently, passenger comfort, efficient travel time, and 
the availability of adequate waiting facilities become increasingly important, particularly for 
commuters who spend considerable time traveling each day. 
 
27

4.3.3 Travel Delay Experienced During Peak Hours 
 
Table 4.8 Average Delay Experienced During Peak Hours 
 
Delay Category 
Frequency Percentage (%) 
Minimal Delay (0–5 minutes) 
48 
12.47 
Moderate Delay (6–15 minutes) 
163 
42.34 
Heavy Delay (16–30 minutes) 
126 
32.73 
Severe Delay (More than 30 minutes) 48 
12.47 
Total 
385 
100.00 
 
The results indicate that 42.34% of respondents experienced delays ranging from 6 to 15 
minutes, while 32.73% experienced delays between 16 and 30 minutes during peak travel 
periods. 
 
Only 12.47% reported minimal delays, whereas another 12.47% experienced delays 
exceeding thirty minutes. These findings suggest that traffic congestion and passenger 
loading activities remain significant factors affecting travel efficiency along the Gusa–Bugo 
corridor. 
 
The prevalence of moderate and heavy delays emphasizes the need for properly designated 
loading zones and organized passenger waiting areas. Such facilities can reduce roadside 
congestion and improve traffic flow by minimizing random stopping and passenger 
accumulation along the highway. 
 
4.3.4 Level of Satisfaction with Modern Jeepney Service Attributes 
 
To determine commuter satisfaction with the current modern jeepney service, respondents 
rated three service attributes using a five-point Likert scale, where 5 indicates Very Satisfied 
and 1 indicates Very Dissatisfied. 
 
The weighted mean for each service attribute was computed using the following formula: 
 
 
 
28

The following verbal interpretation was adopted: 
 
 
Weighted Mean 
Interpretation 
4.21–5.00 
Very Satisfied 
3.41–4.20 
Satisfied 
2.61–3.40 
Moderately Satisfied 
1.81–2.60 
Dissatisfied 
1.00–1.80 
Very Dissatisfied 
 
Table 4.9 Level of Satisfaction with Modern Jeepney Service 
 
Service Attribute 
Weighted Mean 
Verbal Interpretation 
Rank 
Reasonable Fare Rate 
4.14 
Satisfied 
1 
Travel Time and Minimal Delays 
3.38 
Moderately Satisfied 
2 
Safety and Availability of Waiting Sheds 
2.61 
Moderately Satisfied 
3 
Overall Mean 
3.38 
Moderately Satisfied 
 
 
Table 4.9 presents the respondents' level of satisfaction regarding selected attributes of the 
modern jeepney transportation system. Among the evaluated indicators, Reasonable Fare 
Rate obtained the highest weighted mean of 4.14, corresponding to a verbal interpretation of 
Satisfied. This result indicates that commuters generally perceive the current fare structure as 
fair and affordable relative to the quality of service provided. 
 
Travel Time and Minimal Delays obtained a weighted mean of 3.38, interpreted as 
Moderately Satisfied. Although respondents acknowledged the improvements brought about 
by modern jeepneys, recurring traffic congestion and prolonged passenger loading activities 
continue to affect overall travel efficiency. 
 
The Safety and Availability of Waiting Sheds recorded the lowest weighted mean of 2.61, 
which falls under the Moderately Satisfied category but is very close to the threshold for 
dissatisfaction. This suggests that while some commuter facilities are available, respondents 
perceive them to be insufficient in terms of quantity, accessibility, maintenance, and 
protection from adverse weather conditions. 
 
Overall, the service attributes yielded an average weighted mean of 3.38, indicating that 
respondents were Moderately Satisfied with the present modern jeepney transportation 
system. The findings imply that while fare affordability is viewed positively, improvements 
in passenger infrastructure and traffic management remain necessary to enhance the overall 
commuting experience. 
 
29

4.4 Contingent Valuation Method (CVM) and Willingness to Pay 
 
This section presents the respondents' willingness to contribute a nominal maintenance fee 
for the continuous operation, maintenance, and improvement of modern passenger waiting 
sheds, designated loading zones, and transport terminals. The Contingent Valuation Method 
(CVM) was employed to estimate the monetary value commuters place on improved 
transportation facilities. 
 
4.4.1 Willingness to Contribute a Maintenance Fee 
 
Table 4.10 Respondents' Willingness to Pay for Improved Commuter Facilities 
 
Response Frequency Percentage (%) 
Yes 
316 
82.08 
No 
69 
17.92 
Total 
385 
100.00 
 
Table 4.10 shows that 316 respondents (82.08%) expressed their willingness to contribute a 
small maintenance fee for the continued improvement of commuter facilities. In contrast, 69 
respondents (17.92%) indicated that they were unwilling to provide additional financial 
contributions. 
 
The high percentage of positive responses demonstrates that commuters recognize the value 
of investing in safe, clean, and well-maintained waiting sheds and loading facilities. This 
finding further suggests that respondents believe improvements in commuter infrastructure 
will enhance travel convenience, passenger safety, and overall commuting efficiency. 
 
4.4.2 Maximum Amount Willing to Pay 
 
Respondents who answered "Yes" to the previous question were further asked to indicate the 
maximum amount they were willing to contribute per trip for the continuous maintenance and 
operation of commuter facilities. 
 
Table 4.11 Maximum Amount Respondents are Willing to Contribute (n = 316) 
 
Amount 
Frequency Percentage (%) 
₱2.00 
142 
44.94 
₱5.00 
121 
38.29 
₱10.00 
39 
12.34 
More than ₱10.00 14 
4.43 
Total 
316 
100.00 
30

Table 4.11 shows that the largest proportion of respondents (44.94%) were willing to 
contribute ₱2.00 per trip for the maintenance of commuter facilities. This was followed by 
38.29% who selected ₱5.00 as their preferred contribution. 
 
Only 12.34% expressed willingness to contribute ₱10.00, while 4.43% indicated a 
willingness to pay more than ₱10.00 per trip. 
 
These findings suggest that commuters generally support transportation infrastructure 
improvements provided that the required contribution remains affordable. The results indicate 
that implementing a minimal maintenance fee may be socially acceptable if accompanied by 
visible improvements in commuter facilities and service quality. 
 
4.4.3 Estimated Mean Willingness to Pay 
 
The average willingness to pay (WTP) was computed using the weighted average formula. 
​
 
Using the survey responses, 
 
Therefore, the estimated mean willingness to pay is ₱4.72 per commuter per trip. 
 
The computed average indicates that commuters place measurable economic value on 
improved passenger waiting facilities. This result demonstrates public support for 
infrastructure enhancement initiatives provided that the additional contribution remains 
minimal and transparent. 
 
4.5 Geographic Information System (GIS) Spatial Analysis 
 
Geographic Information System (GIS) analysis was conducted to determine the spatial 
distribution of commuter movement within the study area. The collected boarding and 
alighting locations were georeferenced and mapped to identify areas with high passenger 
activity. 
 
The resulting spatial analysis provides a visual representation of commuter travel patterns and 
serves as the primary input for the K-means clustering analysis. 
 
4.5.1 Spatial Distribution of Boarding Locations 
 
Figure 4.11 GIS Map of Boarding Locations  
(Insert GIS Boarding Point Map) 
 
The GIS-generated boarding point map revealed that passenger origins were primarily 
concentrated in the barangays of Bugo, Puerto, and Gusa. These locations exhibited the 
highest density of commuter boarding activities because of their large residential populations 
and proximity to major road corridors. 
 
31

Conversely, Agusan and Cugman recorded fewer boarding activities, indicating relatively 
lower passenger demand. 
 
The spatial concentration of boarding locations demonstrates that commuter demand is 
unevenly distributed across the study corridor, thereby emphasizing the need for strategically 
located passenger waiting facilities. 
 
4.5.2 Spatial Distribution of Destination Points 
 
Figure 4.12 GIS Map of Alighting Locations 
(Insert GIS Destination Map) 
 
The GIS destination map indicates that a significant proportion of commuters travel toward 
Cogon Commercial District, which functions as the city's primary commercial and 
employment center. 
 
Other destination points include Puerto, Bugo, Tablon, Agusan, Cugman, and Gusa. 
 
The clustering of destination points around commercial establishments suggests that 
passenger demand is strongly influenced by employment opportunities, educational 
institutions, government offices, and business districts. 
 
4.5.3 Passenger Density Map 
 
Figure 4.13 Passenger Density Heat Map 
(Insert Heat Map) 
 
The passenger density map illustrates varying levels of commuter concentration throughout 
the study area. High-density passenger movements were observed along the National 
Highway, particularly near intersections, commercial centers, schools, and transport 
terminals. 
 
These areas experience frequent passenger loading and unloading activities throughout the 
day, making them suitable locations for future commuter waiting sheds and designated 
loading areas. 
 
4.6 K-means Clustering Analysis 
 
K-means clustering was employed to classify commuter activity into homogeneous groups 
based on their boarding and destination coordinates. 
 
Three clusters were generated to categorize passenger demand according to intensity. 
 
 
 
 
 
 
 
 
32

Table 4.12 K-means Clustering Results 
 
Cluster 
Demand Level 
Number of Passenger Points 
Cluster 1 High Demand 
162 
Cluster 2 Moderate Demand 134 
Cluster 3 Low Demand 
89 
Total 
385 
 
 
 
The K-means clustering analysis successfully categorized commuter activity into three 
distinct demand groups. 
 
Cluster 1 represented high-demand commuter areas, accounting for 162 passenger points. 
These locations exhibited frequent boarding and alighting activities and were primarily 
situated along major commercial corridors. 
 
Cluster 2 consisted of 134 passenger points representing moderate commuter demand. These 
locations generally served residential communities with consistent but relatively lower 
passenger volumes. 
 
Meanwhile, Cluster 3, containing 89 passenger points, represented low-demand areas 
characterized by limited commuter activity. 
 
The clustering analysis demonstrates that passenger demand is spatially concentrated rather 
than 
uniformly 
distributed 
throughout 
the 
transportation corridor. Consequently, 
transportation infrastructure investments should prioritize high-demand locations to 
maximize commuter benefits. 
 
4.7 Proposed Priority Locations for Modern Passenger Waiting Sheds 
 
The proposed waiting shed locations were determined by integrating the following datasets: 
 
●​ GIS passenger density analysis 
●​ Boarding and destination maps 
●​ K-means clustering results 
●​ Delay analysis 
●​ Commuter satisfaction ratings 
●​ Willingness-to-pay analysis 
 
Table 4.13 Proposed Priority Locations for Passenger Waiting Sheds 
 
Proposed Location 
Cluster 
Priority Level Justification 
Bugo Public Market 
High 
Very High 
Highest boarding demand 
33

Puerto National Highway High 
Very High 
Major transfer corridor 
Gusa National Highway 
High 
High 
High passenger volume 
Tablon Crossing 
Moderate High 
Frequent loading activities 
Agusan Junction 
Moderate Moderate 
Moderate commuter demand 
Cugman Highway 
Low 
Moderate 
Future service expansion 
 
The proposed waiting shed locations were selected based on the integration of commuter 
demand, spatial analysis, and public perception. Areas identified as high-demand clusters 
demonstrated the greatest need for organized passenger facilities due to the volume of 
boarding and alighting activities. 
 
Bugo Public Market and Puerto National Highway emerged as the highest-priority locations 
because they serve as major origins and destinations for daily commuters. These areas 
experience continuous passenger movement and currently exhibit inadequate waiting 
facilities. 
 
The installation of modern waiting sheds at these locations is expected to improve passenger 
comfort, enhance commuter safety, reduce roadside congestion, and facilitate more efficient 
passenger loading and unloading operations. 
 
4.8 Summary of Findings 
 
The results of the study revealed that the majority of the respondents were young adults 
between 18 and 25 years old, with students comprising the largest occupational group among 
modern jeepney commuters. This demographic profile indicates that the modern jeepney 
system primarily serves individuals who rely on public transportation for education, 
employment, and other daily activities. The findings further showed that the Bugo–Cogon 
route recorded the highest commuter utilization, while the barangays of Bugo, Puerto, and 
Gusa served as the primary boarding locations. Most respondents identified the Cogon 
Commercial District as their destination, demonstrating that commuter movement is largely 
concentrated between residential areas and the city's commercial and employment center. 
 
The analysis of travel characteristics revealed that most respondents traveled moderate 
distances of four to eight kilometers and generally paid fares ranging from ₱16.00 to ₱25.00 
per trip. Moderate travel delays of six to fifteen minutes were the most frequently 
experienced during peak hours, suggesting that traffic congestion and passenger loading 
activities continue to affect travel efficiency along the study corridor. Although respondents 
expressed satisfaction with the current fare structure, the overall evaluation of the modern 
jeepney service indicated only moderate satisfaction, primarily due to concerns regarding 
travel delays and the limited availability of safe and convenient passenger waiting sheds. 
 
The Contingent Valuation Method showed that a large majority of commuters were willing to 
contribute a nominal maintenance fee to support the installation and continuous maintenance 
of modern commuter facilities. Most respondents preferred a minimal contribution ranging 
from ₱2.00 to ₱5.00 per trip, resulting in an estimated average willingness to pay of ₱4.72. 
This finding suggests that commuters recognize the importance of investing in transportation 
34

infrastructure, provided that the proposed fee remains affordable and is directly utilized for 
improving commuter facilities. 
 
The Geographic Information System (GIS) analysis and K-means clustering successfully 
identified areas with varying levels of commuter demand throughout the study corridor. High 
passenger concentrations were observed in Bugo, Puerto, and Gusa, indicating that these 
locations experience the greatest boarding and alighting activities. Based on the integration of 
commuter demand, spatial analysis, satisfaction ratings, and willingness-to-pay results, these 
areas were identified as the highest-priority locations for the installation of modern passenger 
waiting sheds. Overall, the findings demonstrate that combining commuter perception, 
economic valuation, and spatial analytical techniques provides an effective basis for 
identifying priority locations for transportation infrastructure improvements and supports 
evidence-based planning for the modernization of commuter facilities along the Gusa–Bugo 
corridor in Cagayan de Oro City. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
35

BIBLIOGRAPHY 
Abad, S. K., & Abad, K. A. (2023). Synergizing geographic information systems (GIS) and 
multicriteria decision making analysis (MCDA) for public transit network optimization: A 
review. Scholar's Digest- Journal of Multidisciplinary Studies, 3(2), 173–182 
Abhilash, S. S. S., Sreedevi, M., & Rao, K. R. (2019). Public transportation service quality 
assessment using AVL and fare card data. Transportation Research Part A: Policy and 
Practice, 125, 245–256 
Agaton, C. B., et al. (2023). State of the art: Public utility vehicle modernization program in 
the Philippines. Journal of Sustainable Development in Transport & Infrastructure, 4(2), 
45-60. 
Alharbi, M., & Hassan, M. (2023). Optimizing the distribution of public transportation stops 
using GIS: A case of Amman City in Jordan. Civil Engineering and Architecture, 11(3), 
1558–1568. https://doi.org/10.13189/cea.2023.110335 
Ali, A. B. (2018). Optimizing bus stop location and spacing using the Analytical Hierarchy 
Process (AHP) and GIS. International Journal of Transportation Science and Technology, 
7(1), 1–11 
Atos, M. S. Q., Cabe, K. B., Gomez, C. J. E., & Padupad, C. L. O. (2021). Modernized 
tradition: Transformation of public transport. DLSU Senior High School Research Congress. 
Animo Repository. https://animorepository.dlsu.edu.ph/conf_shsrescon/2021/paper_spl/2/ 
Bacero, R. M., Bandala, A. A., & Fillone, A. M. (2017). Proposed jeepney fare determination 
using fuzzy logic. Philippine Engineering Journal, 38(2), 23–35. 
https://ncts.upd.edu.ph/tssp/wp-content/uploads/2017/07/TSSP2017-08-Bacero-Bandala-and-
Fillone.pdf 
Balingit, J. C. (2022). The missing link: Assessing the roadside infrastructure of the PUV 
modernization program. Philippine Journal of Public Administration, 66(1), 88-105. 
Bureau of Philippine Standards. (2017). Public utility vehicles – Class 2 and Class 3 – 
Specifications (PNS 2126:2017). Department of Trade and Industry. 
Cagayan de Oro City Council. (2022). City Ordinance No. 14337-2022: An ordinance 
adopting the Local Public Transport Route Plan (LPTRP) of Cagayan de Oro City. City 
Government of Cagayan de Oro. 
Cahigas, M. M. L., Zulvia, F. E., Ong, A. K. S., & Prasetyo, Y. T. (2023). A comprehensive 
analysis of clustering public utility bus passenger's behavior during the COVID-19 pandemic: 
Utilization of machine learning with metaheuristic algorithm. Sustainability, 15(9), 7410. 
https://doi.org/10.3390/su15097410 
Cueto, M. J., Baluyot, M. M., Ordonia, R. L., & Rivera, J. P. (2024). Intelligent transport 
system implementation in Manila: A four-step model approach. International Journal of 
Transportation Science and Technology, 13(1), 88–102. 
https://ncts.upd.edu.ph/tssp/wp-content/uploads/2024/12/TSSP2024-11-Revised-Paper.pdf 
Cunanan, A. L. (2025). Data-driven jeepney modernization: Leveraging telematics data for 
public transport indicators. SafeTravelPH Mobility Group. 
Delgra, M. A., et al. (2019). Public transport crowdsourcing and collaborative governance for 
BRT in transition: Monitoring and analyzing the EDSA Carousel in Metro Manila. 
36

Transportation Research Procedia, 41, 268–279. 
https://easts.info/on-line/proceedings/vol.13/pdf/PP3045_R1_F.pdf 
Department of Transportation. (2017). Omnibus guidelines on the planning and identification 
of public road transportation services and franchise issuance (Department Order No. 
2017-011). Government of the Philippines. 
Du, J., Shi, J., Zhang, N., Liu, Y., & Liu, W. (2025). Correction: Du et al. Preliminary 
Establishment of an Efficient Regeneration and Genetic Transformation System for 
Hemerocallis middendorffii Trautv. & C. A. Mey. Horticulturae, 11(5), 528. 
https://doi.org/10.3390/horticulturae11050528 
Duan, Z., et al. (2018). Using GPS data to assess operational performance of public bus 
routes. Transportation Research Part C, 86, 374–389. 
Francesquite, R. J., & Calva, J. P. (2024). The unveiling of the e-jeepney modernization 
program through the lenses of diverse sectors in Southern Philippines. Sustainability, 16(9), 
3912. https://journal.formosapublisher.org/index.php/eajmr/article/view/8860? 
Francisco, K. (2025). Transport infrastructure in the Philippines: From plans to actual 
allocation. Philippine Institute for Development Studies. https://doi.org/10.62986/dp2024.51 
Gatarin, E. R. (2024). Socio-economic and operational challenges of the Philippine PUV 
modernization program. Journal of Transport Policy and Planning, 12(2), 41–56. 
https://cids.up.edu.ph/wp-content/uploads/2024/08/Examining_PUVMP_Just_Transition_Len
s_Jeepney_Operators_Bacolod3.pdf  
Goud, S. D. (2020). The impact of infrastructure on transit service reliability: A case study. 
Journal of Public Transportation, 22(1), 1–15 
Gumasing, M. J. J., et al. (2024). Factors influencing the adoption of electric jeepneys in the 
Philippines. Transportation Research Interdisciplinary Perspectives, 19, 100832. 
https://www.mdpi.com/2032-6653/15/7/284 
Gumasing, M. J. J., et al. (2024). Is modernization of public transport in the Philippines a 
boon or a bane for the Filipino people? Management Research and Innovation Journal, 20(1), 
4-26. 
Gumasing, M. J. J., Tadina, K. P. V., & Vidamo, N. D. (2021). Sustainability model of 
E-Jeepney operations in Paranaque, Metro Manila. In 2021 IEEE 8th International 
Conference on Industrial Engineering and Applications (ICIEA) (pp. 247–251). IEEE. 
https://doi.org/10.1109/ICIEA52957.2021.9436813 
Japan International Cooperation Agency. (2019). The roadmap for transport infrastructure 
development for Metro Manila and its surrounding areas. JICA Reports. 
Kock, N., & Hadaya, P. (2018). Minimum sample size estimation in PLS-SEM: The inverse 
square root and gamma-exponential methods. Information Systems Journal, 28(1), 227–261. 
https://doi.org/10.1111/isj.12131 
Labrador, C. L., Palma, A. J., Santiago, M. R., Torres, J. D., Gaviola, J. A., & Muhi, R. A. 
(2010). Traffic flow impact of queuing public utility jeepneys at SM City Sta. Mesa. Journal 
of the Eastern Asia Society for Transportation Studies, 8, 1435–1449. 
https://ncts.upd.edu.ph/tssp/wp-content/uploads/2017/02/2010-08_labrador_final.pdf 
Lalio, J. A., & Navarro, R. S. (2025). Commuters’ preferences and willingness to pay for 
modern public utility vehicles. Asian Transport Studies, 9, 100134. 
https://www.researchgate.net/publication/390126481_COMMUTERS%27_PREFERENCES
37

_AND_THEIR_WILLINGNESS_TO_PAY_FOR_MODERN_PUBLIC_UTILITY_VEHICL
E_MPUV 
Li, Y., Wang, X., & Zhang, H. (2023). Study on location of bus stops in subway service areas 
based on residents’ travel accessibility. Sustainability, 15(6), 4873. 
https://www.mdpi.com/2071-1050/15/5/4517? 
Macalalad, A. A., Tolentino, N. J., et al. (2021). Environmental and socio-economic benefits 
of public transport modernization in the Philippines. Transportation Research 
Interdisciplinary Perspectives, 11, 100427. https://www.mdpi.com/1660-4601/18/2/463 
Mayo, J. R., & Taboada, E. B. (2021). Commuter perceptions on the service quality of public 
transport in the Philippines: A case study of the PUV modernization program. Journal of 
Public Transportation, 23(1), 1-15. https://doi.org/10.5038/2375-0901.23.1.2 
Montero-Gutiérrez, J., et al. (2023). Site-specific optimization of bus stop locations and 
climate-responsive shelter design. Energy and Buildings, 278, 112579. 
https://www.researchgate.net/publication/360172864_Site-specific_optimization_of_bus_stop
_locations_and_designs_over_a_corridor 
National Center for Transportation Studies. (2024). Redesigning Philippine land transport 
governance towards improving commuter service quality. University of the Philippines 
Diliman. 
National Economic and Development Authority. (2023). Philippine Development Plan 
2023-2028: Chapter 12: Expand and Upgrade Infrastructure. Government of the Philippines. 
Ong, A. K. S., Prasetyo, Y. T., Estefanio, A., Tan, A. S., Videña, J. C., Villanueva, R. A., 
Chuenyindee, T., Thana, K., Persada, S. F., & Nadlifatin, R. (2023). Determining factors 
affecting passenger satisfaction of “jeepney” in the Philippine urban areas: The role of service 
quality in sustainable urban transportation systems. Sustainability, 15(2), 1223. 
https://doi.org/10.3390/su15021223 
Paringit, E. C., Lucas, R. D., & Cutora, J. J. (2019). GIS for better public transportation and 
transit planning. Philippine Journal of Science, 148(4), 697–708. 
https://www.dlsu.edu.ph/wp-content/uploads/pdf/conferences/research-congress-proceedings/
2019/see-I-004.pdf? 
Philippine News Agency. (2024, February 9). CDO opens 61 new routes under PUV 
modernization plan. https://www.pna.gov.ph/articles/1218591 
Rahman, M. M., et al. (2020). Prioritizing metro service quality attributes using TOPSIS and 
importance-satisfaction analysis. Journal of Public Transportation, 23(1), 1–18. 
https://journals.sagepub.com/doi/10.1177/0361198120917972 
Ranosa, M. J., Fillone, A. M., & De Guzman, A. P. (2017). Jeepney service operation and 
demand analysis in Baguio City, Philippines. Transportation Research Record, 2650(1), 
55–63. 
https://ncts.upd.edu.ph/tssp/wp-content/uploads/2017/07/TSSP2017-06-Ranosa-Fillone-and-
De-Guzman.pdf 
Regan, A. C., et al. (2020). GIS-based identification and visualization of multimodal freight 
transportation catchment areas. Transportation Research Part E, 141, 102019. 
https://link.springer.com/article/10.1007/s11116-020-10155-3 
Regidor, J. R., & Aloc, R. C. (2016). Traffic problems at jeepney stops and proposals for 
improved jeepney stop policies. Journal of the Eastern Asia Society for Transportation 
38

Studies, 11, 2135–2149. 
https://ncts.upd.edu.ph/tssp/wp-content/uploads/2018/08/Regidor96.pdf 
Reyes, J. M., et al. (2023). Moving toward objective metrics: The role of GPS telematics in 
evaluating modernized public utility vehicle performance. Journal of Philippine 
Transportation Studies, 15(2), 112-128. 
Reyes, J. P., Cruz, R. A., & Santos, L. M. (2023). Measuring the efficiency of consolidated 
public transport routes using GPS data. Journal of Transportation Engineering, 149(6), 
04023032. 
Santos, T., Lobato, K., Rocha, J., & Tenedório, J. A. (2020). Modeling photovoltaic potential 
for bus shelters on a city scale: A case study in Lisbon. Sustainable Cities and Society, 60, 
102255. https://www.mdpi.com/2076-3417/10/14/4801 
Savilla, J. P., et al. (2024). Perception of jeepney drivers on the jeepney modernization 
program in Indang, Cavite. Philippine Journal of Social Sciences, 49(1), 55–68. 
https://www.researchgate.net/publication/379494940_Perception_of_the_Jeepney_Drivers_o
n_the_Jeepney_Modernization_in_Indang_Cavite 
Stadler, T., Hofmeister, S., & Dünnweber, J. (2022). A method for the optimized placement of 
bus stops based on Voronoi diagrams. Proceedings of the 55th Hawaii International 
Conference on System Sciences (HICSS55). https://doi.org/10.24251/HICSS.2022.694 
Ventura, A. B., & Regidor, J. R. (2018). Assessment of public utility vehicle modernization 
implementation: Data gaps and planning challenges. Proceedings of the 25th Annual 
Conference of the Transportation Science Society of the Philippines. 
Ventura, A. B., Frayna, C. M., & Vergel, K. N. (2018). Determination of appropriate public 
transportation mode for a university transit route. Philippine Engineering Journal, 39(1), 
45–58. https://ncts.upd.edu.ph/tssp/wp-content/uploads/2018/07/TSSP2018-16.pdf 
Vergel, K. N., et al. (2014). Evaluation of compliance of customized local road vehicles with 
vehicle standards. Philippine Engineering Journal, 35(2), 1–14. 
https://ncts.upd.edu.ph/tssp/wp-content/uploads/2018/08/Vergel14.pdf 
Villegas, M. R., Ledres, J. M., & Estember, R. D. (2021). Physical assessment and perceived 
quality of e-jeepney in Metro Manila. Journal of Transportation Technologies, 11(3), 
211–224. https://www.ieomsociety.org/singapore2021/papers/1199.pdf? 
Wang, F., Ye, M., Zhu, H., & Gu, D. (2022). Optimization method for conventional bus stop 
placement using Voronoi diagrams. Journal of Advanced Transportation, 2022, 1–12. 
https://www.mdpi.com/2071-1050/14/13/7918? 
Wang, Y., Xu, Y., Wang, X., & Fan, X. (2017). Using GPS data to assess the operational 
performance of public bus routes. Transportation Research Record: Journal of the 
Transportation Research Board, 2652(1), 58–67. 
Yigitcanlar, T., Sipe, N., Evans, R., & Pitot, M. (2007). Modeling pedestrian accessibility to 
public transport using GIS-based indices. Environment and Planning B, 34(5), 901–920. 
Yu, Jingqiao & Zhu, Yuan & Wu, Chaowen & Song, Guoqing. (2024). Optimization of Bus 
Stop Location based on Spatial Analysis and K-Means Clustering Method – A Case Study in 
Hohhot City. 
https://www.researchgate.net/publication/378528861_Optimization_of_Bus_Stop_Location_
based_on_Spatial_Analysis_and_K-Means_Clustering_Method_-_A_Case_Study_in_Hohho
t_City 
39

Zhao, J., Copley, C., Wang, J., & Li, T. (2018). Analyzing the relationship between bus stop 
spacing and transit operational reliability. Journal of Advanced Transportation, 2018.Zulueta, 
M. C. (2024). Infrastructure and commuter experience of modernized public utility jeepneys 
using PLS-SEM. Asian Transport Studies, 8, 100112. 
https://www.mdpi.com/2071-1050/16/10/3912 
Zulueta, M. C., et al. (2024). Implications of the progression to sustainable public 
transportation: Insights into the modern jeepney shift. Sustainability, 16(5), 2247. 
https://www.mdpi.com/2071-1050/16/10/3912 
Saptutyningsih, E., & Karimah, N. (2019). Valuing public transportation using the contingent 
valuation method. Economic Journal of Emerging Markets. 
https://journal.umy.ac.id/index.php/esp/article/view/5017 
Fujii, S., et al. (2016). Knowledge, attitudes, and willingness to pay for sewerage and 
sanitation services in Metro Manila. Journal of Environmental Science and Management.  
https://ovcre.uplb.edu.ph/journals-uplb/index.php/JESAM/article/view/164 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
40

APPENDIX A 
Survey Questionnaire (English & Bisaya) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
41

42

43

APPENDIX B 
Informed Consent Form (English & Bisaya) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
44

45

46

47

APPENDIX C 
Curriculum Vitae 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
48

KACEY CAPIÑA 
SILVERCREEK SUBDIVISION, PHASE 1, BLOCK 15 LOT 9,  
CARMEN, CAGAYAN DE ORO CITY 
capinakacey@gmail.com  
0936-821-2308 
​
​
 
EDUCATIONAL ATTAINMENT 
 
Bachelor of Science in Civil Engineering Xavier University – Ateneo de 
Cagayan  
73 Corrales Ave, Cagayan de Oro City, 9000 Misamis Oriental 
 
August 2024 - 
Present 
University of Science and Technology of Southern Philippines               
Claro M. Recto Ave, Lapasan, Cagayan de Oro City, 9000 Misamis Oriental 
 
August 2022 - 
January 2024 
Senior High School – Humanities and Social Sciences 
Xavier Ateneo Senior High School 
Fr. William Masterson SJ Ave, Upper Balulang, Cagayan de Oro City, 9000 
Misamis Oriental  
 
June 
2020 
– 
April 2022 
Junior High School - Misamis Oriental General Comprehensive Highschool 
(MOGCHS) 
Don Apolinar Velez St, Cagayan de Oro City, 9000 Misamis Oriental  
 
​
 
June 2016 to 
March 2020 
Elementary - City Central School 
P.N. Roa St, Brgy. 29, Cagayan de Oro City, 9000 Misamis Oriental  
 
June 
2013 
– 
March 2016 
Preschool to Elementary - St. Mary’s Academy of Carmen 
Villarin St, Carmen, Cagayan de Oro City, 9000 Misamis Oriental  
 
 
June 
2009 
– 
March 2013 
 
49

SKILLS 
●​ Knowledgeable in Computer Aided Design (AutoCAD, Sketchup) 
●​ Knowledgeable in Mapping (ArcGIS, QGIS, Google Earth Pro) 
●​ Knowledgeable in Microsoft Office softwares (Excel, Word, PowerPoint) 
●​ Visual Communication (Canva & Photoshop for Graphic Design, Capcut for Video 
Editing) 
●​ Public Speaking Skills 
●​ Communication Skills 
●​ Organizational Governance Skills 
●​ Event Coordination Skills 
●​ Technical Writing Skills 
●​ Budgeting and Resource Management 
 
RELATED EXPERIENCE/S 
POSITION 
COMPANY NAME 
COMPANY 
ADDRESS 
INCLUSIVE 
DATE 
Creative 
Virtual 
Assistant 
Kacey Capiña  
Silvercreek Subdivision January 2023 - 
December 2023 
Volunteer for Secretariat 
Works  
(under a Police Captain 
Officer) 
Philippine 
National 
Police (PRO10) 
Claro M. Recto Ave, 
Lapasan, 
Cagayan 
de 
Oro City, 9000 Misamis 
Oriental  
April 
2024 
- 
June 2024 
Representative 
(for 
a 
National 
Conference for Civil 
Engineering 
Students 
2025) 
Unified 
Students 
of 
Philippine Institute of 
Civil 
Engineers 
(USPICE) - CDO 
Cagayan de Oro 
City 
November 24 - 
25, 2025 
50

AWARDS 
NAME/TYPE OF AWARD 
AWARD-GIVING 
BODY 
DATE AWARDED 
Consistent Honor Student 
St. Mary’s Academy of Carmen 
 
June 2009 – March 
2013 
Consistent Honor Student 
City Central School 
June 2019 – July 2023 
Consistent Honor Student 
MOGCHS 
June 2016 - March 2020 
Second Honors 
Xavier Ateneo Senior High School June 2021 
Best 
Paper 
(HUMSS 
Category) 
Xavier Ateneo Senior High School May 2022 
​
​
 
ORGANIZATIONS 
POSITION 
NAME OF 
ORGANIZATION 
INCLUSIVE 
DATES 
Associate Head Department of Students’ Health Development; Graphic 
Design 
July 2021 – 
April 2022 
Member 
Leadership Empowerment and Development Society - 
USTP ; Committee for Multimedia Production 
August 
2022 
- 
June 2023 
Associate Head Philippine Institute of Civil Engineers – Xavier 
University Student 
Chapter (PICE-XUSC); 
InPro Commitee 
August 
2024 
– 
July 2025 
Shadow 
Prime 
Minister 
Philippine Institute of Civil Engineers – Xavier 
University Student 
Chapter (PICE-XUSC); House of Representatives 
August 
2025 
– 
Present 
51

Assistant 
Treasurer 
Unified Students of Philippine Institute of Civil 
Engineers (USPICE); Executive Officers 
September 2025 – 
Present 
 
References (available upon request). 
 
Data Privacy Consent 
 
In compliance with the Data Privacy Act (DPA) of 2012, and its implanting Rules and 
Regulations (IRR) effective September 8, 2016, 
I allow ☑ (I hold free and harmless and indemnify Xavier University from any complaint, 
suit or damages which any party may file or claim in relation to my consent) 
I don’t allow ☐ (My resume will be used solely for counseling purposes) 
 
 
Signature of student________________ 
 
Signed this 29th day of April 2026 at Cagayan de Oro City. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
52

CAROLINE PHILOMENA CUNDANGAN 
Blk 15, Lot 26, Bellevue Subdivision, Upper Carmen, CDOC  
cpccundangan@gmail.com 
09150978816 
  
  
EDUCATIONAL ATTAINMENT 
 
Bachelor of Science in Civil Engineering 
Xavier University – Ateneo de Cagayan Corrales Ave., Cagayan de 
Oro City 
  
August 2023 - Present 
Senior High School – Science, Technology, Engineering and 
Mathematics 
Pagadian Science High School 
Rizal Ave, Lumbia, Pagadian City, Zamboanga del Sur 
  
October 2020 – June 
2022 
Junior High School - Saint Columban College Junior High School 
Enerio Street, Pagadian City, Zamboanga del Sur 
  
June 2017 – March 
2020 
Elementary - Pagadian City Pilot School  
San Jose District, Pagadian City, Zamboanga  
Del Sur 
  
June 2010 - March 
2016 
  
SKILLS 
●​ Basic Computer Aided Design (CAD; AutoCAD, Sketchup) 
●​ Basic Mapping Skills (ArcGIS, QGIS, Google Earth Pro) 
●​ Basic Programming Skills (Python) 
●​ Knowledgeable in Microsoft Office Applications (Word, Excel, Powerpoint, Etc.) 
●​ Solid Communication Skills 
●​ Time Management Skills​
 
 
 
 
53

RELATED EXPERIENCE/S 
POSITIO
N 
COMPANY NAME 
COMPANY 
ADDRESS 
INCLUSIVE 
DATE 
Volunteer 
Saint Columban College - 
Junior High School 
Enerio Street, Pagadian City, 
Zamboanga del Sur 
   June 2018 
– 
May 2020 
  
Volunteer 
Pagadian Science High School Rizal 
Ave, 
Lumbia, 
Pagadian 
City, 
Zamboanga del Sur 
April 2022 
ACES 
– 
Events 
Committee 
Member  
Xavier University - Association 
of the College of Engineering 
Students 
Corrales Ave., Cagayan 
de Oro City 
September 
2023  
  
AWARDS 
NAME/TYPE 
OF 
AWARD 
AWARD-GIVING 
BODY 
DATE AWARDED 
Honor Student  
Pagadian City Pilot School 
March 2014 - March 2016 
Consistent Honor Student  Pagadian Science High School July 2021 - June 2022 
Best Paper (Stem Category) Pagadian Science High School  July 2023 
  
ORGANIZATIONS 
POSITION 
NAME OF 
ORGANIZATION 
INCLUSIVE 
DATES 
Math Cub Member 
Saint Columban College Junior High School August 2017– March 
2020 
54

Science Club Member Saint Columban College Junior High School August 2017 - March 
2020 
Youth Member  
Philippine Red Cross - Zamboanga del Sur 
Chapter  
October 2018 - June 
2022 
Angklung 
Ensemble 
Member  
Saint Columban College Junior High School  September 2018 – 
March 2020 
ACES 
– 
Events 
Committee Member  
Xavier University - Association of the 
College of Engineering Students 
 September 2023  
  
References (available upon request). 
  
Data Privacy Consent 
  
In compliance with the Data Privacy Act (DPA) of 2012, and its implanting Rules and 
Regulations (IRR) effective September 8, 2016, 
I allow ☑ (I hold free and harmless and indemnify Xavier University from any complaint, 
suit or damages which any party may file or claim in relation to my consent) 
I don’t allow ☐ (My resume will be used solely for counseling purposes) 
  
Signature of student           ​
 
Signed this 1st day of May 2026 at Cagayan de Oro City.  
  
 
 
 
 
 
 
 
 
 
 
55

BEA ARABELLA LOPEZ 
Phase 3A, Villa Trinitas Subd., Bugo, Cagayan de Oro City  
lopez.beaarabella@gmail.com 
09939759721 
​
​
​
 
EDUCATIONAL ATTAINMENT 
 
Bachelor of Science in Civil Engineering Xavier University – Ateneo de 
Cagayan Corrales Ave., Cagayan de Oro City 
  
August 2023 - 
Present 
Senior High School – Science, Technology, Engineering and Mathematics 
Liceo de Cagayan University  
Kauswagan, Cagayan de Oro City 
  
August 2021 – 
April 2023 
Junior High School  
Bugo National High School  
Rabocca drive, Bugo, Cagayan de Oro City 
  
June 
2017 
– 
April 2021 
Elementary 
Bugo Central School 
Bantilles, Bugo, Cagayan de Oro City 
  
June 
2015 
– 
April 2017 
Elementary 
Philippine Southfield School 
Phs 1, Villa Trinitas Subd., Bugo, Cagayan de Oro City 
  
June 
2001– 
March 2015 
  
  
  
  
  
  
56

SKILLS 
●​ Knowledgeable in Computer Aided Design (AutoCAD/Sketchup) 
●​ Proficient in Mapping (QGIS, ArcGIS) 
●​ Proficient in Microsoft Office softwares (Word, Excel, PowerPoint) 
●​ Quantity Take-Off and Cost Estimation  
●​ Adept Interpersonal and Leadership Skills 
●​ Flexible and can work under pressure 
●​ Safety Awareness in Construction Sites  
●​ Time Management skills 
●​ Visual Communication (Canva for Graphic Design, Capcut for Video Editing) 
●​ Strong Analytical and Problem-Solving Skills  
●​ Ability to Work Independently and in a Team  
●​ Attention to Detail and Accuracy 
  
RELATED EXPERIENCE/S 
POSITION COMPANY NAME 
COMPANY 
ADDRESS 
INCLUSIVE 
DATE 
Volunteer Parish 
Youth 
Coordinating 
Council 
Bugo, Cagayan de 
Oro City 
August 
2021 
– 
December 2023 
Volunteer Bugo National High School 
Bugo, Cagayan de 
Oro City 
July 2018 – May 2021 
Volunteer Parish 
Pastoral 
Council 
for 
Responsible Voting 
Bugo, Cagayan de 
Oro City 
May 10, 2022 
  
  
 
  
57

AWARDS 
NAME/TYPE 
OF 
AWARD 
AWARD-GIVING BODY 
DATE AWARDED 
Consistent Achiever 
Philippine Southfield School June 2011 – May 2015 
Consistent Honor Student Bugo Central School 
June 2015 – May 2017 
Consistent Honor Student Bugo National High School June 2019 – May 2021 
  
ORGANIZATIONS 
POSITION 
NAME OF 
ORGANIZATION 
INCLUSIVE 
DATES 
Ministry Head – Events and 
Presentations 
Philippine Institute of Civil Engineers – 
Xavier University Student 
Chapter 
August 2025 – May 
2026 
Associate Ministry Head – 
Publication 
and 
Communication  
Philippine Institute of Civil Engineers – 
Xavier University Student 
Chapter 
October 2024 – May 
2025 
Member  
Motion Ensemble 
September 2022 – 
May 2023 
  
References (available upon request). 
  
Data Privacy Consent 
 
In compliance with the Data Privacy Act (DPA) of 2012, and its implanting Rules and 
Regulations (IRR) effective September 8, 2016, 
I allow ☑ (I hold free and harmless and indemnify Xavier University from any complaint, 
suit or damages which any party may file or claim in relation to my consent) 
I don’t allow ☐  (My resume will be used solely for counseling purposes) 
Signature of student___________ 
Signed this 30th day of April 2026 at Cagayan de Oro City. 
 
58

JAMMEZA USMAN 
Camella Homes, Prime Rose St. Block 15 Lot 59-61, Upper​
 Balulang, Cagayan de Oro​
 jammezausman@gmail.com 
0955-462-1121 
​
​
​
 
EDUCATIONAL ATTAINMENT 
 
Bachelor of Science in Civil Engineering Xavier University – Ateneo de 
Cagayan Corrales Ave., Cagayan de Oro City 
  
August 2023 - 
Present 
Senior High School – Science, Technology, Engineering, and Mathematics 
Xavier Ateneo Senior High School 
Fr. William Masterson SJ Ave, Upper Balulang, Cagayan de Oro City, 
9000 Misamis Oriental  
  
June 
2021 
– 
April 2023 
Junior High School – Corpus Christi School, Masterson Avenue, Cagayan 
de Oro City, 9000 Misamis Oriental. 
  
June 
2017 
– 
April 2021 
Elementary - Corpus Christi School, Masterson Avenue, Cagayan de Oro 
City, 9000 Misamis Oriental. 
  
June 
2011 
– 
March 2017 
  
 
 
 
 
59

SKILLS 
●​ Knowledgeable in Computer Aided Design (AutoCAD, Sketchup) 
●​ Knowledgeable in Mapping (ArcGIS, QGIS, Google Earth Pro) 
●​ Knowledgeable in Structural Analysis (Frame Analysis, Vertical Reactions, 
Earthworks Volume) 
●​ Knowledgeable in Construction Estimation (NSCP Standards, Formworks, Concrete 
Volume) 
●​ Knowledgeable in Microsoft Office softwares (Excel, Word, PowerPoint) 
●​ Visual Communication (Canva & Photoshop for Graphic Design, Capcut for Video 
Editing) 
●​ Communication Skills 
●​ Organizational Governance Skills 
●​ Technical Writing Skills 
●​ Critical Thinking and Problem Solving ​
​
 
RELATED EXPERIENCE/S 
POSITION 
COMPANY 
NAME 
COMPANY 
ADDRESS 
INCLUSIVE 
DATE 
Volunteer 
Corpus 
Christi 
School  
Masterson Avenue, Cagayan de Oro 
City, 9000 Misamis Oriental. 
June 2011 – April 
2017  
Academic 
Project Lead  
Corpus 
Christi 
School 
Masterson Avenue, Cagayan de Oro 
City, 9000 Misamis Oriental. 
July 
2022 
– 
August 2022 
Student Leader  Corpus 
Christi 
School 
Masterson Avenue, Cagayan de Oro 
City, 9000 Misamis Oriental. 
June 2017 – April 
2021  
  
 
 
60

AWARDS 
NAME/TYPE OF AWARD 
AWARD-GIVING 
BODY 
DATE AWARDED 
Academic Excellence in Mathematics 
(Best in Math)  
Corpus 
Christi 
School  
March 2018, March 2019, 
April 2021  
Consistent Honor Student  
Corpus 
Christi 
School  
June 2017 – April 2021  
  
ORGANIZATIONS 
POSITION 
NAME OF ORGANIZATION 
INCLUSIVE DATES 
Student Council  
Corpus Christi School 
June 2017 – April 
2021  
Mathematics 
Society Member 
Corpus Christi School 
June 2011 – April 
2021  
Computer 
Club 
Member  
Corpus Christi School 
June 2017 – April 
2021  
Science 
Club 
Member  
Corpus Christi School 
June 2015 – April 
2021  
Sports 
Organization 
Member  
Corpus Christi School 
June 2014 – March 
2020  
Associate Head 
Philippine Institute of Civil Engineers – Xavier 
University Student 
Chapter (PICE-XUSC); 
Pubcom Committee 
August 2023 - Present 
Media 
and 
Arts 
Member 
Unified Students of Philippine Institute of Civil 
Engineers (USPICE); Executive Officers 
July 2025 - December 
2025 
61

References (available upon request). 
  
Data Privacy Consent 
  
In compliance with the Data Privacy Act (DPA) of 2012, and its implanting Rules and 
Regulations (IRR) effective September 8, 2016, 
I allow ☑ (I hold free and harmless and indemnify Xavier University from any complaint, 
suit or damages which any party may file or claim in relation to my consent) 
I don’t allow ☐ (My resume will be used solely for counseling purposes) 
  
 
Signature of student_______ 
Signed this 30th day of April 2026 at Cagayan de Oro City. 
  
 
 
 
 
 
 
 
 
 
 
62
