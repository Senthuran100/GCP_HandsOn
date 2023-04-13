from flask import jsonify
from geopy.geocoders import Nominatim
import requests
from google.cloud import storage
import json
storage_client = storage.Client(project='project-id') # Insert the project id

def create_bucket(dataset_name):
    """Creates a new bucket. https://cloud.google.com/storage/docs/ """
    print('function create_bucket called')
    bucket = storage_client.create_bucket(dataset_name)
    print('Bucket {} created'.format(bucket.name))

def delete_bucket(bucket_name):
    """Deletes a bucket. The bucket must be empty."""
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)

    bucket.delete()

    print("Bucket {} deleted".format(bucket.name))

def upload_blob(bucket_name, source_data, destination_blob_name):

    """Uploads a file to the bucket. https://cloud.google.com/storage/docs/ """
    print('function upload_blob called')

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(source_data)
    print('File {} uploaded to {}.'.format(
    destination_blob_name, bucket_name))

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket. https://cloud.google.com/storage/docs/"""
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)

def weather(request):
    data = {"success": False}
    #https://pypi.org/project/geopy/
    geolocator = Nominatim(user_agent="mlops-jsj")
    # params = request.get_json()
    for i in ["Orlando", "Chicago", "Texas"]:
        location = geolocator.geocode(i)
        # https://www.weather.gov/documentation/services-web-api
        result1 = requests.get(f"https://api.weather.gov/points/{location.latitude},{location.longitude}")
        # Example query: https://api.weather.gov/gridpoints/TOP/31,80
        result2 = requests.get(f"{result1.json()['properties']['forecast']}")
        data["response"] = result2.json()
        data["success"] = True
        bucket_name = 'weather_test_2023'
        # delete_bucket(bucket_name)
        # create_bucket(bucket_name)
        # jsonified_data = jsonify(data["response"])
        local_data = json.dumps(data["response"])
        file_name = 'data '+str(i)
        upload_blob(bucket_name, local_data, file_name)
        print('Data inside of ',bucket_name,':')
        # list_blobs(bucket_name)
    return list_blobs(bucket_name)