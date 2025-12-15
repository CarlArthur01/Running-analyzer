"""
Pydantic Schemas for Request/Response Validation
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ActivityBase(BaseModel):
    """Base schema for running activity"""
    activity_id: int
    activity_date: datetime
    distance: float = Field(..., description="Distance in kilometers")
    duration: float = Field(..., description="Duration in minutes")
    pace: Optional[float] = Field(None, description="Pace in min/km")
    average_heart_rate: Optional[float] = None
    max_heart_rate: Optional[float] = None
    elevation_gain: Optional[float] = None
    elevation_loss: Optional[float] = None
    calories: Optional[float] = None

class PredictionRequest(BaseModel):
    """Request schema for race time prediction"""
    avg_weekly_distance: float = Field(..., description="Average weekly distance in km")
    avg_pace: float = Field(..., description="Average pace in min/km")
    avg_heart_rate: Optional[float] = None
    recent_long_run: Optional[float] = None
    weeks_of_training: Optional[int] = None

class PredictionResponse(BaseModel):
    """Response schema for race time prediction"""
    predictions: dict = Field(..., description="Predicted times for different distances")
    confidence: float = Field(..., description="Model confidence score")
    recommendations: Optional[List[str]] = None

class StatsResponse(BaseModel):
    """Response schema for overall statistics"""
    total_runs: int
    total_distance_km: float
    average_pace_min_per_km: float
    total_elevation_gain_m: float
    fastest_5k: Optional[str] = None
    fastest_10k: Optional[str] = None
