"""
Data Processing Service
Handles loading, cleaning, and processing of running data
"""
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any

class DataProcessor:
    """Process and analyze running data"""
    
    def __init__(self, data_path: str = "data/processed/activities_clean.csv"):
         # Initialize data processor
        self.data_path = Path(data_path)
        self.data = None
        
    def process_raw_data(self, raw_path: str = "data/raw/activities.csv"):
        #Process raw data, clean it, and saves to processed folder.
        # 1. Load Raw Data
        data = pd.read_csv(raw_path)
        
        # 2. Basic Cleaning
        data.columns = data.columns.str.lower().str.strip()
        relevant_columns = ['activity id','activity date', 'activity type', 'elapsed time', 'distance', 'max heart rate', 'average heart rate', 'elevation gain', 'elevation loss', 'max speed', 'average speed', 'max cadence','average cadence','calories']
        existing_cols = [c for c in relevant_columns if c in data.columns] #make sure they exist
        data = data[existing_cols].copy()
        
        # 3. Filter Runs
        data = data[data['activity type'] == 'Run']
        
        # 4. Dates
        data['activity date'] = pd.to_datetime(data['activity date'])

        # 5. Calculate Pace & Filter
        if 'average speed' in data.columns:
            data['average_km_h'] = data['average speed'] * 3.6
            # Avoid division by zero and make in to min/km
            data['pace'] = data['average_km_h'].apply(lambda x: 60 / x if x > 0 else 0)
            
            # Filter keep runs faster than 7.5 min/km
            data = data[(data['pace'] < 7.5) & (data['pace'] > 0)]

        # 6. Fix Cadence (x2 issue)
        if 'average cadence' in data.columns:
            # Convert to numeric, coerce errors, fill NaN with 0, then multiply
            data['average cadence'] = pd.to_numeric(data['average cadence']).fillna(0) * 2
        
        # 8. Save
        output_path = Path("data/processed/activities_clean.csv")
        data.to_csv(output_path, index=False)
        
        self.data = data
        return data

    def load_processed_data(self):
        #load the processed data
        if self.data_path.exists():
            self.data = pd.read_csv(self.data_path)
            self.data['activity date'] = pd.to_datetime(self.data['activity date'])
            return self.data
            
        print(f"Processed file not found at {self.data_path}. Running raw data processing...")
        try:
            return self.process_raw_data()
        except Exception as e:
            raise FileNotFoundError(f"Could not load or process data: {e}")
    
    def get_stats(self) -> Dict[str, Any]:
        #get some stats for the front page 
        if self.data is None:
            self.load_processed_data()
        
        stats = {
            "total_runs": len(self.data),
            "total_distance_km": self.data['distance'].sum(),
            "total_elevation_gain_m": self.data['elevation gain'].sum(),
            "longest run": self.data['distance'].max(),
        }
        
        return stats
    
    def get_latest_activities(self, limit: int = 50) -> List[Dict[str, Any]]:
       #get the latest activities for the front page
        if self.data is None:
            self.load_processed_data()
        
        return self.data.head(limit).to_dict('records')
    
    def get_pace_data(self) -> Dict[str, List]:
        #get pace progression data for plot
        if self.data is None:
            self.load_processed_data()
        
        # Sort by date
        df_sorted = self.data.sort_values('activity date')
        
        return {
            "dates": df_sorted['activity date'].tolist(),
            "pace": df_sorted['pace'].tolist()
        }
    
    def get_volume_data(self) -> Dict[str, List]:
        #get training volume data for plot
        if self.data is None:
            self.load_processed_data()
        
        # Group by week
        self.data['week'] = self.data['activity date'].dt.isocalendar().week
        weekly = self.data.groupby('week')['distance'].sum()
        
        return {
            "weeks": weekly.index.tolist(),
            "distance": weekly.values.tolist()
        }

    def get_monthly_volume(self) -> Dict[str, List]:
        #get total distance per month for plot
        if self.data is None:
            self.load_processed_data()
            
        # Create year_month column for grouping
        df_copy = self.data.copy()
        df_copy['year_month'] = df_copy['activity date'].dt.to_period('M').astype(str)
        
        monthly = df_copy.groupby('year_month')['distance'].sum().reset_index()
        
        return {
            "months": monthly['year_month'].tolist(),
            "volume": monthly['distance'].tolist()
        }

    def get_efficiency_data(self) -> Dict[str, List]:
        #get Heart Rate vs Pace data for efficiency analysis
        if self.data is None:
            self.load_processed_data()
            
        # Return simple lists for plotting: x=pace, y=heart_rate, color=year
        df_copy = self.data.dropna(subset=['pace', 'average heart rate'])
        df_copy['year'] = df_copy['activity date'].dt.year
        
        return {
            "pace": df_copy['pace'].tolist(),
            "heart_rate": df_copy['average heart rate'].tolist(),
            "years": df_copy['year'].tolist()
        }

    def get_cadence_data(self) -> Dict[str, List]:
        #get Cadence vs Pace data (excluding zeros)
        if self.data is None:
            self.load_processed_data()
            
        # Filter > 0 cadence
        mask = (self.data['average cadence'] > 0) & (self.data['pace'] > 0)
        df_filter = self.data[mask].copy()
        df_filter['year'] = df_filter['activity date'].dt.year
        
        return {
            "pace": df_filter['pace'].tolist(),
            "cadence": df_filter['average cadence'].tolist(),
            "years": df_filter['year'].tolist()
        }
