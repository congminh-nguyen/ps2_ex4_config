import pandas as pd
from pathlib import Path

class DataLoader:
    """A class to handle loading CSV data files from a specified directory."""
    
    def __init__(self, data_dir: str | Path) -> None:
        """Initialize the DataLoader with a data directory path.
        
        Args:
            data_dir: Path to the directory containing data files, as string or 
                Path
            
        Raises:
            NotADirectoryError: If the specified directory does not exist
        """
        self.data_dir = Path(data_dir).resolve()
        if not self.data_dir.is_dir():
            raise NotADirectoryError(
                f"Data directory not found: {self.data_dir}"
            )

    def load_csv(self, filename: str | Path) -> pd.DataFrame:
        """Load a CSV file from the data directory into a pandas DataFrame.
        
        Args:
            filename: Name of the CSV file to load, as string or Path
            
        Returns:
            pd.DataFrame containing the CSV data
            
        Raises:
            FileNotFoundError: If the specified file does not exist
            IsADirectoryError: If the path exists but is not a file
            ValueError: If the file does not have a .csv extension
        """
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
    loader = DataLoader("data")
    df = loader.load_csv("game.csv")
    print(f"Loaded data from: {df}")
