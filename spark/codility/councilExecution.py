from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.functions import col

class CouncilsJob:
    def __init__(self):
        self.spark_session = (SparkSession.builder.master(
            "local[*]").appName("EnglandCouncilsJob").getOrCreate())
        self.input_directory = '/home/pydev/workflow/dt_learn_data_science/spark/codility/data'

    def extract_councils(self):

        self.district_councilsdf = self.spark_session.read.option("header", "true").option("inferSchema", "true").option(
            "sep", ",").csv(f"{self.input_directory}/england_councils/district_councils.csv")
            
        self.df1 = self.district_councilsdf.withColumn("council_type", lit('district councils'))

        self.london_boroughsdf = self.spark_session.read.option("header", "true").option("inferSchema", "true").option(
            "sep", ",").csv(f"{self.input_directory}/england_councils/london_boroughs.csv")
        self.df2 = self.london_boroughsdf.withColumn("council_type", lit('londonboroughs'))

        self.metropolitan_districtsdf = self.spark_session.read.option("header", "true").option("inferSchema", "true").option(
            "sep", ",").csv(f"{self.input_directory}/england_councils/metropolitan_districts.csv")
        self.df3 = self.metropolitan_districtsdf.withColumn("council_type", lit('metropolitandistricts'))

        self.unitary_authoritiesdf = self.spark_session.read.option("header", "true").option("inferSchema", "true").option(
            "sep", ",").csv(f"{self.input_directory}/england_councils/unitary_authorities.csv")
        self.df4 = self.unitary_authoritiesdf.withColumn("council_type", lit('unitary authorities'))

        self.council_df = self.df1.unionAll(self.df2)
        self.council_df = self.council_df.unionAll(self.df3)
        self.council_df = self.council_df.unionAll(self.df4)

    def extract_avg_price(self):
        self.unitary_authoritiesdf = self.spark_session.read.option("header", "true").option("inferSchema", "true")\
            .option("sep", ",").csv(f"{self.input_directory}/property_avg_price.csv") \
            .select(col('local_authority').alias('council'), col('avg_price_nov_2019'))

    def extract_sales_volume(self):
        self.property_sales_volumedf = self.spark_session.read.option("header", "true").option("inferSchema", "true")\
            .option("sep", ",").csv(f"{self.input_directory}/property_sales_volume.csv")\
            .select(col('local_authority').alias('council'), col('sales_volume_sep_2019'))

    def transform(self, councils_df, avg_price_df, sales_volume_df):
        self.final_df = self.council_df.join(self.unitary_authoritiesdf, self.council_df.council == self.unitary_authoritiesdf.council, "left")\
            .select(self.council_df.council, self.council_df.county, self.council_df.council_type, self.unitary_authoritiesdf.avg_price_nov_2019)

        self.final_df = self.final_df.join(self.property_sales_volumedf,self.final_df.council == self.property_sales_volumedf.council,"left")\
            .select(self.final_df.council,self.final_df.county,self.final_df.council_type,self.final_df.avg_price_nov_2019,self.property_sales_volumedf.sales_volume_sep_2019)    
        
        print(self.final_df.show())
        
        # x = self.final_df.count()
        #self.final_df.write.saveAsTable("lti.english_county_df")
        # return x        

    def run(self):
        return self.transform(self.extract_councils(),self.extract_avg_price(),self.extract_sales_volume())    
            
    # Main Module
s = CouncilsJob()
a = s.run()
# print(a)