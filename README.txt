To use the wikipedia scraper microservice simply fire up the wikiServer.py file and make a post request to localhost:1400

The post request should be in the form {'item': data} where the data is a string type

The wikiServer.py file will print the wikipedia summary to console as well as return this data in a JSON object

To access the response in your client, you first receive the json response and then you can print it using response["item"]

You may change the port to your liking

The wikiApp.py file functions as a client and is set up to make post requests from a string you enter on the command line, but is not necessary if you plan to make the requests from your own program!

Please message me on discord with any questions!!
