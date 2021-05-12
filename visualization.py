## Visualizations
from kibana_dashboard_api import VisualizationsManager, DashboardsManager
from elasticsearch import Elasticsearch
import json

es_connection = Elasticsearch(hosts=['http://elastic:changeme@localhost:9200/'])
visualizations = VisualizationsManager(es_connection)

# Elasticsearch connect
# result = es_connection.indices.create(index='news', ignore=400)
# result = es_connection.indices.delete(index='news', ignore=400)
# result = es_connection.search(index='analysislog-1205_1206')
# print(json.dumps(result, indent=4))

# list all visualizations
vis_list = visualizations.get_all()
for vis in vis_list:
    print(vis.title)


#change the title of the first visualization and save it
vis = vis_list[0]
vis.title = 'New Title'
visualizations.update(vis)