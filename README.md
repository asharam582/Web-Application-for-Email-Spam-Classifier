# Email Spam Classifier Web Application

## Overview

This web application utilizes a pretrained email spam classifier model to predict whether an email is spam or not spam. Users can input email text through a simple user interface and receive the prediction.

## Project Setup

### Requirements

Ensure you have the following dependencies installed:

- Flask
- Gunicorn
- pickle-mixin
- scikit-learn

You can install them using:


bash pip install flask gunicorn pickle-mixin scikit-learn


## Local Development
### To run the application locally:

- Setup: The project is set up using GitHub and a Conda environment.
- Web Application: A simple web application is created using Flask.
- Model: The pretrained email spam classifier model and its requirements are integrated into the application.
- Deployment: The application is deployed to Render for public access.

## Usage
### Web Access
Access the application at https://email-spam-classifier-emsh.onrender.com.

## API Route
An API route allows programmatic access to the model prediction. The API endpoint accepts JSON data in the request body and returns the prediction as JSON response.

Example API request:

```json
{
    "email": "This is a sample email. Please classify it."
}
```

Example API response:


```json
{
    "prediction": "not spam",
    "email": "This is a sample email. Please classify it."
}
```


## Known Issues
InconsistentVersionWarning: There might be a version mismatch between the scikit-learn library used to train the model and the one being used in the current environment. This can lead to unexpected behavior or errors.

### Contributions

**Contributions to the project are welcome!** If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

