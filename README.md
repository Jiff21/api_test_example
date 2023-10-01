# BDD Python Selenium Behave 

## Introduction

A portfollio example of API Tests using 

See [feature files](/features) for what I'm testing and [steps directory](/features/steps) for code samples.

I used a variety of differing selectors, interaction methods & waits to demonstrate my knowledge of selenium. I chose to write the tests against a saucelabs demo site to minimize maintenace. 

## Install

### Dependancies

* [Python 3](https://www.python.org/downloads/).
* Virtualenv (`pip3 install virtualenv`).
* [Docker](https://docs.docker.com/engine/install/)

### Install steps

```bash
virtualenv -p python3.11 env
source env/bin/activate
pip3 install -U -r requirements.txt
docker pull swaggerapi/petstore3:unstable
```

## Running Tests

To have an API To test against I'm using Swaggers Pets Stor API. So in a terminal tab, run petsore.

```bash
docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:unstable
```

Then to run the tests:

```bash
behave features
```

## Allure reports

For a prettier report checkout [Allure](https://docs.qameta.io/allure/) reports with the steps below.

### Install

```bash
brew install allure
```

### Run

```bash
behave -f allure_behave.formatter:AllureFormatter -o utilities/allure/allure_results ./features
```

### Generate and run reports.

```bash
allure generate utilities/allure/allure_results/ -o utilities/allure/allure-reports/ --clean
allure open utilities/allure/allure-reports/
```


If you want a History section next time you run, you need to copy the history from the previous report, before generating the next report.

```bash
rm -R utilities/allure/allure_results/*
cp -R utilities/allure/allure-reports/history/ utilities/allure/allure_results/history
```