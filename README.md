# Classification Project - Telco Churn

## About the Project 

### Project Goals

The goal of this project is to identify drivers of customer churn and and make a recommend changes that will ncrease customer retention.

### Project Description

Customer churn is a problem that is costing Telco revenue. This project attempts to identify reasons for customer churn in order to increase customer retention and reduce loss of revenue. The knowledge gained could expand beyond customer retention to improve sales by identifying what customers like and dislike. This project will anaylize the attributes of customers that churn to build a model that will predict the probablity of a customer churning given specific attributes. 

### Initial Questions

How many customers are churning and not churning?
What is the timeline of churn?
At what month of tenure are they churning?
What non-monetary drivers are associated with churned customers?
What monetary drivers are associated with churned customers?
Do monetary drivers outweigh non-monetary drivers?
What drivers are easiest to change with least amount of impact to the customer?

### Data Dictionary


| Variable              | Meaning                                                                           |
|:----------------------|:----------------------------------------------------------------------------------|
| customer_id           | alphas numeric identifer for each customer                                        |
| gender                | if customer is male or female                                                     |
| senior_citizen        | if customer is a senior citizen or not                                            |
| partner               | if customer has a partner or not                                                  |
| dependents            | if customer has dependents or not                                                 |
| tenure                | number of months the customer has been with telco                                 |
| phone_service         | if customer has phone service or not                                              |
| multiple_lines        | if customer has phone multiple phone lines or not, or no phone service            |
| online_security       | if customer has online security or not, or no internet service                    |
| online_backup         | if customer has online backup or not, or no internet service                      |
| device_protection     | if customer has device protection or not, or no internet service                  |
| tech_support          | if customer has tech support or not, or no internet service                       |
| streaming_tv          | if customer has streaming tv or not, or no internet service                       |
| streaming_movies      | if customer has streaming movies or not, or no internet service                   |
| paperless_billing     | if custome has paperless billing or not                                           |
| monthly_charges       | amount paid by custome per month                                                  |
| total_charges         | total amount paid by customer over tenure                                         |
| churn                 | if customer has left telco or not                                                 |
| contract_type         | if customer has a month-to-month, 1 year, or 2 year contract                      |
| internet_service_type | if customer's internet service is fiber optic, DSL, or no internet service        |
| payment_type          | payment is mailed check, electronic check, auto credit card, or auto bank account |


### Steps to Reproduce

1. clone my repo including the acquire_telco.py and prep_telco.py.
2. You will need an env.py file that contains the hostname, username and password of the mySQL server that contains the telco_churn database and tables. Store that env file locally in the repository. 
3. confirm .gitignore is hiding your env.py file so it won't get pushed to GitHub
4. neded libraries: pandas, matplotlib, seaborn, numpy, sklearn and scipy. 
5. you should be able to run telco_classification_final_report. 

### The Plan

#### Wrangle

##### Modules (acquire.py + prepare.py)

- *Module(s) with user-defined functions for acquiring and preparing the data should be created.*

- *Each function contains a helpful docstring explaining what it does, its input(s) and output(s).*

- *Credentials (such as in an env.py file) are NOT included in the public repo.*


1. write code to acquire data from MySQL Server.
2. tested code and add to acquire_telco.py as get_telco function
3. write code to remove duplicates, fill in blanks, converter data types, combine columns, replace values in column, set customer id column as index, create and concat dummy variables, set column names to lower case with underscores. 
4. add code to prep_telco file as clean_telco function
5. write code to split data into trian, validate, test
6. test code and add to prep_telco as split_telco funtion
7. write code to prepare train, validate, test data for model ingest
8. test code and add to prep_telco file as split_telco function
9. write code to create x and y versions for train, validate, test data samples
10. test and add code to prep_telco file as xy_version function
11. test all functions in working notebook to add to final report later

##### Missing Values (report.ipynb)

1. monthly_charges was missing values for all customers with tenure month 0. Instead of deleting those rows, I filled those values with 0.

##### Data Split (prepare.py (def function), report.ipynb (run function))

1. Use split_telco (train_test_split) to create train data (56%), validate data (24%), test data (20%) samples. Stratified on column 'churn'.

##### Using your modules (report.ipynb)

1. import acquire_telco.py and prep_telco.py into final report notebook for testing. 


#### Explore

##### Ask a clear question, [discover], provide a clear answer (report.ipynb)

1. What is the timeline of churn?

2. What are significant people attributes associated with churn?

3. What are significant service attributes associated with churn?

4. Do people attributes outweigh service attributes?

5. Is the average churn from customers using Manual Payment greater than the average churn of all customers?

6. For customers on month-to-month contract and using manual payment, is churn greater when using paperless billing or when having no dependents?


##### Exploring through visualizations (report.ipynb)

1. What is the timeline of churn?
- plot line graph with churn per month of tenure

2. What are significant people attributes associated with churn?
- plot bar graph of churn associated with attributes like dependents, payments type, contract type

3. What are significant service attributes associated with churn?
- plot bar graph of churn associated with attributes like internet types, online security, phone service

4. Do people attributes outweigh service attributes?
- plot pie chart to show churn differnce between selected attributes


##### Statistical tests (report.ipynb)

5. Is the average churn from customers using Manual Payment greater than the average churn of all customers?
- plot bar graph of churn for customer using manual payment with a horizontal line showing overall churn average
- use single t-test to prove churn of customer using manual payment is greater than overall churn

6. For customers on month-to-month contract and using manual payment, is churn greater when using paperless billing or when having no dependents?
- plot bar graph of churn of customers on month-to-month contracts and using manual payment to compare those customer who are also using paperles billing or have no dependenets. This is to isolate the attribute more associated to churn.
- use indepent t-test to compare those customers that use paperless billing to those with dependents

##### Summary (report.ipynb)

Filterd data to significant subgroup (groups with at least half differnece in categories). The filtered subgroups by significant churn (churn that at least doubls another). 

Following attributes has high association with churn: month-to-month contract, manual pay, paperless billing

#### Modeling

##### Select Evaluation Metric (Report.ipynb)

I used accuracy and precisoin. I accuracy as general score for prediction capability and recall because false negatives are favorable.

##### Evaluate Baseline (Report.ipynb)

basesline is created from most frequent case of churn which is 0 or no churn. baseline is at 73% probablity.

##### Develop 3 Models (Report.ipynb)

Used 3 different algorithms that are easiest to understand (decision tree, random forest, k-nearest neighbor). feature are the same with all however hyperparameter selected for accuracy.

#### Evaluate on Train (Report.ipynb)

Evlation of the three models show that they are not overfitt and KNN with 5 neighbors performed the best with 84% accuracy.

##### Evaluate on Validate (Report.ipynb)
 
- *The top models should be evaluated with the validation sample dataset. It is important to use the validate sample for checking for any overfitting that may have occurred when fitting the model on train. If you are creating 10's of models, it is also important to only validate a handful of your top models with the Validate dataset. Otherwise, your data will have seen validate as much as train and you could accidentally introduce some implicit bias based on data and results you see while validating on so many models. *

All three models went forward to validate. None were so bad or different that it made sense to remove. Random Forest with max_depth set to 4 performed the best with 80% accuracy and 45% recall. Using Random Forest going foward with Test data

##### Evaluate Top Model on Test (Report.ipynb)

Random Forest (model 2) performed with 80% accuracy and 44% recall, very close to validate data results, indicating that the model is not overfit and will product those result on future data.

## Report (Final Notebook) 

#### code commenting (Report.ipynb)

- *Your code contains code comments that are helpful to the reader in understanding what each blocks/lines of code are doing.*

#### markdown (Report.ipynb)

- *Notebook contains adequate markdown that documents your thought process, decision making, and navigation through the pipeline. This should be present throughout the notebook consistently, wtih not just headers, but plenty of content that guides the reader and leaves no questions or doubt as to why you did something, e.g.*

#### Written Conclusion Summary (Report.ipynb)

- *Your conclusion summary should addresses the questions you raised in the opening of the project, which we would want to see at the end of every final notebook. Ideally, when the deliverable is a report, the summary should tie together your analysis, the drivers of the outcome, and how you would expect your ML model to perform in the future on unseen data, in layman's terms.*



#### conclusion recommendations (Report.ipynb)

- *Your notebook should ends with a conclusion that contains  actionable recommendations based on your insights and analysis to the business stakeholder(s), your simulated audience, or someone who would find this information valuable (if there is no stakeholder). Your recommendations should not be not about what to do differently with the data, but instead should be based on the business or domain you are studying.*

#### conclusion next steps (Report.ipynb)

- *Your conclusion should include next steps from a data science perspective that will assist in improving your research. Ideally, if you talk about trying more algorithms to improve performance, think about why you need to improve performance. And if the business calls for it, remember the best way to improve performance is to have better predictors/features. If you talk about gathering more data, being specific about what data you think will help you understand the problem better and why is the way to go!*

#### no errors (Report.ipynb)

- *Your final notebook should run without error. One error in a notebook can lead to the rest of it erroring out. If you have a reader who doesn't know python, they will then not be able to consume your report.*

## Live Presentation

### intro (live)

- *Speaker kicks of the presentation by introducing themselves and their project through a one-liner of what it's about.*

### audience & setting  (live)

- *Always be aware of the audience and setting for your presentation.  What is the appropriate level of technicality? What is the appropriate depth given audience, setting and medium in which its delivered. The way you communicate should be appropriate for the audience: volume, speed of talk, flow, professionalism. (Codeup Data Science Instructor Team, virtually delivered via jupyter notebook).*

### content (live)

- *Notebook talked through step-by-step, in an understandable and meaningful way. Extraneous content in the notebook is not present.*

### Verbal Conclusion (findings, next steps, recommendations)  (live) 

- *Presentation is concluded with a summary of what was found, recommendations, and next steps. The presentation does not just drop off after modeling, but the entire project is nicely tied up and summarized.*

### time (live) 

- *Time limit of 5 minutes is adhered to. The time is managed well, in that there is appropriate time spent on each section. The time of 5 minutes should not be met by talking quickly but by reducing the amount or depth of information conveyed, and by finding easier and more simplified methods to convey the more complex information. The speech should be natural, and take the time needed for the audience to consume the information. So the time is well spent when you have practiced and you have taken the extra time it takes to reduce the content in your notebook and presentation. Time should not be spent scrolling through 10's of visualizations or hundreds of lines of code.*

## Deliver Predictions

### Deliver predictions (.csv) 

*A csv with predictions made from the top model developed should be submitted, as per instructions in the project spec.*

