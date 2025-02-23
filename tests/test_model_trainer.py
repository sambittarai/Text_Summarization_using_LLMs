import pytest
import os
from pathlib import Path
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer.entity import ModelTrainerConfig
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # Import the necessary classes

@pytest.fixture
def model_trainer_config():
    config_manager = ConfigurationManager()
    return config_manager.get_model_trainer_config()

@pytest.fixture
def model_trainer(model_trainer_config):
    return ModelTrainer(config=model_trainer_config)

def test_model_initialization(model_trainer):
    assert isinstance(model_trainer.config, ModelTrainerConfig)
    assert model_trainer.config.model_ckpt == "google/pegasus-cnn_dailymail"

def test_train(model_trainer):
    # Ensure root_dir and data_path are Path objects
    model_trainer.config.root_dir = Path(model_trainer.config.root_dir)
    model_trainer.config.data_path = Path(model_trainer.config.data_path)

    # Use the actual data path
    model_trainer.train()

    # Check if the model and tokenizer are saved
    model_path = model_trainer.config.root_dir / "pegasus-samsum-model"
    tokenizer_path = model_trainer.config.root_dir / "tokenizer"
    assert model_path.exists()
    assert tokenizer_path.exists()

    # Validate the contents of the saved model and tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    assert model is not None
    assert tokenizer is not None

