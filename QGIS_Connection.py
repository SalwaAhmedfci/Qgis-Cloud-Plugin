from qgis.core import * 
from qgis.gui import * 
from qgis.utils import * 
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from VisionCloud import *
from qgis.utils import iface
from qgis.core import QgsProject
from qgis.PyQt.QtGui import QIcon
from qgis.core import (
    QgsVectorLayer
)
import os
app = QgsApplication([], True) 
path = "C:/Users/A.Nagy/anaconda3/envs/env_qgis/Library/bin/qgis.env" 
app.setPrefixPath(path, True) 
app.initQgis() 
# Get the project instance
project = QgsProject.instance()
# Print the current project file name (might be empty in case no projects have been loaded)
# print(project.fileName())

# Load another project
project.read('C:/Users/A.Nagy/anaconda3/envs/qgis_env/test.qgz')

# The format is:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

uri = QgsDataSourceUri()
# set host name, port, database name, username and password
uri.setConnection('mdahub.com', '5432', 'salwa_baemikae', 'salwa_balytae', 'vomypoci')
# set database schema, table name, geometry column and optionally

uri.setDataSource("public", "cairo2", "the_geom")

vlayer = QgsVectorLayer(uri.uri(False), "layer name you like", "postgres")

QgsProject.instance().addMapLayer(vlayer)

print(uri)


QgsApplication.exitQgis() 
