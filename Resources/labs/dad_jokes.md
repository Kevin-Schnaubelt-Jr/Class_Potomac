**Dad Joke API Lab: How to Fetch Jokes using Python**

### Objectives:

1. Understand the basics of working with APIs.
2. Get familiar with the `requests` library in Python.
3. Learn how to handle JSON data in Python.

### Introduction:
This lab will guide you through the process of making an HTTP request to an API, retrieving a dad joke, and parsing the response.

### Requirements:
1. Python installed on your system.
2. `requests` library installed.
   - You can install it using pip:
     ```bash
     pip install requests
     ```

### Step-by-step guide:

#### Step 1: Import necessary modules

The first step is to import the required modules:

- `requests`: A popular Python library for making HTTP requests.
- `json`: A built-in Python library for working with JSON data.

```python
import requests
import json
```

#### Step 2: Set up the API endpoint

We will be fetching dad jokes from the `icanhazdadjoke` API. This API provides a URL endpoint that, when accessed, returns a random dad joke.

```python
url = 'https://icanhazdadjoke.com/'
```

#### Step 3: Make the request

To fetch data from the API, we use the `requests.get()` method. This function requires two arguments:

- The API URL.
- A dictionary of headers.

In our case, the header `{'Accept': 'application/json'}` tells the server that our program wants the data in JSON format.

```python
response = requests.get(url, headers={'Accept': 'application/json'})
```

#### Step 4: Parse the JSON response

The response we get from the server is in string format. To convert this string into a Python dictionary, we use the `json.loads()` method.

```python
data = json.loads(response.text)
```

#### Step 5: Print the data

Finally, we print out the data we've fetched. It will be a dictionary that contains various details about the joke, including the joke itself.

```python
print(data)
```

### Running the Program:

When you run the program, you should see an output similar to the following:

```
{'id': 'some_id', 'joke': 'Why did the scarecrow win an award? Because he was outstanding in his field!', 'status': 200}
```

**Note:** The actual joke may vary, as the API returns random dad jokes.

### Extensions:

1. Instead of printing the whole dictionary, you can extract just the joke by using:
   ```python
   print(data['joke'])
   ```

2. Add error handling. Sometimes the API might not respond, or there might be other issues. It's a good practice to handle such situations gracefully.

3. Create a loop to fetch multiple jokes with a time delay in between.

Enjoy the dad jokes!