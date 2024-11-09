import yaml
from pathlib import Path

def load_config(config_path: str | Path = "../../config.yaml") -> dict:
    """Load YAML config file into a dictionary.
    
    Args:
        config_path: Path to the YAML config file
        
    Returns:
        Dictionary containing the configuration
    """
    with open(config_path) as f:
        return yaml.safe_load(f)

config = load_config()
