# Pinterest Data Pipeline
[DESCRIPTION]

## <ins> Infrastructure </ins>
<br>
Firstly, I got my hands on some infrastructure similar to that which I would be working with were I a data engineer working at Pinterest.

Inside I found user_posting_emulation.py, that contains the login credentials for a RDS database, which contains three tables with data resembling data received by the Pinterest API when a POST request is made by a user uploading data to Pinterest:
- pinterest_data contains data about posts being updated to Pinterest
- geolocation_data contains data about the geolocation of each Pinterest post found in pinterest_data
- user_data contains data about the user that has uploaded each post found in pinterest_data
You can run the provided script and print out pin_result, geo_result and user_result to get familiar with the data the same way I did.

<br>

## <ins> Connecting to the EC2 Client </ins> <br>

![Screenshot 2023-10-16 144027](https://github.com/Mat-Zawadzki/pinterest-data-pipeline/assets/114954374/a9ab614d-279f-4623-82f3-f6fc56c63b4b)


Created a key pair file locally to allow me to connect to my EC2 instance. Found the specific key pair associated to my EC2 instance, in the parameter store section on my AWS account, and under the "Value" field selected "show".
![editedout1](https://github.com/Mat-Zawadzki/pinterest-data-pipeline/assets/114954374/47f4644d-f3ee-4df6-8b1a-685b12798816)


Navigate to the EC2 console and identify the instance with your unique UserId.Select this instance, and under the Details section find the Key pair name and make a note of this. Save the previously created file in the VSCode using the following format: Key pair name.pem.
