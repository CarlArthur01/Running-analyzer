# Running Analyzer 🏃‍♂️

A full-stack application for analyzing Strava running data with machine learning predictions.

## 🎯 Features

- **Data Analysis**: Comprehensive analysis of running activities
- **Visualizations**: Interactive charts showing pace, volume, and progress
- **ML Predictions**: Predict race times for 5K, 10K, Half Marathon, and Marathon
- **Feature Importance**: Identify which training factors most impact performance
- **Modern Dashboard**: Clean, responsive web interface

## 🛠️ Tech Stack

### Backend
- **Python 3.11+**
- **FastAPI** - Modern REST API
- **scikit-learn** - Machine learning
- **pandas/numpy** - Data processing
- **Jupyter** - Data analysis notebooks

### Frontend (Coming Soon)
- **React + TypeScript**
- **Next.js** - Framework
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization

## 📁 Project Structure

```
running-analyzer/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── api/                 # API routes
│   │   ├── models/              # ML models
│   │   ├── services/            # Business logic
│   │   └── utils/               # Utilities
│   ├── notebooks/               # Jupyter notebooks
│   │   ├── 01_data_cleaning.ipynb
│   │   ├── 02_eda.ipynb
│   │   ├── 03_feature_engineering.ipynb
│   │   └── 04_model_training.ipynb
│   ├── data/
│   │   ├── raw/                 # Raw Strava data
│   │   └── processed/           # Cleaned data
│   └── requirements.txt
└── frontend/                    # React/Next.js app (coming soon)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Conda or venv
- Strava data export (CSV)

### Installation

1. **Clone the repository**
```bash
cd Running-analyzer
```

2. **Set up Python environment**
```bash
# Using conda (recommended)
conda create -n running-analyzer python=3.11
conda activate running-analyzer

# Or using venv
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
cd backend
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Running the Backend

```bash
cd backend
uvicorn app.main:app --reload
```

API will be available at: `http://localhost:8000`
API docs: `http://localhost:8000/docs`

### Data Processing

1. Place your Strava data in `backend/data/raw/activities.csv`
2. Open and run notebooks in order:
   - `01_data_cleaning.ipynb` - Clean and structure data
   - `02_eda.ipynb` - Exploratory analysis
   - `03_feature_engineering.ipynb` - Create ML features
   - `04_model_training.ipynb` - Train prediction model

## 📊 API Endpoints

- `GET /api/stats` - Overall statistics
- `GET /api/activities` - List of activities
- `GET /api/charts/pace` - Pace progression data
- `GET /api/charts/volume` - Training volume data
- `POST /api/predict` - Predict race times
- `GET /api/features` - Feature importance

## 🔮 Roadmap

- [x] Project structure setup
- [x] Backend API skeleton
- [ ] Data cleaning and processing
- [ ] Exploratory data analysis
- [ ] Feature engineering
- [ ] ML model training
- [ ] Frontend development
- [ ] Docker containerization
- [ ] Deployment

## 📝 Development

### Running Tests
```bash
cd backend
pytest
```

### Code Style
```bash
black app/
flake8 app/
```

## 📄 License

MIT License

## 👤 Author

Carl Arthur

---

**Note**: This project is under active development. Check back for updates!
