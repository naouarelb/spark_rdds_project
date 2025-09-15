from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os
from transformation.utils import load_data
from transformation.cleaning import cleaning
from transformation.logs import log_summary

spark = SparkSession.builder \
    .appName("MyAnalysisApp") \
    .config("spark.sql.warehouse.dir", "/opt/spark-app/application/tmp") \
    .getOrCreate()

if __name__ == "__main__":
    load_dotenv(dotenv_path="/opt/spark-app/application/app/.env")
    required_env_vars = ["USER_INTERACTION_PATH", "PRODUCT_CATALOG_PATH", "USER_REVIEW_PATH", "LOG_DIR"]
    missing = [env_var for env_var in required_env_vars if env_var not in os.environ]
    if missing:
        print(f"Missing environment variables {','.join(missing)}")
    else:
        USER_INTERACTION_PATH = os.environ["USER_INTERACTION_PATH"]
        PRODUCT_CATALOG_PATH = os.environ["PRODUCT_CATALOG_PATH"]
        USER_REVIEW_PATH = os.environ["USER_REVIEW_PATH"]
        LOG_DIR = os.environ["LOG_DIR"]
        print(f"user intercations file path: {USER_INTERACTION_PATH}")
        print(f"product catalog file path: {PRODUCT_CATALOG_PATH}")
        print(f"user reviews file path: {USER_REVIEW_PATH}")
        print(f"Log dir is: {LOG_DIR}")

    user_interaction = load_data(spark, USER_INTERACTION_PATH)
    product_catalog = load_data(spark, PRODUCT_CATALOG_PATH)
    user_review = load_data(spark, USER_REVIEW_PATH)

    # Cleaning the data !
    user_interaction, product_catalog, user_review = cleaning(user_interaction, product_catalog, user_review)
    user_review.printSchema()

    # Analyze the data (outputs to log file)
    log_summary(LOG_DIR, user_interaction, product_catalog, user_review)
        
    # Cleaned Data joined
    # Repartition data
    product_catalog = product_catalog.repartition("product_id")
    user_review = user_review.repartition("product_id")
    user_interaction = user_interaction.repartition("user_id", "product_id")


    joined = product_catalog.join(user_review, on="product_id", how="right")
    dataset = joined.join(user_interaction, on=["user_id", "product_id"], how="outer")

    dataset.write.mode("overwrite").csv("application/app/output/dataset.csv")

    # print("The dataset combined:")
    # dataset.show(20)