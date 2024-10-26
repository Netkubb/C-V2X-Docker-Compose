FROM mongo

COPY init.json /init.json
# password: password
CMD mongoimport --host mongodb --db reach-engine --collection User --type json --file /init.json --jsonArray