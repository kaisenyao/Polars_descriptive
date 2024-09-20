from pyinstrument import Profiler
from main import (
    read_dataset_pl,
    read_dataset_pd,
    generate_summary_pl,
    generate_summary_pd,
    create_visualization_pl,
    save_comparison_report,
)

file_path = "salary.csv"


def test_read_dataset_pd():
    df_pd = read_dataset_pd(file_path)
    assert df_pd is not None


def test_read_dataset_pl():
    df_pl = read_dataset_pl(file_path)
    assert df_pl is not None


if __name__ == "__main__":
    df_pd = read_dataset_pd(file_path)
    df_pl = read_dataset_pl(file_path)

    if df_pl is not None and df_pd is not None:
        stats_pd = generate_summary_pd(df_pd)
        stats_pl = generate_summary_pl(df_pl)
        create_visualization_pl(df_pl, column="Salary")
        save_comparison_report(stats_pd, stats_pl)
