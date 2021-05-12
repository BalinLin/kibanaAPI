# How to run Grafana on docker
```bash==
cd cd ~/exper/docker-elk
docker-compose up -d
```

# Visit Grafana on localhost
- http://127.0.0.1:5601/

# Run grafana_api
- install
```bash==
pip install kibana-dashboard-api
```
- run
```bash==
python visualization.py
```

# Reference
- [kibanaAPI](https://github.com/harabchuk/kibana-dashboard-api)