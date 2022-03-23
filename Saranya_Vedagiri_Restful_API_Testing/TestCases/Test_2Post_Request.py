import requests
import json
import jsonpath

url="https://gorest.co.in/public-api/users"
access_token='Bearer 350740b9bae50aeca39557a9ec9f7714bedda425e4b36912d7484179148ccb50'
file_read=open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\post_value.json",'r')
json_input=file_read.read()
request_json=json.loads(json_input)
response=requests.post(url,request_json,headers={'Authorization':access_token})
json_response=json.loads(response.text)

def test_post_request_successfully_created():

    code=jsonpath.jsonpath(json_response,'code')
    assert code[0]==201
    print(" A resource was successfully created in response to a POST request. The Location header contains the URL pointing to the newly created resource.")


def test_for_authentication_failure():
    url = "https://gorest.co.in/public-api/users"
    access_token = 'Bearer 350740b9bae50aeca39557aec9f7714bedda425e4b36912d7484179148ccb50'
    file_read = open("C:\\Users\\karan\\Desktop\\QA\\RestFull_Python\\post_value.json", 'r')
    json_input = file_read.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json, headers={'Authorization': access_token})
    json_response = json.loads(response.text)
    code = jsonpath.jsonpath(json_response, 'code')
    print(code)
    assert code[0]==401
    print("Authentication failed:Status code for wrong Authentication is matches successfully ")

def test_post_response_validation():
    name=jsonpath.jsonpath(json_response,'data.name')
    name1=name[0]
    if name1 in json_input:
        print("Post request and Response data Matching Successfully")
    else:
        print("Data Not Matching")
