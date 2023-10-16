# <ins> Pinterest Data Pipeline </ins>
[DESCRIPTION]

## Infrastructure
Firstly, I got my hands on some infrastructure similar to that which I would be working with were I a data engineer working at Pinterest.

Inside the file given to me by AiCore, I found user_posting_emulation.py, that contains the login credentials for a RDS database, which contains three tables with data resembling data received by the Pinterest API when a POST request is made by a user uploading data to Pinterest:
- pinterest_data contains data about posts being updated to Pinterest
- geolocation_data contains data about the geolocation of each Pinterest post found in pinterest_data
- user_data contains data about the user that has uploaded each post found in pinterest_data
You can run the provided script and print out pin_result, geo_result and user_result to get familiar with the data the same way I did.

<br>

## Connecting to the EC2 Client
To start off, I signed into the AWS console
<br>
  
![smallerboi](https://github.com/Mat-Zawadzki/pinterest-data-pipeline/assets/114954374/836785d0-28de-483e-9e35-c8c597a0ce62)


I then created a key pair file locally to allow me to connect to my EC2 instance. Using the KeyPairId received in the zip folder, I found the specific key pair associated to my EC2 instance. In the parameter store section on my AWS account, under the "Value" field I selected "show" to copy the content of key pair (including the BEGIN and END header) and pasted it in the .pem file in VSCode..
<br>


![editedout1](https://github.com/Mat-Zawadzki/pinterest-data-pipeline/assets/114954374/47f4644d-f3ee-4df6-8b1a-685b12798816)
![editedboi3](https://github.com/Mat-Zawadzki/pinterest-data-pipeline/assets/114954374/35ade65e-db89-4975-930f-1615b7821fe9)


Navigate to the EC2 console and identify the instance with your unique UserId.Select this instance, and under the Details section find the Key pair name and make a note of this. Save the previously created file in the VSCode using the following format: Key pair name.pem.
