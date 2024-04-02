from pyspark.sql import functions as F


def get_product_category_pairs(df_products, df_categories):
    # Объединяем датафреймы по идентификатору категории
    joined_df = df_products.join(df_categories, df_products["category_id"] == df_categories["category_id"], "left")

    # Фильтруем пары «Имя продукта – Имя категории»
    product_category_pairs = joined_df.select(df_products["product_name"], df_categories["category_name"]).na.drop()

    # Фильтруем продукты без категорий
    products_without_categories = joined_df.filter(F.col("category_id").isNull()).select(df_products["product_name"])

    return product_category_pairs, products_without_categories

