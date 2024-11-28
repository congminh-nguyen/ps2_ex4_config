from pydantic import BaseModel
from pathlib import Path

class PathsConfig(BaseModel):
    """Configuration class for paths used in the application.
    
    Attributes:
        data_dir: Path to the directory containing data files
    """
    data_dir: Path