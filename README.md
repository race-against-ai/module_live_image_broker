# Live image broker

![Architecture](../../doc/export/architecture.svg "architecture")

Since the rawvideo is transferred via TCP/IP, one application (ffmpeg or live_visualization)
needs to act as a server while the other one acts as a client.
While both applications are capable of both roles, this setup creates huge disadvantage.
When either one of the applications goes down, the other one will go down with it since the connection gets lost.
Especially on the ffmpeg side this can have negative implications because the DJI Goggles might require a
plug out and back in to work properly again.
To overcome such difficulties, the live_image_broker acts according to his name, as a broker between the two.
It acts as a server to both sides. The image source (ffmpeg) can connect on port 50000 and the image sink 
(live_visualization) can connect on port 50001. The live_image_broker will simply pass on all received image data
and also waits for a reconnect if either application (source or sink) is killed. This way both applications can
keep running when the other one is killed, as long as the live_image_broker keeps running.

![live_image_broker schema](../../doc/export/live_image_broker_schema.svg "live_image_broker schema")

## Setup environment

To setup a development environment and install all requirements run the following commands (example for windows):

    python -m venv venv
    venv/Scripts/activate
    python -m pip install -r requirements.txt

## Run

    python live_image_broker/main.py