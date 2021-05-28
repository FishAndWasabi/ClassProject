## Project 2

# How to improve the visualization:  a story with chart from medical paper 
+ Yuming Chen, chenym18@lzu.edu.cn, 320180939611
+ Huiyi Liu, liuhuiyi18@lzu.edu.cn, 320180940030


## 1. Abstract
We retrieved a number of recent academic papers on platforms such as Google Scholar and chose a relatively good and meaningful visualization to analysis after discussion. 

Then we provided a detailed explanation of the information visualization include the story in the visualization, its context, how to read it, what are the visual variables and  use some of the concepts from cognitive theory to explain the effectiveness of it. The aim is to help you better understand the information reflected by this visualization. The information visualization was then replicated using _Matplotlib_ with the process and code recorded in the jupyter notebook. 

Even if the visualization was carefully selected,  basically following the guidelines and principles of data visualization, there still existed some problems.  So we proposed changes that would improve the graph and implemented the changes, making it have a better performance. All the changes and the reasons were explained in detail. 

We hope to help you to have a better understanding of data visualization and be more interested in it. In addition, we are eager for making  progress  together with you, so please communicate with us with suggestions or better ideas. If you have questions or find mistakes in the process of reading this article, feel free to contact us via email.

## 2. Introduction

The bar chart we selected is shown below It is from a paper published in journal _Nature_. It is based on a research about the interactions of 8 drugs used for Covid-19 treatment with 645 different drugs, and displays the number of drugs that cause side effects when used together with the focused 8 drugs. The number of each disease group as results of side effects grouped by these 8 drugs is also shown. Closely related to COVID-19 epidemic, the graph has a great significance on current medical research and the society. 

![1.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/1.png)
This visualization is of great significance. As Covid-19 spreads rapidly worldside nowadays, great medical breakthroughs are required urgently to treat or prevent Covid-19 effectively. Scientists and researchers have published thousands of clinical trial results and articles to provide treatment methods for the disease. An important part of these studies examines the use of existing drugs for Covid-19 treatment, and suggests possible treatment methods. There have been some attempts to use some of these drugs in combination. However, using more than one drug together may cause serious side effects on patients. Therefore, detecting drug-drug interactions of the drugs used will be of great importance in the treatment of Covid-19. Besides, the visualization of side effects of drugs interaction are in  favour  of guiding  the medicine selection for doctors and researchers, as it is an essential issue that should be examined before recommending a drug to a patient and after treatment. With the experimental results obtained, the authors of this paper created this visualization, which is meaningful to facilitate the selection of appropriate drugs  according to the targeted patient.

The focus is on which disease group is mostly produced as a result of side effects. The chart summarizing the side effects in order to compare the effects of the drugs in general. However, there are problems about the chart, the most obvious one is that the chart contains three dimensions of information and uses the large legend, which overloads the reader's working memory and makes the visualization difficult to understand. We improved the chart by decomposing the graph into several pie charts and bar charts with each one reflects two-dimensional information, labeling elements directly instead of using legends, adding the interactive radio box for readers to select the information they need, removing non-data-ink such as grid lines and redundant data-ink such as y-axis, using colorblind-friendly palette and avoid similar colors, and adding titles to briefly illustrate the meaning of the visualization. In this way, readers are able to understand the information directly and easily.

## 3. Visualization description
Why we choose this visualization? As more and more people become infected with COVID-19, we are desperate for the appearance of a comprehensive medical plan to cure COVID-19 so that we are able not to be scared of it. Therefore, we pay great attention  to the relevant medical research. In the field of medical researching, side effects are important factors to consider, for they may make the situation even worse sometimes. Especially when using multiple drugs, side effects may add and result  in  serious  consequences. When we found this chart, we really looked forward to making more medical researchers and doctors get to know it so that they can suggest more appropriate treatment options based on it.

In the following subsections, we will introduce the detailed information of this graph including what are the sources of the graph and data, what is the story in the visualization, how to read it, what are the visual variables and so on. 

### 3.1 Source of visualization and data
The visualization is from a paper published in the scientific journal _Nature_: [Identifying side effects of commonly used drugs in the treatment of Covid 19](https://www.nature.com/articles/s41598-020-78697-1).It reflects the most common side effects of drugs used in Covid-19 treatment according to the results of the project's experiment.

A combination of three different data sources was used to select the drugs whose interactions with other drugs would be calculated. The first is the Decagon study, from which we use the network infrastructure. Another source is the LitCovid dataset, which compiles Covid-19 oriented studies on PubMed. The last one is an online system called "covid19-druginteractions.org" that predicts drug interactions which is shared by Liverpool University.

### 3.2 Explanation of the graph
![2.jpg](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/2.jpg)
Referred to Bertin’s Original Retinal Variables, the visual variables involved in this graph are as follows:
 - Size (height) of the bar
 The heights of the bars represent the number of drugs that cause side effects when used in conjunction with the focused drug.
 - Position of the bar 
 The positions of the bars represent the name of focused drugs.
 - Color of the bar 
 The colors of the bars reflect disease groups produced as results of side effects.
 
 The data types involved include categorical data (drugs and disease groups) and discrete data (number of the drugs ).
 
There are 8 focused drugs in the experiment: hydroxychlor oquine, chioroquine, azithromycin, ritonavir, ribavirin, atazanavir, heparin and clozapine. They are commonly used in the COVID-19 treatment. The graph reflects the side effects caused when each of these drugs are used together with other 645 drugs.

You may wonder how to read this graph. Take the first bar for example. We can find that the focused drug is hydroxychlor oquine according to the ticks on the x-axis. Among the 645 drugs, there are more than 150 drugs that have side effects when used together with hydroxychlor oquine. Among these 150 drugs, nearly half of them cause  hematopoietic system disease as results of side effects when used with hydroxychlor oquine. The other side effects caused include cardiovascular system disease, integumentary system disease and dizziness.

### 3.3 Story of the visualization

In December 2019, a coronavirus species that can spread from person to person was identified in Wuhan, China. The disease later on called Covid-19 posed a risk to be declared as a pandemic by the World Health Organization (WHO) in a short time. As of the date in early June 2020, more than 6.4 million people were infected with this virus, and 373,334 persons died. It has been realized that scientists and researchers have published thousands of clinical trial results and articles in this process to provide treatment methods for the disease. An important part of these studies examines the use of existing drugs for Covid-19 treatment, and suggests possible treatment methods.

One of the issues that should be examined before recommending a drug to a patient and after treatment is the side effects of the drug. Research shows that multiple drugs usage (polypharmacy) significantly increases drug side effects. For older patients, the probability of polypharmacy generally increases. However, studies clearly show that as the number of drugs used increases, the negative effects seen in patients may also increase. Therefore, it is vital to predict drug-drug interactions (DDI) and adverse drug reactions (ADR) for the drugs to be used in the treatment of a disease. Knowing the side effects and DDI of the drugs recommended in Covid-19 treatment will play an important role in the success of the process.

According to statistical studies, the vast majority of Covid-19 patients are seen at age 50 and over (Sobotka et al. 2020). According to the results of polypharmacy studies, regular and multiple drugs usage is over 60% in this age group. When these two examinations are evaluated together, it is understood that the rates of multiple drugs usage for Covid-19 patients are quite high. For this reason, the importance of DDI studies increases in Covid-19 treatment.

Under this circumstance, three scientists: Irfan Aygün, Mehmet Kaya and Reda Alhaji did researches and experiments in order to identifying side effects of commonly used drugs in the treatment of Covid-19 and their achievement was recently published in the top journal _Nature_ on Dec 09,2002. In this study, the interactions of 8 drugs used for Covid-19 treatment with 645 different drugs and possible side effects estimates have been produced using Graph Convolutional Networks. 

After the interactions of each drug were examined, the resulting side effects were classified. A drug which causes the same side effect as 25 or more drugs will have its side effects are added to the chart. This way, the most common side effects of the 8 drugs used in the experiments have been derived and visualized. In order to compare the effects of the drugs in general, the chart summarizing the side effects is shown.

According to the graph, we can come to conclusion that the hematopoietic system and the cardiovascular system are exposed to more side effects than other organs. Among the focused drugs, Heparin and Atazanavir appear to cause more adverse reactions than other drugs. 

### 3.4 Context of the visualization
Context is an essential factor that need to be thought about during the design of visualization, which include:
- __Purpose__
The graph is used for exploratory search, aiming to find the relations and comparisons between the side effects of different drug's interaction. It provides insights into and an understanding of the problem faced by the researcher. 
- __Readership__
For the reason that the visualization is from a medical academic paper published in a science journal, the expected main readers include medical researchers, scientists, doctors and other medical workers. It may also be analysed by readers who are interested in visualization.
- __Media__
The graph has already been presented in the academic journal. As its influence grow, it is expected to be presented in blogs on the website.
- __Visual guides__
There are other visual guides. The visualization is mainly focused on the comparison between the side effects of drug interaction of the target 8 drugs used in COVID-19 treatment and other drugs. Readers can get general information and overview of side effects caused by drug interaction. Therefore, readers who have medical knowledge may understand the information easier.

### 3.5 Evaluation of the graph
The visualization basically follow  the  principles for visualization and integrity. It creates a simple graph that conveys the information to be presented. It maximizes the data-ink ratio and avoids non-data-ink. It erases part of redundant data-ink. The height of the bar is proportional to the numerical quantities represented (the actual number of drugs).

From the perspective of cognitive theory, the disuse of animation avoids cognitive tunneling, helps the reader to better pay attention to the information represented. However, the use of legend with too many instances makes it hard for readers to memory, which not only wastes time to understand the information, but also distracts readers. Legends require the reader to go back and forward. They will not easily focus on the picture as a whole. If the reader enters a stage of cognitive tunnelling, he/she will not be able to process the graph. And the reader will have to load the working memory with the legend.

The visualization gives a fairly clear picture of the comparison of side effects of drug interation between different drugs. However, there still exists some problems such as the color of the bars are too similar to distinguish, the critical concrete values are hard to recognize, lack of labeling and so on. Besides, the comparison of different diseases groups of a certain drug is not that clear, for example, when considering side effects of azithromyci's drug interaction, which disease group has a larger proportion, integumentary system disease or cardiovascular system disease? Therefore, Some improvement can be taken to make it more readable.


## 4. Visualization improvement
Based on the analysis and evaluation above, we found that this visualization can be improved and have a better performance. Therefore, we discussed and determined the changes on the graph which are explained in this section.

### 4.1 Decompose the graph into pie charts and bar charts
We decomposed the original graph into 8 pie charts and 25 bar charts. The composition of each bar in the original graph is translated into a pie chart, and the bar charts only reflects general information rather than disease groups. Some examples are as follows:
![change1-1.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change1-1.png)
The pie chart above displays the names and proportions of the composited disease groups as side effects within the entire drug interactions.
![change1-2.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change1-2.png)
The bar chart above displays the number of drugs causing hematopoietic system disease as side effects in drug interaction with the eight focused drug used in COVID-19 treatment.

The decomposed pie charts reflect the composition and proportion of different disease groups as side effects of the interaction between the certain drug and other different drugs. It is used in the situation where medical researchers or doctors want to find out the side effects of drug interaction of a certain kind of drug, determining whether use it with other medicines when curing a patient with COVID-19 together with other diseases. The decomposed bar charts reflect the number of drugs which cause a certain disease group as side effects (or the total) when interacting with the focused drugs. It is used in the situation where medical researchers or doctors want to find out which drugs are not suitable for patients who have a certain kind of disease, and how likely the drugs will make their disease even worse because of the side effect.

The reason for this change is that according to the cognitive theory, the original graph contains too much information and too many legend instances which overloads readers' working memory. Decomposing the graph fits the little capacity of working memory, making the reader easier to focus on the information they need. Besides, this change could display more comparison relations.

Compared with the previous graph, the newly created graphs are more clear and readable. Readers can hardly compare some heights of different disease groups in the same bar in the original graph, but after this change applied, they can simply choose the corresponding drug and compare the proportions of each disease group in the pie chart. The reader can also get information faster in new graphs.

This change can also be applied to other generic graphs when the bar chart represents more than two information dimensions.

### 4.2 Label elements directly instead of using a legend in pie charts
For the pie charts, we directly label the disease groups on the pieces instead of using legends. As for the bar charts, there is always only one disease group with only one color, so color is not used as a visual variable and does not need to be taken into consideration.
![change2.jpg](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change2.jpg)
According to the practical guidelines for effective visualizations, we should label elements directly, avoiding indirect look-up. We remove the legends for the reason that legends require the reader to go back and forward, which prevent them from easily focusing on the picture as a whole. Besides, cognitive tunnelling may naturally happen when looking at a visual element in the graph, making the reader not able to process the graph. Moreover, The reader will have to load the working memory with the legend. If the user goes back and forth to the legend, it will have to process other elements in the graph which may overload the working memory.

In the original graph, readers need to go back and forward to process the legend. But now they can get the information directly with the help of labeling.

This change should also be applied to other generic graphs with legends unless the space is too tight.

### 4.3 Add the interactive radio box to select what to display 
We add a radio box to make it interactive. Readers are able to choose the information they are interested in and get more details. When choosing a drug, the corresponding pie chart which reflects side effects of its drug-drug interaction is displayed. The reader can get the information about the detailed disease groups and their proportions. When choosing a disease group, the corresponding bar chart is displayed, which reflects the drugs whose side effects of drug-drug interaction conclude the chosen disease group. The reader can get the information about the name of the drugs and the number of their drug-drug interactions which causes the selected disease.
![change3.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change3.png)
![change3-2.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change3-2.png)

According to the theory of Shneiderman, ontology of visualizations based on user task include overview, zoom, filter, details-on-demand, relate, history and extract. The preview visualization only covers overview and relate. We add some details-on-demand which allows readers to select an item and get details when needed. 

Compared with the previous graph, the newly created graphs are more targeted and there are less interference  information and interference variables.

This change should also be applied to other generic graphs when there are  a number of categories which makes it  hard for readers to find information about the one they interest in.

### 4.4 Remove the grid lines
We removed the horizontal grid lines of the original graph.
![grid.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change4.png)
According to the visualization principles,  non-data-ink shall be erased. As an instance of non-data-ink, the grid lines can distract the reader from the data, and competing for our attention based on cognitive theory. Therefore, the unnecessary grid lines are removed. 

When readers read the previous graph, their attention is likely to be distracted, they make use some working memory on the grid lines but gain nothing related to the information. However, they can concentrate on the useful information after this change applied.

This change can also be applied to other generic graphs with over-busy grid lines. Only lines that communicate or highlight some insight in the data are necessary.

### 4.5 Remove the y-axis in bar charts and label the value above each bar instead

We removed the y-axis in bar charts and labeled the value above each bar instead.
![y_label.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change5.png)
The labels on the y-axis are redundant data-ink which shall be erased according to the visualization principles when the redundancy does not have a distinctly worthy purpose. Labelling the values above the bars helps readers to get the exact values directly.

In previous graph, readers can only estimates the values or proportions by looking up the labels on the y-axis and the height of bars, while the changed graph makes it convenient for readers to find the values directly, comparing with more details. Besides, the distraction of the attention also decreases, the graph is simpler and can better emphasize the information.

This change can also be applied to other generic graphs with unnecessary labels on y-axis.

### 4.6 Use colorblind-friendly palette

We changed the colors into colorblind-friendly palette with the guide of [Paul Tol's Notes (2019)](https://personal.sron.nl/~pault/):
![color.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change6.png)
Information visualization ought to be colorblind-friendly. In the real world, red–green color blindness is the most common form, followed by blue– yellow color blindness, and total color blindness. Therefore, we should avoid using these pairs of colors together. A problem of the original chart is that some of the colors used are too close to distinguish (such as orange and red), and some of them are not colorblind-friendly (such as using red together with green), which violates the practical guidelines for effective visualizations. Therefore, we carefully choose the colors used in charts and test the colour  palette with online color blindness simulation tools.

For color-blind readers, they may misunderstand the information when reading the previous graph but the problem does not bother them after this change applied. Moreover, readers may be confused when looking up the legend instances of similar colors. In the new graph, however, they are able to distinguish them easily. 

This change can also be applied to other generic graphs that are not colorblind-friendly or when the colors used in the graph are too similar, especially when color is a visual variable that carries information.

### 4.7 Add title for charts
We added titles for bar charts and pie charts, instructing the meaning and information of the graph briefly.
![final-1.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change7-1.png)
![final-2.png](https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper/raw/main/images/change7-2.png)
According to the practical guidelines for effective visualizations, graphs should have a clear, self‐explanatory title or caption. Original graph is lack of explanation to help readers understand the data. Insights from data cannot be provided without context. Without the right context, visualizations can be misleading. The titles instruct the purpose of data in some degree, which explains some of the context.

In the original graph, it is difficult for the reader to understand the meaning, context and story of the graph without the title or caption. After applying this change, readers are more likely to understand what the graph is about rapidly.

This change can also be applied to other generic graphs without titles or captions.

## 5. Conclusion
We have learned the ways to improve visualizations and have been aware of the problems in the visualization. A visualization should always take the story and context into consideration. If you have never encountered data visualization before, we hope that you have a general understanding  of data visualization by reading our story. We will analyse more visualization cases and then try to create our own creative and effective visualization based on meaningful data in order to learn visualization better. Please contact us if you have better advice or if you want to join us with interest in visualization.

This article is posted both on GitHub and on gitee which is a platform similar as GitHub, with complete code and images. Please visit our repository if you want to get more details.
github: https://github.com/Lucifer-x/visualization-story-with-a-chart-from-medical-paper.
gitee: https://gitee.com/iris_liu/visualization-story-with-a-chart-from-medical-paper.

