# Monthly Top Tracks Playlist

This Python application creates a playlist of your top 10 most listened to songs in the last 4 weeks from Spotify. It is intended to be run at the end of each month.

### Prerequisites
- Python 3.x
- A Spotify Developer Account and a registered application to obtain a client_id, client_secret, and redirect_uri
- The spotipy Python library (pip install spotipy)
- The python decouple Python library (pip install python-decouple)

### Installing Required Packages
#### NOTE: I recommend creating a virtual environment before this next step, but it is entirely optional.

To install the required Python packages, navigate to the root directory of the cloned repository and run the following command:

`pip install -r requirements.txt`

This will install the necessary packages to run this project.

### Getting Started
Clone this repository to your local machine.

Create a new file in the root directory of the cloned repository called .env.

In the .env file, add the following lines and replace <your_client_id>, <your_client_secret>, <your_redirect_uri> with your actual Spotify Developer app information:

`CLIENT_ID=<your_client_id>`

`CLIENT_SECRET=<your_client_secret>`

`REDIRECT_URI=<your_redirect_uri>`

Run the application and follow the prompts to log in to your Spotify account and authorize the application.
The application will then generate a playlist of your top 10 most listened to songs in the last 4 weeks.

### Acknowledgments

[Spotify Web API](https://developer.spotify.com/documentation/web-api)

[spotipy Python library](https://spotipy.readthedocs.io/en/2.24.0/)
