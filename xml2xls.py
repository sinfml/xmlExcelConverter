import xlwt
import xml.etree.ElementTree as ET


# 打开xml文件
def openXml(
    str="",
):
    return ET.parse(str)


# 写到exceml
def writeToExecel(map: dict):
    workbook = xlwt.Workbook(encoding="ascii")
    sheet = workbook.add_sheet("translation")
    keys = list(map)
    count = len(map)
    for index in range(count):
        key = keys[index]
        sheet.write(index, 0, key)
        sheet.write(index, 1, map[key])
    workbook.save("string.xlsx")


xmlFile = openXml()

map = {}

for root in xmlFile.getroot():
    stringRoot = root.attrib.get("name")
    map[stringRoot] = root.text

writeToExecel(map)
