#!/bin/bash

# Check if unoserver is running
if pgrep -x "unoserver" > /dev/null; 
then
    :
else
    # Start unoserver in the background
    unoserver >> /dev/null &
    echo "unoserver started in the background."
fi

python $(pwd)/app.py