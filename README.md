## API autotests project
### Based on Python/PyTest/Requests + Allure for reporting
#### The project consists of:
##### data.py - constants, input data
##### conftest.py - fixtures
##### requests_petstore.py - REST API methods
##### tests_petstore.py - tests
__________________________________
##### Requirements for Allure: 
###### JAVA JDK
###### SCOOP (you could use this feature for a fast installing Allure)
###### Allure (for Allure installation please use this command: "scoop install allure")
__________________________________
###### 1) For running tests use the command: "pytest -s -v tests_petstore.py --alluredir=allureresults"
###### 2) Then use the command: "allure serve allureresults"  for generating html report via Allure
###### pay attention please: you should use all commands without quotion marks ;)
![AllurePic](https://user-images.githubusercontent.com/84810149/221435064-d1fd9ef0-5547-47de-bc02-e7dd9d89db97.jpg)
