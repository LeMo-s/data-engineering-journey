The script processes an input CSV file containing two columns — products and amount — and performs the following steps:

    - Data Ingestion: Reads the raw CSV file into a dataframe.

    - Text Standardization: Trims leading/trailing whitespaces and converts all fruit names to lowercase to eliminate formatting    inconsistencies (e.g., treating " Apple " and "apple" as the same product).

    - Missing Value Removal: Drops any rows containing null values.

    - Deduplication: Filters the dataframe to retain only unique rows, removing any duplicate entries.

    - Data Export: Writes the fully cleaned and optimized dataframe into a new, separate CSV file.


Why Null Values Were Dropped

During data exploration, a single anomaly was identified: one row contained a valid fruit name but had a null value in the amount column. All other rows contained valid integer values.

    Design Decision: The row with the missing amount was intentionally dropped from the final dataset for the following reasons:

        - Data Integrity: The primary purpose of this dataset is to track quantities. A product record without a numerical amount provides no actionable value for inventory management or downstream analysis.

        - Statistical Accuracy: Leaving a null value or filling it with an arbitrary placeholder (like 0 or the mean) could skew total counts and averages.

        - Minimal Impact: Because this was an isolated incident affecting only one row, dropping it completely preserves the integrity of the data without sacrificing any significant volume of information.

Critical Caveat: Why the Deduplication (unique) Result Cannot Be Fully Trusted

While the .unique() method was applied to clean up potential data-entry repetition, its results must be treated with caution due to a structural limitation in the source data.

    The ID Problem: The dataset completely lacks a unique identifier column (such as a transaction_id).

Because there is no unique ID to differentiate records, running .unique() introduces the following risks:

    - Accidental Data Loss: In a sales or inventory log, it is entirely possible for two separate, legitimate events to look identical. For example, if two different customers buy 5 apples on the same day, both transactions will read as apple, 5. Polars has no way of knowing these are separate real-world events; it will see them as duplicates and delete one.

    - Under-Counting Metrics: By dropping identical rows blindly, the pipeline assumes any matching row is a system glitch. If those rows were actually separate, valid transactions, the final aggregated totals will actively under-report real sales volumes.

Conclusion: For the purpose of this script, duplicate rows are assumed to be illegitimate repeats to prevent data inflation. However, in a production environment, this deduplication cannot be 100% trusted until a unique transaction ID is added to the source schema.