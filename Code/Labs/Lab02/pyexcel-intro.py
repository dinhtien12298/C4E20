import pyexcel
dataa = [
    {
        "Name": 'Tien',
        'age': ' 20'
    },
    {
        'Name': 'abc',
        'age': '12'
    }
]

pyexcel.save_as(records=dataa, dest_file_name="your_file.xls")
