# SiGaSkartioSvakaCast
SHA256, backend

REST backed for a url "shortening"
Acctualy the Hash doesnt work like that, it prolongs actual url
But for a sake of a argument, I used implemented Hash algorithm SHA256

How to run this app:

pip install flask

Then go to src/ and run:

python view.py

This will start application on localhost port 5000

There is sample data in Data folder. That was and will be used for test pourpose. The Data wont affect applications functionalities

Keep in mind that this application doesnt not have permanet memory, so if app is restarted hashed links will be LOST.

