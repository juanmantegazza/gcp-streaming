# Dataflow Driver Program

## Direct Runner vs Dataflow Runner
We basically have 2 ways of running our job(there are more but they are out of the scope). We can run it locally using the Direct Runner, or we can run it in the cloud using the Dataflow Runner.

What we always should do is to iterate through the first versions of the code using the Direct Runner, to catch silly bugs. And after that, use the Dataflow Runner to test the program it in the cloud.

In this case, we have a [version for the Direct Runner](/source/PubSubToBigQuery_dr.py) and a [version for the Dataflow Runner](/source/PubSubToBigQuery.py). The main difference is that we need to pass the credentials in the first case. To do that, we need to create a service account with the appropiate permissions and generate a json key.

To run 

## PubSubToBigQuery.py
Once we debug it locally we can 