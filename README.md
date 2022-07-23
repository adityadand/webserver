# webserver
flask webserver fully capable of remote controlling device script is running on

# to run with ngrok ( remote controlled)
simply add ur account ngrok credintials in ur own system
then just run "python webserve.py"

# to run without ngrok
remove "run_with_ngrok(app)" statement and other ngrok imports if required
then run by
> set FLASK_APP=webserve.py

> python -m flask run


# to use volume feature you need to install setvol tool
https://rlatour.com/setvol/

# using features
![180612950-046bc86e-7332-4484-8ea5-c2beac8b3c6c](https://user-images.githubusercontent.com/33375699/180612988-79a3dd12-8ecc-4a02-a0d4-fdafaac50f00.png)
