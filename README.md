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

## <ins> Connecting to the EC2 Client </ins>
![Screenshot 2023-10-16 144027](https://github.com/Mat-Zawadzki/pinterest-data-pipeline/assets/114954374/a9ab614d-279f-4623-82f3-f6fc56c63b4b)
