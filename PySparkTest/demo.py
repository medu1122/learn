from pyspark.sql import SparkSession
def read_csv_file():
    spark=SparkSession.builder.appName("demo").getOrCreate() # tao session
    df=spark.read.csv("data.csv",header=True,inferSchema=True) # doc file csv
    df.show()
    df.printSchema()
def main():
    read_csv_file()
if __name__ == "__main__":
    main()