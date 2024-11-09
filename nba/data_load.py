import pandas as pd
from pathlib import Path
import config

class DataLoader:
    """A class to handle loading CSV data files from a specified directory."""
    
    def __init__(self, data_dir: str | Path = None) -> None:
        """Initialize the DataLoader with a data directory path.
        
        Args:
            data_dir: Path to the directory containing data files, as string or 
                Path. If None, uses the path from config.
            
        Raises:
            NotADirectoryError: If the specified directory does not exist
        """
        if data_dir is None:
            # Get the parent directory of the config.yaml file
            data_dir = Path(__file__).parent.parent / config['data']['data_path']
            
        self.data_dir = Path(data_dir).resolve()
        if not self.data_dir.is_dir():
            raise NotADirectoryError(
                f"Data directory not found: {self.data_dir}"
            )

    def load_csv(self, filename: str | Path = None) -> pd.DataFrame:
        """Load a CSV file from the data directory into a pandas DataFrame.
        
        Args:
            filename: Name of the CSV file to load, as string or Path.
                If None, uses the filename from config.
            
        Returns:
            pd.DataFrame containing the CSV data
            
        Raises:
            FileNotFoundError: If the specified file does not exist
            IsADirectoryError: If the path exists but is not a file
            ValueError: If the file does not have a .csv extension
        """
        if filename is None:
            filename = config['data']['data_path']
            
        file_path = (self.data_dir / filename).resolve()
        
        if not file_path.is_file():
            if not file_path.exists():
                raise FileNotFoundError(f"CSV file not found: {file_path}")
            raise IsADirectoryError(
                f"Path exists but is not a file: {file_path}"
            )
            
        if not file_path.name.lower().endswith('.csv'):
            raise ValueError(f"File must be a CSV file: {file_path}")
            
        return pd.read_csv(file_path)

if __name__ == "__main__":
    loader = DataLoader()
    df = loader.load_csv()
    print(f"Loaded DataFrame shape: {df.shape}")
