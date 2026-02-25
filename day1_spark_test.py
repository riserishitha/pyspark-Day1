from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Day1SparkLearning") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Version:", spark.version)
print("Spark Session Created Successfully")

spark.stop()