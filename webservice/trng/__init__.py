## @package trng
#  This package implements a websocket consumer that receives random numbers from the hardware RNG and stores them in a circular buffer to be processed by the api.

import logging

logger = logging.getLogger(__name__)