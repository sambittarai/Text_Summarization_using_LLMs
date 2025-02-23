# Text Summarization Using LLMs and Hugging Face

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
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the configuration files (config/config.yaml and params.yaml) with your desired parameters.
	

## **Usage**

### Training the Model

To train the summarization model, run:

   ```bash
   python main.py
   ```

### Running the API

To start the API for training and prediction:

   ```bash
   python app.py
   ```

### Batch Prediction

For batch prediction, use the provided API endpoint:

   ```bash
   curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "Your input text here"}'
   ```

## **Workflow Overview**

The project follows a modular workflow:

- **Data Ingestion:** Load and preprocess the dataset.
- **Data Transformation:** Tokenize and prepare the data for training.
- **Model Training:** Fine-tune the pre-trained Pegasus model on the dataset.
- **Prediction Pipeline:** Generate summaries for new input text.
- **API Integration:** Expose training and prediction functionalities via RESTful APIs.

## **Dataset and Model**

- **Dataset: Samsung/samsum -** A conversational summarization dataset.
- **Model: Pegasus-cnn_dailymail -** A pre-trained model for abstractive summarization.

## **Configuration**

The project uses two configuration files:

- config/config.yaml: Contains paths, model settings, and training parameters.
- params.yaml: Defines hyperparameters for training and evaluation.

- Example config.yaml:

   ```bash
data_path: "artifacts/data"
model_ckpt: "google/pegasus-cnn_dailymail"
root_dir: "artifacts/model_trainer"
   ```

- Example params.yaml:

   ```bash
TrainingArguments:
  num_train_epochs: 10
  warmup_steps: 500
  per_device_train_batch_size: 1
  weight_decay: 0.01
  logging_steps: 10
  evaluation_strategy: steps
  eval_steps: 500
  save_steps: 1000000
  gradient_accumulation_steps: 16
  ```

## **API Endpoints**

### Training API

- **Endpoint:** POST /train

- **Description:** Starts the model training process.

- **Example:**

   ```bash
curl -X POST http://localhost:5000/train
   ```

### Prediction API

- **Endpoint:** POST /train

- **Description:** Generates a summary for the input text.

- **Example:**

   ```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "Your input text here"}'
   ```

