# Resume
We have at least 6 different types of data: email, phone
number, device, geolocation, and user data.
The challenge, if you accept it, is to design and prototype a simple API that
receives a request and enriches and aggregates the data in order to serve the
enriched data back to the user.
Data is as follows, 6 independent data sources with data ready to be enriched
based on different keys:
“email”, “phone_number”, “devices”, “geolocation”, “user_data”
When expecting a request we expect different keys that will be enriched
depending on the initial key

Propose an architecture to build the different services and logic from the API
Gateway to compile the response based on the requested data and matches with
the database. Propose it using API best practices, technology stack, proposed
data model and different endpoints, to get, upload, update and delete data from
the different services. Be sure to justify a low latency response.

# User story
### consultation service
We have at least 6 different types of data: email, phone
number, device, geolocation, and user data.
The challenge, if you accept it, is to design and prototype a simple API that
receives a request and enriches and aggregates the data in order to serve the
enriched data back to the user.
Data is as follows, 6 independent data sources with data ready to be enriched
based on different keys:
“email”, “phone_number”, “devices”, “geolocation”, “user_data”
Email data example:

Email data example:

| email | creation_date | email_status | email_score  | valid_email | fraud |

|  -- | -- | -- | -- | -- | -- | -- | -- | -- |

|  carl@trully.ai | 2020/06/01 | active | 910 | 1 | 0 |

| test@proton.mail | 2022/05/08 | active | 423 | 0 | 1 |

| osvaldo@gmail.com | 2020/02/01 | active | 950 | 0 | 0 |

| roberto@gmail.com | 2019/05/11 | active | 954 | 1 | 0 |

| ricardo@gmail.com | 2016/12/29 | active | 966 | 1 | 0 |

| fernando@gmail.com | 2017/04/13 | active | 913 | 1 | 0 |

| fraud@hotmail.com | 2022/08/12 | active | 450 | 0 | 1 |

| fraudster@proton.mail | 2022/08/14 | active | 310 |0 | 1 |


When expecting a request we expect different keys that will be enriched
depending on the initial key

Propose an architecture to build the different services and logic from the API
Gateway to compile the response based on the requested data and matches with
the database. Propose it using API best practices, technology stack, proposed
data model and different endpoints, to get, upload, update and delete data from
the different services. Be sure to justify a low latency response.


# Implementation

#### Clonar
 

    git clone https://github.com/raulespecialist/api_source.git
Enter in the directory

    cd api_source

Make a virtual env

    python -m venv .env 

Enter in the virtual env

    source .env/bin/activate

Inside the virtual environment (.env) update pip

    pip install --upgrade pip

Then install all the necessary requirements

    pip install -r requirements.txt

Start the API REST in port 8001

    python manage.py runserver 127.0.0.1:8001

This is the implementation of the first API that provides the data to the second API that works as a gateway.
[Link to second API (gateway)](https://github.com/raulespecialist/api_gateway)
