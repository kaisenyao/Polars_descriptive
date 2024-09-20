import pandas as pd
import polars as pl
import matplotlib.pyplot as plt


def read_dataset_pd(file_path):
    df = pd.read_csv(file_path)
    print("Dataset successfully loaded using Pandas!")
    print("Columns in dataset:", df.columns)
    return df


def read_dataset_pl(file_path):
    df = pl.read_csv(file_path, ignore_errors=True)
    print("Dataset successfully loaded using Polars!")
    print("Columns in dataset:", df.columns)
    return df


def generate_summary_pd(df):
    numeric_columns = ["Age", "Years of Experience", "Salary"]
    print("\nImportant Summary Statistics (Rounded to 2 Decimals):")
    summary = df[numeric_columns].describe().round(2)
    print(summary)
    return summary.to_dict()


def generate_summary_pl(df):
    numeric_columns = ["Age", "Years of Experience", "Salary"]
    print("\nImportant Summary Statistics (Rounded to 2 Decimals):")
    summary = df.select(numeric_columns).describe()
    print(summary)
    summary_dict = {
        col: summary.select(pl.col(col)).to_pandas().to_dict()
        for col in numeric_columns
    }
    return summary_dict


def create_visualization_pd(df, column):
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=20, edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(False)
    plt.savefig("data_visualization.png")
    plt.show()


def create_visualization_pl(df, column):
    df_pandas = df[column].to_pandas()
    plt.figure(figsize=(10, 6))
    df_pandas.hist(bins=20, edgecolor="black")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(False)
    plt.savefig("data_visualization.png")
    plt.show()


def save_comparison_report(
    pandas_stats, polars_stats, output_file="summary_comparison_report.md"
):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Summary Comparison Report\n\n")

        for key in pandas_stats:
            f.write(f"## {key}\n\n")
            f.write("### Pandas\n")
            f.write(f"{pandas_stats[key]}\n\n")
            f.write("### Polars\n")
            f.write(f"{polars_stats.get(key, 'N/A')}\n\n")

    print(f"Comparison report saved to {output_file}")
