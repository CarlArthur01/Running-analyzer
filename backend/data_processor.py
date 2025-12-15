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
        """
        Initialize data processor
        
        Args:
            data_path: Path to processed data file
        """
        self.data_path = Path(data_path)
        self.df = None
        
    def load_data(self) -> pd.DataFrame:
        """Load processed data"""
        if self.data_path.exists():
            self.df = pd.read_csv(self.data_path)
            return self.df
        else:
            raise FileNotFoundError(f"Data file not found: {self.data_path}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Calculate overall statistics"""
        if self.df is None:
            self.load_data()
        
        stats = {
            "total_runs": len(self.df),
            "total_distance_km": self.df['distance'].sum(),
            "average_pace_min_per_km": self.df['pace'].mean(),
            "total_elevation_gain_m": self.df['elevation_gain'].sum(),
        }
        
        return stats
    
    def get_activities(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get list of activities"""
        if self.df is None:
            self.load_data()
        
        return self.df.head(limit).to_dict('records')
    
    def get_pace_data(self) -> Dict[str, List]:
        """Get pace progression data for charts"""
        if self.df is None:
            self.load_data()
        
        # Sort by date
        df_sorted = self.df.sort_values('activity_date')
        
        return {
            "dates": df_sorted['activity_date'].tolist(),
            "pace": df_sorted['pace'].tolist()
        }
    
    def get_volume_data(self) -> Dict[str, List]:
        """Get training volume data"""
        if self.df is None:
            self.load_data()
        
        # Group by week
        self.df['week'] = pd.to_datetime(self.df['activity_date']).dt.isocalendar().week
        weekly = self.df.groupby('week')['distance'].sum()
        
        return {
            "weeks": weekly.index.tolist(),
            "distance": weekly.values.tolist()
        }
