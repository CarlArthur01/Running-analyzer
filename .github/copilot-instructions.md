# Running Activity Analysis Project

## Project Overview
This project analyzes running and fitness activities exported from Strava. The data pipeline cleans and processes GPS activity data to compare metrics like pace, heart rate, cadence, elevation, and performance across different times of day.

## Data Architecture

### Input Data: `activities.csv`
- **Source**: Strava bulk export (multi-activity CSV format)
- **Structure**: Each row is one activity with 80+ columns including duplicated field names
- **Key fields**: Activity ID, Activity Type (Run/Golf), Elapsed Time, Distance, Heart Rate (max/avg), Pace, Cadence (max/avg), Elevation Gain/Loss, Speed (max/avg), Calories, Start Time
- **Important**: Column names have mixed case in raw data and are normalized to lowercase in the pipeline

### Data Processing Pipeline: `data_cleaner.ipynb`
1. **Load**: Read `activities.csv` with pandas
2. **Normalize**: Convert all column names to lowercase with `.str.lower()`
3. **Select**: Extract 16 relevant columns for analysis (see `relevant_columns` list in cell 3)
4. **Analyze**: Compare metrics across dimensions - time of day, heart rate zones, pace, cadence, elevation, distance, duration

## Project Conventions

### Column Name Handling
- **Always** normalize column names to lowercase immediately after loading: `data.columns = data.columns.str.lower()`
- Reference columns using lowercase names: `'activity id'`, `'elapsed time'`, `'max heart rate'`
- Original CSV has mixed-case column names, but code expects lowercase

### Activity Type Filtering
- Dataset includes multiple activity types (Run, Golf, etc.)
- Primary focus is on running activities
- Filter using: `data[data['activity type'] == 'Run']`

### Core Metrics for Analysis
The pipeline focuses on these 16 columns (order matters for reproducibility):
```python
['activity id', 'activity type', 'elapsed time', 'distance', 'max heart rate', 
 'average heart rate', 'pace', 'cadence', 'elevation gain', 'elevation loss', 
 'max speed', 'average speed', 'max cadence', 'average cadence', 'calories', 'start time']
```

### Time-Based Analysis
- `start time` field contains timestamps for analyzing performance by time of day
- Analysis goals include comparing: morning vs afternoon vs evening runs
- Consider parsing with `pd.to_datetime()` for time-of-day extraction

## Development Workflow

### Environment Setup
- Python with pandas and numpy (core dependencies)
- Jupyter notebook environment for interactive exploration
- No additional external APIs or services

### Running Analysis
- Open `data_cleaner.ipynb` in Jupyter
- Execute cells sequentially from top to bottom
- First cell loads data and shows shape
- Second cell normalizes columns and displays info/head
- Third cell selects relevant columns

### Data Validation
- Use `data.shape` to verify row/column counts after each transformation
- Use `data.info()` to check data types and non-null counts
- Use `data.head()` to visually inspect transformations

## Key Patterns

### Missing Data Strategy
- Strava export contains many columns not relevant to running analysis
- Some runs may have incomplete sensor data (e.g., no heart rate monitor)
- Handle with pandas `.isna()` checks before aggregations

### File Organization
- `activities.csv` - Raw data source (not versioned if large)
- `data_cleaner.ipynb` - Main analysis notebook
- No separate module/script structure yet; all code in notebook

## Future Extensibility
Code comments indicate planned comparisons:
- Time of day performance
- Heart rate zone analysis
- Pace trends
- Cadence patterns
- Elevation impact on performance
- Distance vs duration correlations
