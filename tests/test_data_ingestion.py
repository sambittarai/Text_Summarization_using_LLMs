import pytest
import os
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.entity import DataIngestionConfig

@pytest.fixture
def data_ingestion_config():
    config_manager = ConfigurationManager()
    return config_manager.get_data_ingestion_config()

@pytest.fixture
def data_ingestion(data_ingestion_config):
    return DataIngestion(config=data_ingestion_config)

def test_download_file(data_ingestion):
    data_ingestion.downlaod_file()
    assert os.path.exists(data_ingestion.config.local_data_file)

def test_extract_zip_file(data_ingestion):
    data_ingestion.downlaod_file()
    data_ingestion.extract_zip_file()
    assert os.path.exists(data_ingestion.config.unzip_dir)
    assert len(os.listdir(data_ingestion.config.unzip_dir)) > 0