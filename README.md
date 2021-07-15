**Description**

`bhodl-calculator` is a simple webapp that use Coingekko API to calculate the current value of a previous investment in Bitcoin.
You can try it with my live [demo](https://calculator.bhodl.io). Note that the API can only handle 100 requests/minutes, so the best is to run it youself.

**Setup**

Clone bhodl-calculator :
```
~/$ git clone https://github.com/bhodl/bhodl-calculator.git
```
****
Setup a virtual environnement, activate it, and install dependancy like this :
```
~/$ cd bhodl-calculator
~/bhodl-calculator/$ virtualenv -p python3 .env
~/bhodl-calculator/$ source .env/bin/activate
(.env)~/bhodl-calculator/$ pip install -r requirements.txt
```
Now run the app like this :
```
(.env)~/bhodl-calculator/$ python app.py
```
You shoud now see something like this in the terminal window :
```
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN:154-254-654
```
Just point your browser to the address and your're good to go!

**To do**
* Add safegard to prevent to much requests
* Prevent the use of not allowed date
