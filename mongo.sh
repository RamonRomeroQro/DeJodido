
if [ ! -d ./data/db ]; then
    echo 'data does not exist, creating ...'
    mkdir -p ./data/db
fi

echo 'running mongo deamon ...'
mongod --dbpath ./data/db
