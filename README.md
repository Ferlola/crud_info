This project gets from the user:
- The city and the country.
- The ip address.
- The operating system details.
- the CPU details.
- The hostname.
- The network name.
- The IP.
- The ip configuration.
- The date and time.
- The RAM percentaje.
- The RAM memory.



### 🔍 <span style="color: blue;">Requirements</span>:
--------------------------------------------------------
- virtual environment (highly recommended)

### 🚀 <span style="color: blue;">Installation</span>:
--------------------------------------------------------
- Create virtual environment.
```
$ python3 -m venv .venv
```

- Activate virtual environment.
```
$ source .venv/bin/activate
```

- Install requeriments.
```
(.venv) $ pip3 install -r requirements.txt
```
- Run the project.
```
(.venv) $ python3 manage.py makemigrations
(.venv) $ python3 manage.py migrate
(.venv) $ python3 manage.py runserver
```

- Open browser.

<pre><a href="http://localhost:8000">http://localhost:8000</a></pre>

