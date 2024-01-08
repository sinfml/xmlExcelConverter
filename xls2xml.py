import xlrd
import xml.etree.ElementTree as ET


def readExcel():
    data = xlrd.open_workbook("string.xlsx")
    sheet = data.sheets()[0]

    nclos = sheet.ncols
    nrows = sheet.nrows
    print("total clos : %d, rows : %d" % (nclos, nrows))

    keys = sheet.col_values(0, 0, nrows)
    values = sheet.col_values(1, 0, nrows)
    print("keys: %s and values : %s" % (str(keys), str(values)))

    map = {}

    for index in range(len(keys)):
        map[keys[index]] = values[index]

    return map


# 添加到xml树中
def addToElement(root, key, value):
    subElements = ET.SubElement(root, "string", {"name": key})
    subElements.text = value


# 读取excel内容
map = readExcel()
# 构建xml
root = ET.Element("resources")
items = map.items()

for key, value in items:
    addToElement(root, key, value)

data = ET.ElementTree(root)
data.write("test.xml", encoding="utf-8")
