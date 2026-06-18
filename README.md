# Getting Remote Data Lab

This repository contains the solution for the **Retrieving Remote Data from an API** lab. It implements a generic Python class, `GetRequester`, designed to perform HTTP GET requests to a remote endpoint and deserialize JSON response payloads.

## Features

- **Generic HTTP GET Client:** Can be initialized with any target URL.
- **Raw Response Body Retrieval:** Fetches and returns raw byte content via `get_response_body()`.
- **JSON Deserialization:** Resolves and decodes the response payload into standard Python data structures (lists, dictionaries, etc.) using `load_json()`.

## API Documentation

### `GetRequester` Class

Located in [GetRequester.py](file:///c:/Users/flatironuser20/Desktop/PyAssignments/Py-API-Development/PyRemoteDatafromAPI/lib/GetRequester.py).

#### `__init__(self, url)`
Initializes the class with the target endpoint URL.
- **url** (str): The target endpoint URL.

#### `get_response_body(self)`
Queries the stored URL endpoint via an HTTP GET request.
- **Returns**: `bytes` - The raw response body.

#### `load_json(self)`
Retrieves the raw HTTP response body and deserializes it.
- **Returns**: `list` or `dict` - The parsed JSON data structure.

## Usage Example

```python
from lib.GetRequester import GetRequester

# Target endpoint containing a JSON employee directory
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

# Initialize the requester
requester = GetRequester(url)

# Retrieve raw content (bytes)
raw_bytes = requester.get_response_body()
print("Raw Bytes:", raw_bytes[:100])

# Retrieve and parse JSON payload
employees = requester.load_json()
for employee in employees:
    print(f"Name: {employee['name']}, Occupation: {employee['occupation']}")
```

## Setup & Testing

### Prerequisites
- Python 3.8+
- `requests` library

### Running Unit Tests
To run the automated tests and verify the implementation:
```bash
python -m pytest
```
All tests should pass, confirming correct integration with the API and exact structure matching.
