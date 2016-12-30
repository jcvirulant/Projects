row = None

def validate_row(self):

    try:
        self.row = int(input('Row Number: '))
    except ValueError:
        print('Incorrect input. Please enter a number between 1 and 10.')
        self.validate_row()
    else:
        if self.row in range(1, 11):
            print(row)
        else:
            print('Incorrect input. Please enter a number between 1 and 10.')
            self.validate_row()

validate()
