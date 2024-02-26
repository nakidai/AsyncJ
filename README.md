# AsyncJ
**AsyncJ - Python module for fast asynchronous work with JSON files**

# Examples
**Get a dictionary from a JSON file**

```py
# Importing modules
import asyncio # To run the asynchronous main() function

from asyncj import AsyncJson # Main class used in the example

# Initialize the class with filename
asyncjson =  AsyncJson("test.json")


# The asynchronous main() function
async def main() -> None:
	# Getting a dictionary
	data: dict = await asyncjson.read()
	# Displaying the resulting dictionary
	print(data)


# Running the asynchronous main() function
if __name__ == "__main__": 
	asyncio.run(main())
```

**Change dictionary in JSON file**
```py
# Importing modules
import asyncio # To run the asynchronous main() function

from asyncj import AsyncJson # Main class used in the example

from random import randint # To generate a random number

# Initialize the class with filename
asyncjson =  AsyncJson("test.json")


# The asynchronous main() function
async def main() -> None:
	# Getting a dictionary
	data: dict = await asyncjson.read()
	# Getting a random number
	random_number: int = randint(100, 999)
	# Setting a new random value in the dictionary for the "test" key
	data["test"] = random_number
	# Writing the modified dictionary to a JSON file
	await asyncjson.write(data)
	

# Running the asynchronous main() function
if __name__ == "__main__": 
	asyncio.run(main())
```

# Requirements
**Python version 3.8 or higher**