# Web Scraper

## Overview
The web scraper is a single GET API which calls a server that extracts JSON data from a list of URLs and returns a response with product details. 

## Table of Contents
- [Installation](#installation)
- [Endpoint](#endpoint)
- [Usage](#usage)
- [Response-formats](#response-formats)
- [Unit-test](#unit-test)

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/mamihackl/WebScraper.git
    ```
2. Navigate to the project directory:
    ```
    cd WebScraper 
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Endpoint
This endpoint facilitates two operations: retrieving data from a single URL and extracting target data in JSON format from a list of URLs, both accomplished through a GET request.
```
http://127.0.0.1:5000/product-details
```


## Usage
To run the application, use the following command:

1. In one shell, run the following command:
```
python webscraper.py
```

2. Open another shell, and run the following command:

```
curl -X GET -H "Content-Type: application/json" -d '["https://example1", "https://example2"]' http://127.0.0.1:5000/product-details
```

Alternatively, you can also use Postman. How to test using Postman, please refer to https://www.postman.com/api-platform/api-testing/


## Response formats
The response is structured in JSON format as follows: It consists of a list of dictionaries, with each dictionary containing the keys 'displayName' and 'url'.

```
[
    {
        "url": "https://example1",
        "displayName": [
            "example1"
        ]
    },
    {
        "url": "https://example2",
        "displayName": [
            "example2"
        ]
    }
]
```

## Unit test
To run the unit test, use the following command:

```
python -m unittest test_web_scraper.py 
```
