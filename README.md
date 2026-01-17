# Student Performance Prediction App

This project is a web application that predicts student performance using a machine learning model. It uses Streamlit for the user interface and a linear regression model trained on student data.

## Project Structure

- `Dockerfile`: Docker configuration to containerize the application.
- `app/`: Main application directory.
  - `interface.py`: Streamlit web application code.
  - `projet.ipynb`: Jupyter notebook for model training and data analysis.
  - `performance_model.pkl`: Trained linear regression model (pickle file).
  - `requirements.txt`: Python dependencies.

## Features

- Interactive web interface to input student data.
- Predicts performance index based on:
  - Hours Studied
  - Previous Scores
  - Extracurricular Activities
  - Sleep Hours
  - Sample Question Papers Practiced
- Displays predicted performance with a dialog box.

## Prerequisites

- Python 3.9 or higher
- Docker (for containerized deployment)

## Local Setup

1. Clone or download the project.
2. Navigate to the project directory.
3. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app/interface.py
   ```
5. Open your browser to `http://localhost:8501`.

## Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t student-performance-app .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 student-performance-app
   ```
3. Access the app at `http://localhost:8501`.

## Model Training

The model is trained using the `projet.ipynb` notebook:

1. Downloads the "Student Performance" dataset from Kaggle.
2. Preprocesses the data (encodes categorical variables).
3. Trains a linear regression model.
4. Evaluates the model using mean squared error.
5. Saves the model as `performance_model.pkl`.

To retrain the model, run the notebook cells in order.

## Dependencies

- streamlit: For the web interface.
- scikit-learn: For the machine learning model.
- numpy: For numerical operations.
- pandas: Used in the notebook for data manipulation.
- kagglehub: For downloading the dataset in the notebook.

## Health Check

The Docker container includes a health check that verifies the Streamlit app is running by checking `http://localhost:8501/_stcore/health`.

## Notes

- The model assumes input values are within reasonable ranges (e.g., hours studied 1-10, scores 0-100).
- The app loads an image from Unsplash for display.
- Ensure internet access for the image and (if retraining) dataset download.
