from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import col

class ETLSuperStore:
    # Create the Spark Session and Path Folder
    def __init__(self):
        self.spark_session = (SparkSession.builder.master("local[*]").appName("SuperStoreETL").getOrCreate())
        self.path_folder = "/home/pydev/workflow/dt_learn_data_science/spark/superstore"

    def extractSales(self):
            self.salesDf = self.spark_session.read.option("header", "true") \
                .option("inferSchema", "true")\
                .option("sep", ",")\
                .csv(f"{self.path_folder}/data/Super_Store_Sales_*.csv")

            # print(self.salesDf.count())
            # print(self.salesDf.show())
            # print("Hello")    

# Main
etl = ETLSuperStore()
etl.extractSales()
