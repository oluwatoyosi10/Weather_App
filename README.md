PURPOSE:
This app provides the user with real-time weather information and other weather related data which can help them make better decisions for their day to day activities. Activities which include;
*Travel Planning: Users can check the weather of a destination before planning a trip.
*Daily Planning: Knowing the weather helps users plan their day, considering factors like temperature and precipitation.
*Emergency Preparedness: Weather information is crucial during emergencies, such as storms or extreme temperatures.

The App:
The provided code implements a simple weather application using the OpenWeatherMap API. The application has one main windows . Users can input a city on the main window, and the app fetches and displays the current weather information for that city.
The following libraries where used in the creation of the app;
*.	request library: is a library used in making HTTP requests, which means it simplifies the process of sending and receiving data from websites
*.	Pillow library (PIL fork): is a powerful library for working with images. It provides a wide range of image processing capabilities, making it a popular choice for tasks such as opening, manipulating and saving various image file formats.
*.	tkinter library: is used for creating a graphical user interface (GUI). It provides functions for creating Windows, labels, buttons, entry fields’ e.t.c.
In addition to these, the following functions where used in the creation of the app;
*.	request.get: this function takes a URL as its first argument and returns a response object. The response object contains all the information that was returned by the server in response to your request.
*.	get_weather: this retrieves weather information for the city entered in the entry field and displays the information on the GUI
*.	Open main.window: this function opens the main window of the app which contains GUI elements like labels, entry, fields, buttons e.t.c.
*.	Mainloop function: this function is used to start the tkinter event loop which continuously listens to events and updates the GUI accordingly. 
