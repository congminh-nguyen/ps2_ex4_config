import yaml
from pathlib import Path

config = yaml.safe_load((Path(__file__).parent.parent / "config.yaml").read_text())
