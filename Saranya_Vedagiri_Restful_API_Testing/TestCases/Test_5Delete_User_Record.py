import requests
import json
import jsonpath

# URL to Fetch the data from the server


file_read = open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\userid.txt", 'r')
user_id1 = file_read.read()
user_id=(int(user_id1))

url=f"https://gorest.co.in/public-api/users/{user_id}"



res=requests.get(url)
print(res.content)
access_token='Bearer 350740b9bae50aeca39557a9ec9f7714bedda425e4b36912d7484179148ccb50'
response=requests.delete(url,headers={'Authorization':access_token})

print(response.status_code)
print(response.content)

json_response=json.loads(response.text)
code=jsonpath.jsonpath(json_response,'code')

print(code[0])



def test_to_compare_code_response():

    assert code[0]==204
    print(" The request was handled successfully and the response contains no body content (like a DELETE request)")

def test_to_check_deletion():
    url = "https://gorest.co.in/public-api/users/3102"
    access_token = 'Bearer 350740b9bae50aeca39557a9ec9f7714bedda425e4b36912d7484179148ccb50'
    response = requests.delete(url, headers={'Authorization': access_token})

    print(response.status_code)
    print(response.content)

    json_response = json.loads(response.text)
    code = jsonpath.jsonpath(json_response, 'code')

    assert code[0] ==404
    print("Successfully Deleted")


