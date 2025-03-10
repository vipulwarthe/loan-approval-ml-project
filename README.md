# loan-application
loan approval prediction application

# Machin learning project on Loan approval Status:
===============================================

    ## githug link: https://github.com/vipulwarthe/loan-approval-project-deploy-with-flask


The major aim of this project is to predict which of the customers will have their loan approved.

The main objective for this dataset:

Using machine learning techniques to predict loan payments.

updated process:

## Create one instance with ubuntu 20.04 AMI/t2.medium/sg-SSH/All Traffic-anywhere/30gb and connect with VS code.

    1  sudo su
    2  sudo apt-get update
    3  sudo apt-get upgrade -y   
    4  sudo apt install python3-venv -y
    5  python3 -m venv MLPRO
    6  source MLPRO/bin/activate  
    7  mkdir mlproject
    8  cd mlproject 

## create empty repo in github with name loan-application with README.md and .gitignore file with python extention and select licience type MIT. 
     
    9  git clone https://github.com/vipulwarthe/loan-approval-project-deploy-with-flask 
 
Or you can directly clone the repo and work on it.

    10 ls
    11 chmod 700 loan-application
    12 cd loan-application

## create requirements.txt and setup.py files in loan-application folder and run below cmd

setup.py - build and distribute Python packages

requirements.txt file - is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project
       
       sudo apt install python3-pip
    13 pip install -r requirements.txt
    14 git status
    15 git add .
    16 git commit -m "packages updated"
    17 git push origin main   (add username and password)
 
Github New token : 

## Create one notebook folder and add .ipynb file and LoanData.csv file in it and run the ipynb file.

-if kernel is not set then install manually python 

    sudo apt-get update

    sudo apt-get install python3 python3-venv python-pip

    18 pip install ipykernel -U --force-reinstall

Now run .ipynb file and predict the loan prediction.
    
    19 git status
    20 git add .
    21 git commit -m "notebook file updated"
    22 git push origin main   (add username and password)

## Create on templates folder and add home.html and index.html files with code also create application.py file in loan-approval project repo.

    23 python application.py

Open the browser and check your loan-approval application is running or not.

You will see the loan approval application is running on 5000 port

Open new terminal on vs-code and activate python envirnoment

      ls
      cd mlproject
      cd loan-application
      source myvenv/bin/activate
      git config --global --add safe.directory /home/ubuntu/mlproject/loan-application
      git status
      git add .
      git commit -m "templates folder added"
      git push origin main

If you will get below error: use below commands to resolve the error of github permissions

fatal: Unable to create '/home/ubuntu/mlproject/loan-application/.git/index.lock': Permission denied

    ls -l /home/ubuntu/mlproject/

    sudo chown -R ubuntu:ubuntu /home/ubuntu/mlproject/

    git config user.name "VipulWarthe"

    git config user.email "vipulwarthey@gmail.com"

## Deploy the model with AWS ElasticBeanstalk and AWS CodePipeline:

-first create IAM role for user -roles- create role - select ec2 

1) AWSElasticBeanstalkWebTier 
2) AWSElasticBeanstalkWorkerTier 
3) AWSElasticBeanstalkMulticontainerDocker

-create role

Elastic beanstalk: 

-create application-application name-(student performance)

-platform-python3.7

-application code-sample application - Presets - Single instance (free tier eligible)

-Service access-Use an existing service role-aws-elasticbeanstalk-service-role

-key pair - give any - ec2 instace profile - select created profile - skip to review - submit

-till elastic beanstalk envirnoment geting ready we can not create codepipeline(waite for it)

codepipeline:

-create pipeline -pipeline name-student_performance

-service role-new service role-advance setting-default

-next-source provider-github(version1)-connect to the github-

-confirm-select repo-mlproject-Branch-main

-change detection option-Github webhooks-next-

-Add build stage - skip build stage-next-Deploy-Deploy provider-

-AWS elastic beanstalk - Region-select your region-next-

-Application name-student performance-Envirnoment name- studentperformance-env --next- wait for envirnoment create-

-go to the Applications tab and click- select your application name-next-click on create pipeline

-click inside in deploy on AWS elastic beanstalk it will open link in browser

-go to the elastic beanstalk dashboard - you will see the studentperformance-env - click on Domain URL it will open in browser

-you will see the home page -just write /predictdata after your URL you will see the prediction page.


-deletation process - first delete codepipeline - then delete elastice beanstalk -then terminate the instance

