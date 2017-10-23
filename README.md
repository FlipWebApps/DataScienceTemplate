![](https://travis-ci.org/FlipWebApps/DataScienceTemplate.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/FlipWebApps/DataScienceTemplate/badge.svg?branch=master)](https://coveralls.io/github/FlipWebApps/DataScienceTemplate?branch=master)  

# DataScienceTemplate
A starting template for data science projects. This template should be adopted to your projects needs

# Initial File Structure
The file structure should be considered dynamic based upon the working and evolution of your project.

```
├── .gitignore           <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if needed
├── .travis.yml          <- Travis CI build file
├── environment.yml      <- conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md            <- The top-level README for developers using this project.
├── data
│   ├── interim_[desc]   <- Interim files - give these folders whatever name makes sense.
│   ├── processed        <- The final, canonical data sets for modeling.
│   └── raw              <- The original, immutable data dump.
│
├── docs                 <- Any specific documentation (try ideally to keep to README.md)
│
├── eda                  <- Exploratory analysis notebooks and files. 
│   └── example.ipynb    <- Example notebook
│
├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
│                           generated with `pip freeze > requirements.txt`
│
├── src                  <- Code for use in this project.
│   ├── __init__.py
│   ├── common           <- Folder for example common python functionality
│   │   ├── __init__.py
│   │   └── example.py   <- Example functions
│   │
│   └── tests            <- Test cases
│       ├── __init__.py
│       └── test_common_example.py     <- Example tests
```

# Testing
If a code block is copied more than one then it should be placed into a common script under src and unit tests added. The same applies for any other non trivial code to ensure the correct functioning.

To run tests, install pytest using pip or conda and then from the repository root run 
```pytest```
