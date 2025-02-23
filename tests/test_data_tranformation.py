import pytest
import os
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.entity import DataTransformationConfig
from datasets import DatasetDict, Dataset

@pytest.fixture
def data_transformation_config():
    config_manager = ConfigurationManager()
    return config_manager.get_data_transformation_config()

@pytest.fixture
def data_transformation(data_transformation_config):
    return DataTransformation(config=data_transformation_config)

def test_convert_examples_to_features(data_transformation):
    example_batch = {
        'dialogue': ["Hello, how are you?", "I'm fine, thank you!"],
        'summary': ["Greeting exchange.", "Response."]
    }
    features = data_transformation.convert_examples_to_features(example_batch)
    assert 'input_ids' in features
    assert 'attention_mask' in features
    assert 'labels' in features

def test_convert(data_transformation, tmp_path):
    # Create a dummy dataset
    dummy_data = DatasetDict({
        'train': Dataset.from_dict({
            'dialogue': ["Hello, how are you?", "I'm fine, thank you!"],
            'summary': ["Greeting exchange.", "Response."]
        })
    })
    dummy_data.save_to_disk(tmp_path / "samsum_dataset")

    # Update config to use the dummy dataset path
    data_transformation.config.data_path = tmp_path / "samsum_dataset"
    data_transformation.config.root_dir = tmp_path / "data_transformation"

    data_transformation.convert()
    assert os.path.exists(data_transformation.config.root_dir / "samsum_dataset")
    assert len(os.listdir(data_transformation.config.root_dir / "samsum_dataset")) > 0