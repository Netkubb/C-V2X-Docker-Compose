FROM mongo

COPY init.json /init.json
# password: password
CMD mongoimport --host mongo --db cv2x --collection users --type json --file /init.json --jsonArray --username mongo --password mongo --authenticationDatabase admin 