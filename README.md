# Text Summarization Using LLMs and Hugging Face

Dataset: https://huggingface.co/datasets/Samsung/samsum
Transformer: https://huggingface.co/google/pegasus-cnn_dailymail

This project is an end-to-end text summarization pipeline using **Large Language Models (LLMs)** and the **Hugging Face Transformers library**. It provides a streamlined workflow for training and deploying summarization models, with support for custom datasets and configurations.

---

## **Key Features**

- **Pre-trained Models**: Utilizes state-of-the-art models like **Pegasus** from Hugging Face for text summarization.
- **Customizable Pipeline**: Supports data ingestion, transformation, model training, and prediction.
- **API Integration**: Provides RESTful APIs for training and batch prediction.
- **Scalable**: Designed to handle large datasets and can be extended for other NLP tasks.

---

## **Installation**

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-summarizer.git
   cd text-summarizer

2. Install the required dependencies:
    pip install -r requirements.txt

3. Set up the configuration files (config/config.yaml and params.yaml) with your desired parameters.