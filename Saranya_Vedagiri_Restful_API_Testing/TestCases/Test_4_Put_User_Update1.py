import requests
import json
import jsonpath

# URL to Fetch the data from the server


file_read = open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\userid.txt", 'r')
user_id1 = file_read.read()
user_id=(int(user_id1))

url=f"https://gorest.co.in/public-api/users/{user_id}"


#url="https://gorest.co.in/public-api/users/3082"
access_token='Bearer 350740b9bae50aeca39557a9ec9f7714bedda425e4b36912d7484179148ccb50'

file_read=open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\put_value.json",'r')
json_input=file_read.read()
request_json=json.loads(json_input)

response=requests.put(url,request_json,headers={'Authorization':access_token})

json_response=json.loads(response.text)
print(response.content)
code=jsonpath.jsonpath(json_response,'code')
name=jsonpath.jsonpath(json_response,'data.name')

response1=requests.get("https://gorest.co.in/public-api/users/3073")
json_response1=json.loads(response1.text)
print(response1.content)



def test_to_get_user_details():
    assert response.status_code==200
    print("Status code 200 for PUT successfully matches")



def test_to_compare_code_response():
    assert code[0]==200
    print("Response code for PUT is successfully Matches from Response Body")
def test_to_check_updated_response_name():
    if name[0] in json_input:
        print("Succesfully updated the name value")
    else:
        print("Updation not successful")
