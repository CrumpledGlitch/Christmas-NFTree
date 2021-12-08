
# Christmas NFTree

Mint an NFT, watch the tree

## Setup
- WS2812 Connected to Pi however needed
- git clone
- cd repo

- sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel redis flask rq

--

- wget http://download.redis.io/releases/redis-6.0.6.tar.gz
- tar xzf redis-6.0.6.tar.gz
- cd redis-6.0.6
- make

-- 

- install nodejs
- install npm


## Running the tree

The following need to be running in screens or as services (be sure to check which should be run as root or sudo) ;

- **sudo** Lights_Control.py 
- redis-server
- **sudo** rq worker
- sh Youtube.sh (you will have to create your own key)

