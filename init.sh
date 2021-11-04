cd lyo-samples/trs4j-bugzilla-sample
mvn clean jetty:run &
cd ../..

docker-compose up -d
docker-compose -f ewetasker_server/docker-compose.yaml up -d