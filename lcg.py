from openpyxl import Workbook
import time


class LCG:
    def __init__(self, seed):
        self.m = 2 ** 40 - 1
        self.a = 1103515245
        self.c = 12345
        self.state = seed

    def run(self):
        self.state = (self.a * self.state + self.c) % self.m
        return (self.state | (1 << 39)) & 0xFFFFFFFFFF

def create_spreadsheet(path, row_to_freeze):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "LCG"
    sheet.freeze_panes = row_to_freeze
    headers = ["Number", "Number length", "Time taken"]
    sheet["A1"] = headers[0]
    sheet["B1"] = headers[1]
    sheet["C1"] = headers[2]
    data = []

    for _ in range(100):
        seed = int(time.time())
        lcg = LCG(seed)

        start_time = time.monotonic()
        number = lcg.run()
        end_time = time.monotonic()
        time_taken = end_time - start_time

        data.append([f'{number}', f'{number.bit_length()} bits', f'{time_taken:.6f} s'])

        time.sleep(1)

    formatted_data = []
    for i in range(len(data)):
        formatted_data.append(dict(zip(headers, data[i])))

    row = 2
    for d in formatted_data:
        sheet[f'A{row}'] = d["Number"]
        sheet[f'B{row}'] = d["Number length"]
        sheet[f'C{row}'] = d["Time taken"]
        row += 1
    workbook.save(path)


create_spreadsheet("lcg.xlsx", "A2")
