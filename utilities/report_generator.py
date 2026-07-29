
from tabulate import tabulate

def display_table(records, headers):

    if not records:

        print("\nNo Records Found.")

        return

    print()

    print(

        tabulate(

            records,

            headers=headers,

            tablefmt="grid"

        )

    )

def print_heading(title):

    print()

    print("=" * 80)

    print(title.center(80))

    print("=" * 80)