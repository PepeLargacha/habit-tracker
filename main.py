"""Main Script"""

import datetime
from pixela_user import delet_pixel

GRAPH_ID = 'graph1'
# graph_unit = 'min'
# graph_unit_type = 'int'
today = datetime.datetime.now().date()

delet_pixel(GRAPH_ID, today)
