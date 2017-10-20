![](https://travis-ci.org/FlipWebApps/DataScienceTemplate.svg?branch=master)

# DataScienceTemplate
A template for data science projects

# Initial File Structure
The file structure should be considered dynamic based upon the working and evolution of your project.

├── .gitignore           <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if needed
├── .travis.yml          <- Travis CI guild file
├── LICENSE
├── README.md            <- The top-level README for developers using this project.
├── data
│   ├── interim_[desc]   <- Interim files - give these folders whatever name makes sense.
│   ├── processed        <- The final, canonical data sets for modeling.
│   └── raw              <- The original, immutable data dump.
│
├── docs                 <- Any specific documentation (try ideally to keep to README.md)
│
├── notebooks            <- Jupyter notebooks. Naming convention is a number (for ordering),
│                           the creator's initials, and a short `-` delimited description, e.g.
│                           `1.0-jqp-initial-data-exploration`.
├── requirements.txt     <- The requirements file for reproducing the analysis environment, e.g.
│                           generated with `pip freeze > requirements.txt`
│
├── code                 <- Code for use in this project.
│   ├── common           <- Folder for example common python functionality
│   │   ├── __init__.py  <- Makes src a Python module
│   │   └── example.py
│   │
│   └── tests            <- Example test cases
│       ├── __init__.py
│       └── test_common_example.py

# Testing
install pytest using pip or conda and then from the repository root run >>pytest
