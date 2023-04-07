from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Example PySpark App") \
    .getOrCreate()

# Create a sample DataFrame
data = [("Alice", 28), ("Bob", 35), ("Charlie", 45), ("Dave", 25)]
df = spark.createDataFrame(data, ["name", "age"])

# Print the DataFrame
df.show()

# Filter the DataFrame
filtered_df = df.filter(df.age > 30)

# Print the filtered DataFrame
filtered_df.show()

# Stop the SparkSession
spark.stop()