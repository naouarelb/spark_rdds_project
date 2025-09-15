# 🚀 Spark Data Processing Project
This project is a Spark application designed to test how Spark work on large datasets in a distributed environment.
It runs inside a Docker-based Spark cluster (using Bitnami Spark images), making it easy to scale and reproduce.

# 📂 Project Structure
```plaintext
.
├── application/
│   ├── app/
│   │   ├── main.py                 # Entry point of the Spark job
│   │   │
│   │   ├── transformation/         # Transformation logic and helpers
│   │   │   ├── analysis.py         # Data analysis functions
│   │   │   ├── cleaning.py         # Data cleaning and preprocessing
│   │   │   ├── utils.py            # General utilities (load, save, helpers)
│   │   │   └── logs.py             # Logging and monitoring helpers
│   │   │
│   │   ├── output/                 # Job outputs (Parquet, CSV, etc.)
│   │   ├── README.md               # App-specific documentation (logic, transformations)
│   │   └── .env                    # Environment variables for the app
│   │
│   ├── data/                       # Input datasets (CSV, JSON, etc.)
│   ├── tmp/                        # Temporary working directory (intermediate files)
│   └── logs/                       # Spark/Job logs
│
├── docker-compose.yml              # Spark cluster setup (master + workers)
├── Dockerfile                      # Custom Spark image definition
├── generate_data                   # Script to generate mock/test data
├── requirements.txt                # Python dependencies
└── README.md                       # Project-level documentation (setup, run instructions)
```

# ⚙️ Requirements

- Docker version 28.4.0
- docker-compose version 1.29.2
- Datasets in CSV format
- Python 3.10.12 