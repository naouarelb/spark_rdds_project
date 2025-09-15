from pyspark.sql import SparkSession, DataFrame


def load_data(spark: SparkSession, path: str) -> DataFrame:
    data = spark.read.csv(path = path, header = True)
    data = data.repartition(8)
    return data