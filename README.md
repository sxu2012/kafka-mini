# kafka-mini
Building A Streaming Fraud Detection System With Kafka + Python

Files:
- docker-compose.kafka.yml: docker-compose file for kafka cluster
- docker-compose.yml: docker-compose file for our kafka flaud detection applicaiton
- screenshots.pdf: screenshots of running the kafka cluster, the fake transaction generator, and the fraud detector application. 
- generator: folder that contains the fake transaction generator application
- detector: folder that contains the fraud detection application

Running procedure:
1. Build and start kafka cluster

docker-compose -f docker-compose.kafka.yml up --build

2. Build and start fraud detection application

docker-compose up --build

3. View the result fraud transactions:

docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud

4. View the result legit transactions:

docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consume --bootstrap-server localhost:9092 --topic streaming.transactions.legit
