import openpyxl
import pywhatkit as pwk
from phonenumbers.phonenumberutil import NumberParseException
import time

group_number = 'HM6R2qU8yhMCo4c3XL0DmJ'
processed_rows = set()
# https://chat.whatsapp.com/D:D:\Mallika\Madu new file
def process_excel_file():
    workbook = openpyxl.load_workbook('D:\Mallika\Madu new file.xlsx')
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        slno = row[0]
        name = row[1]
        

        message = f"Sl No: {slno}\nname: {name}"

        if row in processed_rows:
            print(f"Skipping duplicate row: {row}")
            continue

        try:
            current_time = time.localtime()
            time_hour = current_time.tm_hour
            time_min = current_time.tm_min + 1

            wait_time = 8 # Set the wait_time as desired

            pwk.sendwhatmsg_to_group(group_number, message, time_hour, time_min, wait_time)
            processed_rows.add(row)
        except NumberParseException:
            print(f"Country code missing for WhatsApp group: {group_number}")

def run_code_continuously():
    while True:
        process_excel_file()
        time.sleep(10)  # Delay between iterations (e.g., 1 minute)

if __name__ == '__main__':
    process_excel_file()  # Initial processing
    run_code_continuously()