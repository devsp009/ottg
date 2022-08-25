# Obey The Testing Goat - 21st August 2022

# Lesson 001 B
Create a standard test file and name it functional_tests.py

We will use firefox for this test
```
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest


class NewUserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver4FirefoxBrowser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def tearDown(self) -> None:
        self.driver4FirefoxBrowser.quit()

    def test_can_enter_two_numbers_and_get_sum(self):
        self.driver4FirefoxBrowser.get('http://localhost:8000')
        self.assertIn('Calculator',self.driver4FirefoxBrowser.title)
        self.fail('Complete the test')

if __name__ == '__main__'        :
    unittest.main()


```
Execute this file by keying in
```
python functional_tests.py
```

# Lesson 001
How to setup and run django project ?

First create a fresh branch
```
git checkout -b users/krk/20220821_create_django_project
```

In the virtual environment run the following command to create a new project with the name Calculator. Note the DOT at the end to create it in the current folder

```
django-admin startproject calculator .

```

Run the server in a separate terminal window.

Note by default the new terminal will open the virtual environment. If not please go ahead and activate the virtual env before running the following command to start the calculator project.

```
python manage.py runserver
```
Open any browser and visit http://localhost:8000 to find a default django project running.

Note: 127.0.0.1 and localhost are the same. Its your local machine.

# Branch first.. Basic Git commands

How to Clone? (get a fresh repository in local box)
```
git clone git@github.com:kanchiraghuraman/ottg.git
```

How to branch?

```
git checkout -b users/ini/20220821_prerequisites
```

Save changes
```
git add -A
git commit -am "Some context message"
```

Send changes to repository
```
git push --set-upstream origin users/ini/20220821_prerequisites
```


# Lesson 00: Prerequisites

Install python

mkdir /src/learning/YYYYMM

```
mkdir /src/learning/202208

mkdir /src/learning/202208/ottg

cd /src/learning/202208/ottg

git init

code .
```

# Setup python virtual environment

Ensure you are in the correct folder/directory.
Create Virtual Environment with name **venv**
```
python -m venv venv
```
Activate Virtual Environment
```
.\venv\Scripts\Activate.ps1
```
Note: if you see error text in red with message like Unauthorized access. You will have to follow this additional steps to allow running powershell scripts.

Error Message: .\venv\Scripts\Activate.ps1 : File C:\src\learning\202208\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.

```
<!-- Get-ExecutionPolicy -->
<!-- Get-ExecutionPolicy -List -->
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Deactivate Virtual Environment
```
<!-- .\venv\Scripts\deactivate.bat -->
deactivate

```

#Setup Python for Testing

In python virtual environment

```
python -m pip install --upgrade pip
pip install django
pip install selenium
pip install webdriver-manager
pip install chromedriver-binary
```

# EXAMPLE Test File

Reference: https://pypi.org/project/webdriver-manager/

Create a test file example4chrome01.py

```
# selenium 4 - Chrome
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver4ChromeBrowser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver4ChromeBrowser.get('http://www.google.com')
time.sleep(15) #seconds

assert 'Google' in driver4ChromeBrowser.title

driver4ChromeBrowser.close()

```

To run this file in venv terminal
```
python example4chrome01.py
```

# EXAMPLE Test File for EDGE example4edge01.py

```
# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver4EdgeBrowser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver4EdgeBrowser.get('https://microsoft.com')

time.sleep(15) #seconds

assert 'Microsoft' in driver4EdgeBrowser.title

driver4EdgeBrowser.close()

```