# Kafka Containers

This `docker-compose` file is comprised of 2 services.

A `development runtime` of a `Kafka Cluster`, and a UI so you can see
what is the configuration of the cluster, broker, topics, and consumers.

## Kafka Cluster

The kafka cluster runs on default ports that is used by kafka.

It is also running a schema registry in port `8081`.

An optional monitoring port is also available but is disabled by the `docker-compose` env variable.

The cluster does not have authentication to make it easily accessible for learning.

The cluster also comes with a lightweight UI to check cluster configuration and contents, but is not
as rich as the UI service we are spinning up with this compose file. This cluster's UI is accessible via
`http://localhost:3030`

## Kafka Cluster UI

The UI is a richer way to view the kafka cluster.

It is accessible via `http://localhost:9080`.
