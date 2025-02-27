from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

visa_jap_df = spark.read.format('csv').option('header','true').load('../input/visa_number_in_japan.csv')
visa_jap_df.show()