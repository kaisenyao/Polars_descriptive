from pyinstrument import Profiler
from main import (
    read_dataset_pl,
    read_dataset_pd,
    generate_summary_pl,
    generate_summary_pd,
)


def save_profiler_report(
    profiler_pl, profiler_pd, output_file="profiler_comparison_report.md"
):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Profiler Comparison Report\n\n")

        f.write("## Polars Profiler Output\n\n")
        f.write("```\n")
        f.write(profiler_pl)
        f.write("\n```\n\n")

        f.write("## Pandas Profiler Output\n\n")
        f.write("```\n")
        f.write(profiler_pd)
        f.write("\n```\n")

    print(f"Profiler comparison report saved to {output_file}")


if __name__ == "__main__":
    file_path = "salary.csv"

    # Profiler for Polars
    with Profiler(interval=0.001) as profiler:
        df = read_dataset_pl(file_path)
        print(df.shape)
        generate_summary_pl(df)
        print(df["Age"].median())

    profiler_pl = str(profiler.output_text())
    print(profiler_pl)

    # Profiler for Pandas
    with Profiler(interval=0.001) as profiler2:
        df = read_dataset_pd(file_path)
        print(df.shape)
        generate_summary_pd(df)
        print(df["Age"].median())

    profiler_pd = str(profiler2.output_text())
    print(profiler_pd)

    # Save profiler comparison report
    save_profiler_report(profiler_pl, profiler_pd)
