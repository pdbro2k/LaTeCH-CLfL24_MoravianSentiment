# LaTeCH-CLfL24_MoravianSentiment
Data and Code for the Paper "Modeling Moravian Memoirs: Ternary Sentiment Analysis in a Low Resource Setting" presented at LaTeCH-CLfL 2024

A presentation can be found at https://digicademy.github.io/2024_LaTeCH-CLfL_Moravian-Sentiment/

## Requirements

- Python 3.8.10
- install from requirements.txt
- store GerVADER from https://github.com/KarstenAMF/GerVADER into lib
- store SentiWS_v2.0 from https://www.wortschatz.uni-leipzig.de/de/download into models/lexical-resources

## Folder Structure

```bash
LaTeCH-CLfL24_MoravianSentiment
│
├───data
│   ├───error-analysis # (Categorized) misclassifications of the best performing fine-tuned model
│   ├───fine-tuning # Train/test datasets (and metadata)
│   ├───predictions # Model predictions
│   └───shap # (Grouped) shap values for eXplainability analyses
├───lib
│   └───GerVADER # See requirements
├───models
│   ├───fine-tuned # Content can be generated with the notebooks in scripts/fine-tuning 
│   └───lexical-resources
│       └───SentiWS_v2.0 # See requirements
└───scripts
    ├───applications # Notebooks used for research-driven applications
    ├───classification # Notebooks used to evaluate model performances
    ├───error-analysis # Notebooks used to analyze misclassifications
    ├───explainability # Notebooks used to conduct explainability analyses
    ├───fine-tuning # Notebooks used to fine-tune transformer models
    ├───metadata # Notebook used to analyze metadata
    └───utils # Some helper functions
```