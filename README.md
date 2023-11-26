# Hyderabad, India Chapter - Chatbot for Interview Preparation using NLP

## Table of Contents
- [About](#about)
- [Setup](#setup)
    - [Folder Structure](#folder-structure)
    - [Installation](#installation)
- [Collaborators](#collaborators)
- [License](#license)


## About
Omdena Hyderabad Local Chapter is working on a LLM based chatbot that can conduct mock interviews for aspiring candidates, evaluate the responses of job aspirants during mock HR interviews and provide quantitative, personalized feedback for each candidate along with recommendations to develop their skills to successfully navigate HR rounds of interviews.


## Setup

### Folder Structure

The project follows the following folder structure:

```
.
├── CONTRIBUTING.md                    --> Contributing Guidelines
├── README.md                          --> Project README
├── app/                               --> Streamlit App
│   └── main.py
├── data                               --> Data Directory
│   ├── README.md                      --> Data README
│   ├── final                          --> Final Data
│   └── final.dvc
├── docs/                              --> Documentation Directory
│   ├── Data.md                        --> Data Documentation
│   ├── Preprocess.md                  --> Preprocessing Documentation
│   ├── Analysis.md                    --> Analysis Documentation
│   ├── Modelling.md                   --> Modelling Documentation
│   ├── Deployment.md                  --> Deployment Documentation
│   └── assets                         --> Documentation Assets
├── lib/                               --> Library Directory
│   └── __init__.py
├── poetry.lock                       --> Poetry Lock File
├── pyproject.toml                    --> Poetry Project File
└── src/                              --> Source Directory
    ├── task-1/                       --> Task 1 Directory (Data Collection)
    │   ├── README.md                 --> Task 1 README
    │   ├── data/                     --> Task 1 Data Directory
    │   │   ├── README.md
    │   │   ├── external/             --> Task 1 External Data Directory
    │   │   ├── external.dvc
    │   │   ├── raw/                  --> Task 1 Raw Data Directory
    │   │   └── raw.dvc
    │   ├── docs/                     --> Task 1 Documentation Directory
    │   │   ├── Data.md
    │   │   └── assets/               --> Task 1 Documentation Assets
    │   ├── notebook/                 --> Task 1 Notebook Directory
    │   └── scripts/                  --> Task 1 Scripts Directory
    │       └── __init__.py
    ├── task-2/                       --> Task 2 Directory (Data Preprocessing)
    │   ├── README.md                 --> Task 2 README
    │   ├── data/                     --> Task 2 Data Directory
    │   │   ├── README.md
    │   │   ├── processed/            --> Task 2 Processed Data Directory
    │   │   └── processed.dvc
    │   ├── docs/                     --> Task 2 Documentation Directory
    │   │   ├── Preprocess.md
    │   │   └── assets/               --> Task 2 Documentation Assets
    │   ├── notebook/                 --> Task 2 Notebook Directory
    │   └── scripts/                  --> Task 2 Scripts Directory
    │       └── __init__.py
    ├── task-3/                       --> Task 3 Directory (Data Analysis)
    │   ├── README.md
    │   ├── docs
    │   │   ├── Analysis.md
    │   │   └── assets
    │   ├── notebook
    │   └── scripts
    │       └── __init__.py
    ├── task-4/                       --> Task 4 Directory (Modelling)
    │   ├── README.md                 --> Task 4 README
    │   ├── docs/                     --> Task 4 Documentation Directory
    │   │   ├── Modelling.md
    │   │   └── assets/               --> Task 4 Documentation Assets
    │   ├── lib/                      --> Task 4 Library Directory
    │   │   └── __init__.py
    │   └── notebook/                 --> Task 4 Notebook Directory
    └── task-5/                       --> Task 5 Directory (Deployment)
        ├── README.md                 --> Task 5 README
        └── docs/                     --> Task 5 Documentation Directory
            ├── Deployment.md
            └── assets/               --> Task 5 Documentation Assets
```


### Installation

To install the project, make sure you have 
- [Git](https://git-scm.com/downloads)
- [Python 3.10](https://www.python.org/downloads/release/python-31012/)
- [Poetry](https://python-poetry.org/docs/#installation) installed.

**1. Clone the repository**
```bash
git clone https://dagshub.com/Omdena/HyderabadIndiaChapter_ChatbotInterviewPreparation.git
```

**2. Install Poetry and activate the virtual environment**
```bash
poetry install
poetry shell
```

**3. Setup DVC**
```bash
dvc remote add origin s3://dvc
dvc remote modify origin endpointurl https://dagshub.com/Omdena/HyderabadIndiaChapter_ChatbotInterviewPreparation.s3
dvc remote modify origin --local access_key_id <your_token>
dvc remote modify origin --local secret_access_key <your_token>
```

**4. Get the data**
```bash
dvc pull
```

**5. Setup environment variables**
```bash
cp .env.example .env
```
Replace the values in `.env` with your own values.

**6. Run the app**
```bash
streamlit run app/main.py
```

## Collaborators


## License
