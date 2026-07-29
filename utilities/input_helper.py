
def get_integer(message):

    while True:

        try:

            value = int(input(message))

            return value

        except ValueError:

            print(

                "Please Enter Integer Value."

            )


def get_float(message):

    while True:

        try:

            value = float(input(message))

            return value

        except ValueError:

            print(

                "Please Enter Numeric Value."

            )


def get_text(message):

    while True:

        value = input(message).strip()

        if value == "":

            print(

                "Input Cannot Be Empty."

            )

            continue

        return value