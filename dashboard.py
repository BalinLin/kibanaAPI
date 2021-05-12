## Dashboards
from kibana_dashboard_api import VisualizationsManager, DashboardsManager
from elasticsearch import Elasticsearch

es_connection = Elasticsearch(hosts=['http://elastic:changeme@localhost:9200/'])

visualizations = VisualizationsManager(es_connection)
dashboards = DashboardsManager(es_connection)

vis_list = visualizations.get_all()
vis = vis_list[0]
vis.title = 'New Title'
visualizations.update(vis)

# list all dashboards
dash_list = dashboards.get_all()
print(dashboards)
for d in dash_list:
    print(d.title)

# Add a visualization to the first dashboard
dash = dash_list[0]
dash.add_visualization(vis, 6, 3)
dashboards.update(dash)