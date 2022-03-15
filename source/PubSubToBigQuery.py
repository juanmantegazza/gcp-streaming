"""An Apache Beam streaming pipeline.
It reads messages from Pub/Sub, transforms the message data and writes the results to BigQuery.
"""
# [START]
import argparse
import logging
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def custom_function(message):

    """Here we can crate a custom function than takes each message and performes a custom 
    transformation. For example, we can parse a data, replace null values, drop a column, 
    intert a timestamp. Or whatever we like.
    """

    return data
    

def run(
    input_subscription,
    output_table,
    pipeline_args=None):
    """The main function which creates the pipeline and runs it."""

    pipeline_options = PipelineOptions(pipeline_args, save_main_session=True, streaming=True)

    with beam.Pipeline(options=pipeline_options) as pipeline:

        (
            pipeline
            | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(subscription=input_subscription)
            | "UTF-8 bytes to string" >> beam.Map(lambda msg: msg.decode("utf-8"))
            | "Parse JSON messages" >> beam.Map(custom_function)
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                output_table,
                create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()

    # Here we add some specific command line arguments we expect.
    parser.add_argument(
        "--input_subscription",
        help="Input PubSub subscription of the form "
        '"projects/<PROJECT>/subscriptions/<SUBSCRIPTION>."',
    )

    parser.add_argument(
        "--output_table",
        help="Output BigQuery table for results specified as: "
        "PROJECT:DATASET.TABLE or DATASET.TABLE."
    )

    # Parse arguments from the command line.
    known_args, pipeline_args = parser.parse_known_args()

    run(
        input_subscription=known_args.input_subscription,
        output_table=known_args.output_table,
        pipeline_args=pipeline_args
    )
# [END]