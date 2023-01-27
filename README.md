# Migrate Brightcove Videos to AWS S3 using Python
This script demonstrates how to migrate videos from Brightcove to AWS S3 using Python.

## Prerequisites
- A Brightcove account and API credentials (Account ID, Client ID, and Client Secret)
- An AWS account and S3 credentials (Access Key and Secret Key)
- A bucket on S3 to store the videos
- Python 3 installed on your system
## Libraries used
- requests for interacting with the Brightcove API
- boto3 for interacting with AWS S3
## Usage
1. Replace the placeholder values for your Brightcove and AWS credentials in the script.
2. Run the script:
```
python3 brightcove_to_aws_migration.py
```
3. The script will retrieve the list of videos from Brightcove, download them and then upload to the specified S3 bucket.

# Note
This is a simple script, for a real-world implementation, you may need to add error handling, logging, retries and may need to handle pagination of the data returned by the API.

# Disclaimer
This script is for demonstration purposes only and should not be used in production without proper testing and modification to fit your use case.

# Author
Elton Dcunha

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# Acknowledgments
- [Brightcove API documentation](https://studio.support.brightcove.com/media/manage/downloading-videos-video-cloud.html).
- [AWS S3 documentation](https://aws.amazon.com/s3/).

This script uses the requests library to interact with the Brightcove API and the boto3 library to interact with AWS S3. It first gets an access token from Brightcove using the client credentials, then it retrieves a list of videos from the Brightcove API, and finally, it iterates through each video and uploads it to the specified S3 bucket.

You should use a README file to provide documentation and usage instructions for your code. This will help others understand what your code does, how to use it, and how to contribute to it. The README should also include information about any dependencies or requirements, as well as any relevant licenses or disclaimers.
