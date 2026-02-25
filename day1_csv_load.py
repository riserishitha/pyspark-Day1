from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSVLoad") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv(
    "data/users.csv",
    header=True,
    inferSchema=True
)
df.select("name", "city").show()
df.filter(df.age > 25).show()
df.groupBy("city").count().show()
df.show()
df.printSchema()

spark.stop()