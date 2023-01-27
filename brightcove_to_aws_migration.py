import boto3
import requests

# Brightcove API credentials
brightcove_account_id = 'your_account_id'
brightcove_client_id = 'your_client_id'
brightcove_client_secret = 'your_client_secret'

# AWS S3 credentials
aws_access_key = 'your_access_key'
aws_secret_key = 'your_secret_key'
aws_bucket_name = 'your_bucket_name'

# Brightcove API endpoint
brightcove_api_url = 'https://cms.api.brightcove.com/v1/accounts/{}/videos'.format(brightcove_account_id)

# Get access token from Brightcove
response = requests.post('https://oauth.brightcove.com/v4/access_token',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         data={'grant_type': 'client_credentials',
                               'client_id': brightcove_client_id,
                               'client_secret': brightcove_client_secret})
access_token = response.json()['access_token']

# Get list of videos from Brightcove
response = requests.get(brightcove_api_url,
                        headers={'Authorization': 'Bearer ' + access_token,
                                 'Content-Type': 'application/json'})
videos = response.json()['items']

# Connect to S3
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Iterate through each video and upload to S3
for video in videos:
    video_id = video['id']
    video_url = video['sources'][0]['src']
    video_filename = '{}.mp4'.format(video_id)

    # Download video from Brightcove
    response = requests.get(video_url)

    # Upload video to S3
    s3.upload_fileobj(response.raw, aws_bucket_name, video_filename)

    print('Video {} uploaded to S3 as {}'.format(video_id, video_filename))
