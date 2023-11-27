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
│   ├── final.dvc
│   ├── processed                      --> Processed Data
│   ├── processed.dvc
│   ├── raw                            --> Raw Data
│   └── raw.dvc
├── docs/                              --> Documentation Directory
│   ├── Data.md                        --> Data Documentation
│   ├── Preprocess.md                  --> Preprocessing Documentation
│   ├── Analysis.md                    --> Analysis Documentation
│   ├── Modelling.md                   --> Modelling Documentation
│   ├── Deployment.md                  --> Deployment Documentation
│   └── assets/                        --> Documentation Assets
├── lib/                               --> Library Directory
│   └── __init__.py
├── poetry.lock                       --> Poetry Lock File
├── pyproject.toml                    --> Poetry Project File
└── src/                              --> Source Directory
    ├── task-1/                       --> Task 1 Directory (Data Collection)
    │   ├── README.md                 --> Task 1 README
    │   └── notebook/                 --> Task 1 Notebook Directory
    ├── task-2/                       --> Task 2 Directory (Data Preprocessing)
    │   ├── README.md                 --> Task 2 README
    │   └── notebook/                 --> Task 2 Notebook Directory
    ├── task-3/                       --> Task 3 Directory (Data Analysis)
    │   ├── README.md                 --> Task 3 README
    │   └── notebook/                 --> Task 3 Notebook Directory
    ├── task-4/                       --> Task 4 Directory (Modelling)
    │   ├── README.md                 --> Task 4 README
    │   └── notebook/                 --> Task 4 Notebook Directory
    └── task-5/                       --> Task 5 Directory (Deployment)
        └── README.md                 --> Task 5 README
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
