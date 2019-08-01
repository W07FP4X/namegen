# NameGen
A unique name generator written in Python.  
## Prerequisites
* Python 3
* PIP 3
## Build
docker build -t namegen_service .
## Run
docker run --name=namegen_service -d --restart=always -p 7777:7777 -t namegen_service
## API Endpoints

*Endpoint requires no authentication.

### Get unique names:

Get unique human and machine readable names.

**URL** : `/names/<count>`

**URL Parameters** : `count=[integer]` where `/names/<count>` is the number (1-1000) of unique names to return.

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Content example:**

For the following curl request with a "count" of 3 provided: "curl --request GET http://127.0.0.1:7777/names/3"


```json
{
    [
    "Oscar_Lima_TJ6XBMTB",
    "Hotel_Quebec_7L5CRQ4P",
    "X-ray_Mike_3LBL6CGJ",
    ]
}
```
## Customize the names
-modify the list of names
## Run the tests:
* pip install pytest
* pip install tavern
* pip install tavern[pytest]
## TODO
* TLS
* AuthN/AuthZ
