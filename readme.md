#Gmail Email Cleanup API
###Summary
This application is desigend to collect all of the header information for a gmail email and then store the information into a dynamodb table.
The system works in an entirerty and requires the email to be added to the developer console for gmail. The application is kept in developer status with Google during this time which is why that must be added first.


###Environment Variables
email = email that is being imported / processed

###Requirements
You also need to build out a credentials.json file which comes from Google to be able to connect to the API.