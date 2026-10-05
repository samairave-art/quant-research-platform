from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# Main directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
UNIVERSE_DIR = DATA_DIR / "universe"

RESEARCH_DIR = PROJECT_ROOT / "research"
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"


# Research defaults
DEFAULT_BENCHMARK = "SPY"
DEFAULT_START_DATE = "2015-01-01"
DEFAULT_INITIAL_CAPITAL = 1_000_000.0


# Trading assumptions
DEFAULT_TRANSACTION_COST_BPS = 10.0
DEFAULT_SLIPPAGE_BPS = 5.0


# Project metadata
PROJECT_NAME = "Quantitative Research & Algorithmic Trading Platform"
PROJECT_VERSION = "0.1.0"