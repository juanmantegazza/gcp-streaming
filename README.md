# Streaming Project in Google Cloud Platform
The idea of this project is to use GCP data stack to ingest data in real time, wrangle it and load it to a Data Warehouse. The data products that I will be using are PubSub, Dataflow and BigQuery.

I am going to keep a template style the most I can so this structure is useful for a lot of different projects.

## Ingestion with Pub/Sub
The idea of this part is to spin up a [Pub/Sub topic](https://cloud.google.com/pubsub/docs/create-topic-console) so we can publish messages to it. I choose not to cover the part of App that generates the data because that is actually the part that makes the difference between projects. Because of that, what we need is a topic and a [suscription](https://cloud.google.com/pubsub/docs/create-topic-console) asociated with that topic.

The moment we have the topic ready, we would choose one of all the ways of [publishing messages](https://cloud.google.com/pubsub/docs/publisher#python) to that topic. I generally use the console to publish some dummy data and then set up the [Python Client Library](https://googleapis.dev/python/pubsub/latest/index.html) for a productive PoV.

## ETL with Dataflow
Now that we have the topic ready and messages comming, we neet to capture them, maybe do some cleaning to them, and load them to a place we can use them(run queries on it, use the date as source for dashboards, etc.)

We are going to use [Dataflow](https://cloud.google.com/dataflow/docs/concepts), that internally runs the [Apache Beam](https://beam.apache.org/documentation/) programming model.

In a simplified way, what we need to do is to create a [Driver Program](/source/) which later will be deployed to the cloud. More info on the [source folder](/source/).