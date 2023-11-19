# weathergov-python
Show weather forecast using weather.gov api
# Weather Forecast Applications

## Description
This repository contains two very simple applications for displaying weather forecasts: a terminal app and a web app. Both applications fetch weather data based on geographical coordinates of a provided location name within the United States. (Cambridge, MA for example).

### Terminal Application
- Fetches and displays weather forecasts for a specified location directly in the terminal.
- Utilizes GeoPy to convert location names to geographical coordinates. [GeoPy](https://geopy.readthedocs.io/en/stable/#)
- Retrieves weather forecast data using the [National Weather Service API](https://weather-gov.github.io/api/general-faqs) 

### Web Application
- Code mainly lifted from terminal application
- Flask-based web appl that displays weather forecasts on a (very simple) web page.
- Dynamically renders the webpage using Flask and Jinja2 templates.


## API Used
- **Nominatim API via GeoPy**: For converting location names to latitude and longitude.
- **National Weather Service API**: Provides weather forecast data based on geographical coordinates.

## Libraries and Packages
- **Flask**: For the web application's server and web pages.
- **GeoPy**: For geocoding location names.
- **Requests**: For making HTTP requests to APIs.

## Setup and Installation
1. Clone the repository:
`git clone [https://github.com/benpinter88/weathergov-python]`
2. Install required packages:
`pip install Flask geopy requests`

### Running the Terminal Application
Execute the terminal application script:

`python terminal_app.py`

### Running the Web Application
Start the Flask web server:

`python web_app.py`

Visit `http://127.0.0.1:5000/` in your web browser to view the forecast page.
