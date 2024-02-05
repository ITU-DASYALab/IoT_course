## General hints

Generally good places to find literature, for IoT and beyond:

  * https://dblp.uni-trier.de/
  * https://scholar.google.com/
  * https://www.researchgate.net/
  * https://ieeexplore.ieee.org/

Judging a journal/publication's ranking and reputation is a complex issue and beyond scope here, but as an introduction,
  * https://en.wikipedia.org/wiki/Journal_ranking

  and a popular ranking site:

  * https://www.scimagojr.com/

## IoT Textbooks

At the time of writing (Jnauary 2022), there is no single IoT Textbook that we can fully recommend. 
Some  reasons for this might be
  - Diversity of IoT: The term 'IoT' contains far too many things (pun intended) to be addressed in one coherent view or book.
    - Authors tend to always present from their respective angle, depending on what industry or research area they come from.
  - Fast technological development, industry/markets driven - the latest developments relevant for our field literally are not older than just a few months or years.

Among the most useful introductory textbooks:

Buyya, R., & Dastjerdi, A. V. (Eds.). (2016). Internet of Things: Principles and paradigms. Elsevier.

Chaudhari, B. S., & Zennaro, M. (Eds.). (2020). LPWAN Technologies for IoT and M2M Applications. Academic Press.

## Introduction

### Historical context:

D. Estrin, D. Culler, K. Pister and G. Sukhatme, "Connecting the physical world with pervasive networks," in IEEE Pervasive Computing, vol. 1, no. 1, pp. 59-69, Jan.-March 2002, doi: 10.1109/MPRV.2002.993145.
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=993145

Weiser, M. (1991). The Computer for the 21 st Century. Scientific american, 265(3), 94-105.
https://www.jstor.org/stable/24938718 

#### Definiton & Scope:

Overview of the Internet of things, Recommendation ITU-T Y.2060
https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-Y.2060-201206-I!!PDF-E&type=items
```
Ignore the formal sections, read:
3.2 Terms defined in this Recommendation
6 Introduction of the IoT
7 Fundamental characteristics and high-level requirements of the IoT
8 IoT reference model
Appendix I
IoT ecosystem and business models
```


## Architectures

Krčo, S., Pokrić, B., & Carrez, F. (2014, March). Designing IoT architecture (s): A European perspective. In 2014 IEEE world forum on internet of things (WF-IoT) (pp. 79-84). IEEE.

Eclipse IoT Working Group. (2016). The three software stacks required for iot architectures. IoT software requirements and how to implement then using open source technology.
https://iot.eclipse.org/community/resources/white-papers/pdf/Eclipse%20IoT%20White%20Paper%20-%20The%20Three%20Software%20Stacks%20Required%20for%20IoT%20Architectures.pdf

Zeuch, S., Chaudhary, A., Del Monte, B., Gavriilidis, H., Giouroukis, D., Grulich, P. M., ... & Markl, V. (2019). The nebulastream platform: Data and application management for the internet of things. arXiv preprint arXiv:1910.07867.

https://www.nebula.stream/paper/zeuch_cidr20.pdf

## Sensors

With one or two grains of salt added, read:
Sehrawat, Deepti, and Nasib Singh Gill. "Smart sensors: Analysis of different types of IoT sensors." 2019 3rd International Conference on Trends in Electronics and Informatics (ICOEI). IEEE, 2019. - 
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8862778

National Instruments Measurement Fundamentals series - http://www.ni.com/white-paper/14860/en/

## Embedded systems

Saltzer, J. H., & Kaashoek, M. F. (2009). Principles of computer system design: an introduction. Morgan Kaufmann.

Barr, M., & Massa, A. (2006). Programming embedded systems: with C and GNU development tools. " O'Reilly Media, Inc.".

Heath, S. (2002). Embedded systems design. Elsevier

Opler, Ascher (January 1967). "Fourth-Generation Software". Datamation. 13 (1): 22–24.
via archive.org:
https://ia600102.us.archive.org/17/items/TNM_4th_generation_software_hardware_-_Datamation_20171010_0125/TNM_4th_generation_software_hardware_-_Datamation_20171010_0125.pdf

Hahm, O., Baccelli, E., Petersen, H., & Tsiftes, N. (2015). 
Operating systems for low-end devices in the internet of things: a survey. 
IEEE Internet of Things Journal, 3(5), 720-734

E.Baccelli et al., RIOT: an Open Source Operating System for Low-end Embedded Devices in the IoT, IEEE Internet of Things Journal, 2018.

## Networking

Tanenbaum, A. S., & Wetherall, D. (1996). Computer networks. Prentice-Hall international editions, I-XVII.
Please read: Ch. 1.4 Reference Models

Flickenger, R. (2007). Wireless Networking in the Developing World: A practical guide to planning and building low-cost telecommunications infrastructure. Hacker Friendly LLC, Seattle, WA, US.
Chapters 1 & 4

optional. in-depth radio propagation - a glimpse into:

Barclay, L. (Ed.). (2003). Propagation of radiowaves (Vol. 2). Iet.

### LPWAN

Raza, Usman, Parag Kulkarni, and Mahesh Sooriyabandara. "Low power wide area networks: An overview." ieee communications surveys & tutorials 19.2 (2017): 855-873.
https://ieeexplore.ieee.org/abstract/document/7815384

Chaudhari, Bharat S., Marco Zennaro, and Suresh Borkar. "LPWAN technologies: Emerging application characteristics, requirements, and design considerations." Future Internet 12.3 (2020): 46.
https://www.mdpi.com/1999-5903/12/3/46

Mekki, Kais, et al. "A comparative study of LPWAN technologies for large-scale IoT deployment." ICT express 5.1 (2019): 1-7.
https://www.sciencedirect.com/science/article/pii/S2405959517302953

#### esp. LoRaWAN

de Carvalho Silva, Jonathan, et al. "LoRaWAN—A low power WAN protocol for Internet of Things: A review and opportunities." 2017 2nd International Multidisciplinary Conference on Computer and Energy Science (SpliTech). IEEE, 2017.
https://ieeexplore.ieee.org/abstract/document/8019271

Haxhibeqiri, Jetmir, et al. "A survey of LoRaWAN for IoT: From technology to application." Sensors 18.11 (2018): 3995.
https://www.mdpi.com/1424-8220/18/11/3995

### Layer models / OSI/ISO:

Day, J. D., & Zimmermann, H. (1983). The OSI reference model. Proceedings of the IEEE, 71(12), 1334-1340.
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1457043

Briscoe, N. (2000). Understanding the OSI 7-layer model. PC Network Advisor, 120(2), 13-15.
https://www.os3.nl/_media/info/5_osi_model.pdf

## Security

LoRaWAN Networks Susceptible to Hacking: Common Cyber Security Problems, How to Detect and Prevent Them

https://act-on.ioactive.com/acton/attachment/34793/f-87b45f5f-f181-44fc-82a8-8e53c501dc4e/1/-/-/-/-/LoRaWAN%20Networks%20Susceptible%20to%20Hacking.pdf

Ferrara, P., Mandal, A. K., Cortesi, A., & Spoto, F. (2020). Static analysis for discovering IoT vulnerabilities. International Journal on Software Tools for Technology Transfer, 1-18
https://link.springer.com/article/10.1007/s10009-020-00592-x

Neshenko, N., Bou-Harb, E., Crichigno, J., Kaddoum, G., & Ghani, N. (2019). Demystifying IoT security: an exhaustive survey on IoT vulnerabilities and a first empirical look on internet-scale IoT exploitations. IEEE Communications Surveys & Tutorials, 21(3), 2702-2733.
https://ieeexplore.ieee.org/abstract/document/8688434

Yin, L., Fang, B., Guo, Y., Sun, Z., & Tian, Z. (2020). Hierarchically defining Internet of Things security: From CIA to CACA. International Journal of Distributed Sensor Networks, 16(1), 1550147719899374.

 Additional reading on security, suggested Philippe Bonnet - Thursday, 13 April 2023:
  	
    Useful documents related to IoT security: https://www.enisa.europa.eu/news/enisa-news/iot-security-enisa-publishes-guidelines-on-securing-the-iot-supply-chain
    
    OWASP IoT Top 10: https://wiki.owasp.org/index.php/OWASP_Internet_of_Things_Project
    
    Standards for IoT security: https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program


## Energy

Wang, K., Wang, Y., Sun, Y., Guo, S., & Wu, J. (2016). Green industrial Internet of Things architecture: An energy-efficient perspective. IEEE Communications Magazine, 54(12), 48-54.
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7785890


## Data stacks & analytics

Recommended reading:

Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Edition - Aurélien Géron
First 2 sections of Chapter 1, and all of Chapter 2.
It's fairly many pages, but there's a lot of figures and code snippets, and it does a great job of demystifying ML systems.

https://github.com/quantumahesh/Hands-On-Machine-Learning-Book/blob/master/Hands-on-Machine-Learning.pdf

Supplementary reading:

Time series analysis in Python - Kaggle Notebook
https://www.kaggle.com/kashnitsky/topic-9-part-1-time-series-analysis-in-python
Gives a nice intro on how to handle time-series data in ML.


## Societal and ethical aspects

Tolmie, P., Crabtree, A., Rodden, T., Colley, J., & Luger, E. (2016, February). “This has to be the cats” Personal Data Legibility in Networked Sensing Systems. In Proceedings of the 19th ACM Conference on Computer-Supported Cooperative Work & Social Computing (pp. 491-502).
https://dl.acm.org/doi/abs/10.1145/2818048.2819992

## Edge Computing

AI / ML / TinyML - see https://github.com/things-guide/things-guide-resources/wiki/Embedded-ML

## Satellite IoT



Wei, J., Han, J., & Cao, S. (2019). Satellite IoT edge intelligent computing: A research on architecture. Electronics, 8(11), 1247.
https://www.mdpi.com/2079-9292/8/11/1247

McDowell, Jonathan C. "The low earth orbit satellite population and impacts of the SpaceX Starlink constellation." The Astrophysical Journal Letters 892.2 (2020): L36.
https://iopscience.iop.org/article/10.3847/2041-8213/ab8016/meta
 
 Qu, Zhicheng, et al. "LEO satellite constellation for Internet of Things." IEEE access 5 (2017): 18391-18401.
 https://ieeexplore.ieee.org/abstract/document/8002583
 
 Huang, Huawei, et al. "Green data-collection from geo-distributed IoT networks through low-earth-orbit satellites." IEEE Transactions on Green Communications and Networking 3.3 (2019): 806-816.
 https://ieeexplore.ieee.org/abstract/document/8681409
 
 Update on the Satellite Internet of Things Market, March 2022
 http://satellitemarkets.com/market-trends/update-satellite-internet-things-market
 
 Fraire, J. A., Céspedes, S., & Accettura, N. (2019, October). Direct-To-Satellite IoT-A Survey of the State of the Art and Future Research Perspectives. In International Conference on Ad-Hoc Networks and Wireless (pp. 241-258). Springer, Cham.
https://link.springer.com/chapter/10.1007/978-3-030-31831-4_17

## Guides, Coding, Hacking

```
Programming with MicroPython
by Nicholas H. Tollervey
Released October 2017
Publisher(s): O'Reilly Media, Inc.
ISBN: 9781491972731
```

