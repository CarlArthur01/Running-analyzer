# Running Analyzer 🏃‍♂️

A soon to be application for analyzing Strava running data with machine learning predictions.

## Features

- **Data Analysis**: Comprehensive analysis of running activities
- **Visualizations**: Interactive charts showing pace, volume, and progress
- **ML Predictions**: Predict race times for 5K, 10K, Half Marathon, and Marathon
- **Feature Importance**: Identify which training factors most impact performance
- **Modern Dashboard**: Clean, responsive web interface


### Backend
- **Python 3.11+**
- **FastAPI** - Modern REST API
- **scikit-learn** - Machine learning
- **pandas/numpy** - Data processing
- **Jupyter** - Data analysis notebooks
```

### Data Processing

1. Place your Strava data in `backend/data/raw/activities.csv`
2. Open and run notebooks in order:
   - `01_data_cleaning.ipynb` - Clean and structure data
   - `02_eda.ipynb` - Exploratory analysis
   - `03_feature_engineering.ipynb` - Create ML features
   - `04_model_training.ipynb` - Train prediction model


 Roadmap

- [x] Project structure setup
- [x] Backend API skeleton
- [ ] Data cleaning and processing
- [ ] Exploratory data analysis
- [ ] Feature engineering
- [ ] ML model training
- [ ] Frontend development
- [ ] Docker containerization
- [ ] Deployment



## 👤 Author

Carl Arthur

---

**Note**: This project is under active development. Check back for updates!
