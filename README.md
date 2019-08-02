# NameGen 🎲

A unique name generator written in Python.  
## Prerequisites
* Python 3
* PIP 3
## Build
    docker build -t namegen_service .
## Run
    docker run --name=namegen_service -d --restart=always -p 7777:7777 -t namegen_service
## API Endpoints 
ℹ︎ *Endpoints require no authentication.*

### Get unique names:

Get unique human and machine readable names.

**URL** : `/names/<count>`

**URL Parameters** : `count=[integer]` where `/names/<count>` is the number (1-1000) of unique names to return.

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

### Success Response

**Code** : `200 OK`

**Example:**

Request:

    curl --request GET http://127.0.0.1:7777/names/3

Result:

```
{
    [
    "Oscar_Lima_TJ6XBMTB",
    "Hotel_Quebec_7L5CRQ4P",
    "X-ray_Mike_3LBL6CGJ",
    ]
}
```
## Customize the names
Modify ./data/names.txt to provide your own list of custom names:
```
Alfa
Bravo
Charlie
Delta
...
```

## Run the tests:
* `pip install tavern`
* `pip install tavern[pytest]`
* Run and build the service.
* `py.test ./tests/test_api.tavern.yaml  -v`
## TODO
* TLS
* AuthN
* AuthZ
