import requests
import json
import jsonpath

# URL to Fetch the data from the server

file_read = open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\userid.txt", 'r')
user_id1 = file_read.read()
user_id=(int(user_id1))
print(user_id)


url=f"https://gorest.co.in/public-api/users/{user_id}"


response=requests.get(url)
json_response=json.loads(response.text)
print(response.content)


open("filename", "w").close()
file=open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\getfile.json","w")
json_string=json.dumps(json_response)
file.write(json_string)
file.close()

file_read = open("C:\\Users\\karan\\PycharmProjects\\Saranya_Vedagiri_Restful_API_Testing\\Data\\getfile.json", 'r')
get_input = file_read.read()
print(get_input)
code=jsonpath.jsonpath(json_response,'code')
id=jsonpath.jsonpath(json_response,'data.id')
name=jsonpath.jsonpath(json_response,'data.name')
email=jsonpath.jsonpath(json_response,'data.email')


def test_to_get_user_details():
    assert response.status_code==200
    print("Status code successfully matches")







def test_to_write_user_details_infile():
    assert code[0]==200
    print("Status code successfully matches")

def test_to_check_response_details():
    if email[0] in get_input:
        print("Email Value is Correct")
    else:
        print("Wrong ID Value")