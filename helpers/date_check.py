import re
import sys
import datetime

# load file and get date string
def check_date(files: list) -> bool:
    
    for file in files:
        with open(file) as fd:
            text = fd.read()

        date_string = re.search(r'Date: (\d{4}-\d{2}-\d{2})', text).group(1)
        post_date = datetime.date.fromisoformat(date_string)
        
        if not post_date == datetime.date.today():
            print("Date is not correct!")
            return False

        return True

if __name__ == "__main__":
    result = check_date(sys.argv[1:])

    if result:
        sys.exit(0)
    else:
        sys.exit(1)