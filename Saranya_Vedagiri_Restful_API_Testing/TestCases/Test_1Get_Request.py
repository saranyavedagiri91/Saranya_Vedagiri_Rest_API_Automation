import pytest
import requests
import json
import jsonpath

url="https://gorest.co.in/public-api/users"
response=requests.get(url)
content=response.content
header=response.headers
print(content)
def test_response_status_check():
    assert response.status_code ==200
    print("Status code 200 for get successfully matches")
def test_date_and_time():
    if ('2022' in header.get('Date')):
        print("Date Validation is Passed")
    else:
        print("Date Validation is Failed")

def test_response_content():
    print(header.get('Content-Type'))
    print(header.get('Content-Encoding'))
    print(response.cookies)
    print(response.elapsed)
    print(response.encoding)

json_response=json.loads(response.text)

def test_Number_Pages_Information():

    pages=jsonpath.jsonpath(json_response,'meta.pagination.pages')
    print("Number of Pages:",pages)

def test_Limit_Fix_per_Page_Is_20():

    limit=jsonpath.jsonpath(json_response,'meta.pagination.limit')
    print("Number of records per Page:",limit)
    print(limit)
    assert limit[0]==20
    print("Page limit 20 is successfully matches")

def test_to_check_page2():

    url2="https://gorest.co.in/public-api/users?page=2"
    response2=requests.get(url2)
    json_response2=json.loads(response2.text)

    print(response2.content)
    page2=jsonpath.jsonpath(json_response2,'meta.pagination.page')
    print(page2)
    assert page2[0]==2
    print("Url for page2 is viewed successfully")

def test_to_check_page_out_of_limit():

    url3="https://gorest.co.in/public-api/users/pages=2000"
    response3=requests.get(url3)
    json_response3=json.loads(response3.text)
    print(json_response3)
    code=jsonpath.jsonpath(json_response3,'code')
    message=jsonpath.jsonpath(json_response3,'data.message')
    print(message)
    assert code[0]==404
    print("The requested resource does not exist.Page not found 404 Error")
    assert message[0]=='Resource not found'
    print("Resource Not Found")











































