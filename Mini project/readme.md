# PeopleCare

## Problem Description

PeopleCare is an Insurance company that provides Health Insurance to its customers. They have successfully moved up the market ladder and become popular within a span of a few years. Now the company has decided to expand its insurance to vehicles as well. They want to optimize their cost of reaching out to customers by only focusing on customers who have a higher likelihood of purchasing the vehicle policy.

Now, in order to predict whether a customer would be interested in Vehicle insurance, PeopleCare has conducted a public survey and collected information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel) etc. They have hired you as a data scientist to build a model to predict whether these potential customers would be interested in opting for a Vehicle Insurance from PeopleCare. They will only use this strategy if you are able to create a model which is atleast 75% accurate.

| **Variable** | **Definition** |
| --- | --- |
| id | Unique ID for the customer |
| Gender | Gender of the customer |
| Age | Age of the customer |
| Driving\_License | 0 : Customer does not have DL, 1 : Customer already has DL |
| Region\_Code | Unique code for the region of the customer |
| Previously\_Insured | 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance |
| Vehicle\_Age | Age of the Vehicle  |
| Vehicle\_Damage | 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past. |
| Annual\_Premium | The amount customer needs to pay as premium in the year |
| Policy\_Sales\_Channel | Anonymised Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc. |
| Vintage | Number of Days, Customer has been associated with the company |
| Response | 1 :  Customer is interested, 0 : Customer is not interested |

## Installation Steps
Install Pipenv:

If you don't have Pipenv installed, you can install it using pip inside the project directory:
``````
pip install pipenv
```````

### Initialize a Pipenv Environment:

Run the following command in your project directory to create a new Pipenv environment and a Pipfile:

``````
pipenv --python 3.11  # Replace 3.11 with your preferred Python version
``````
### Install Dependencies from requirements.txt:

If you have a requirements.txt file containing a list of dependencies, you can install them all at once. Make sure the requirements.txt file is in your project directory. Run:
``````
pipenv install -r requirements.txt
``````

### Activate the Pipenv Environment:

To activate the Pipenv environment, use the following command:
``````
pipenv shell
``````

## Run the Waitress Server:

To serve your Flask application, you need to run Waitress from the command line. Use the following command:

``````
waitress-serve --host=0.0.0.0 --port=9696 predict:app
``````
--host=0.0.0.0: This option makes your Flask app accessible from any network interface.
--port=9696: This is the port number on which your app will be accessible. You can change it to your desired port.
predict:app: Replace the predict with your Flask application's Python file name (without the .py extension), and the second app with your Flask app variable name (usually app by default).

### Access Your Flask Application:

Your Flask application is now running, and you can access it in your web browser by visiting:

``````
http://your_server_ip:9696
``````
Replace your_server_ip with the IP address or hostname of your server.

## Building the Docker Image

### Build the Docker Image:

Use the following command to build a Docker image for the PeopleCare prediction service. The -t flag assigns a name and optionally a tag to the image. The . at the end indicates the build context is the current directory:

``````
docker build -t peoplecare-prediction .
``````
This command will create a Docker image named peoplecare-prediction.

## Running the Docker Container

### Run the Docker Container:

To run the PeopleCare prediction service as a Docker container, you can use the following command. The -p flag maps the host port 9696 to the container port 9696:

``````
docker run -p 9696:9696 peoplecare-prediction:latest
``````
peoplecare-prediction:latest is the name and tag of the Docker image you built earlier.
The PeopleCare prediction service will now be running inside a Docker container.


This README description instructs the reader to run the `prediction_instance.ipynb` file after running the Docker container to test the PeopleCare prediction service with sample data and view the results.
