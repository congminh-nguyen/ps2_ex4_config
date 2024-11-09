from pydantic import BaseModel, Field
from typing import List, Optional
from pathlib import Path

class GameData(BaseModel):
    """Data model for NBA game data."""
    season_id: int = Field(..., description="Season identifier")
    game_id: Optional[str] = Field(None, description="Unique game identifier")
    game_date: Optional[str] = Field(None, description="Date of the game")
    team_id_home: Optional[int] = Field(None, description="Home team identifier")
    team_id_away: Optional[int] = Field(None, description="Away team identifier") 
    pts_home: Optional[int] = Field(None, description="Points scored by home team")
    pts_away: Optional[int] = Field(None, description="Points scored by away team")

    class Config:
        validate_assignment = True

class ModelConfig(BaseModel):
    """Data model for model configuration."""
    name: str = Field(..., description="Name of the model")
    type: str = Field(..., description="Type of model (e.g. classification)")
    params: dict = Field(..., description="Model parameters")

    class Config:
        validate_assignment = True

class DataConfig(BaseModel):
    """Data model for data configuration."""
    table: str = Field(..., description="Name of the data table")
    data_path: str = Field(..., description="Path to data file")
    features_columns: List[str] = Field(..., description="List of feature column names")

    class Config:
        validate_assignment = True

class Config(BaseModel):
    """Overall configuration data model."""
    data: DataConfig = Field(..., description="Data configuration")
    model: ModelConfig = Field(..., description="Model configuration")

    class Config:
        validate_assignment = True
