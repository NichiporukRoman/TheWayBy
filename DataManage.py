import xml.etree.ElementTree as ET


def manageDataCategory(id, category):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()

    region_old = root.find('self_travelling').find('region').text

    root = ET.Element('root')
    self_travelling = ET.SubElement(root, 'self_travelling')
    category_new = ET.SubElement(self_travelling, 'category')
    region_new = ET.SubElement(self_travelling, 'region')
    num_new = ET.SubElement(self_travelling, 'num')
    num_new.text = '1'
    category_new.text = category
    region_new.text = region_old
    tree = ET.ElementTree(root)
    tree.write('Data/' + str(id) + '.xml')


def manageDataRegion(id, region):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()

    category_old = root.find('self_travelling').find('category').text

    root = ET.Element('root')
    self_travelling = ET.SubElement(root, 'self_travelling')
    category_new = ET.SubElement(self_travelling, 'category')
    region_new = ET.SubElement(self_travelling, 'region')
    num_new = ET.SubElement(self_travelling, 'num')
    num_new.text = '1'
    category_new.text = category_old
    region_new.text = region
    tree = ET.ElementTree(root)
    tree.write('Data/' + str(id) + '.xml')


def manageDataNum(id, num):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()

    category_old = root.find('self_travelling').find('category').text
    region_old = root.find('self_travelling').find('region').text

    root = ET.Element('root')
    self_travelling = ET.SubElement(root, 'self_travelling')
    category_new = ET.SubElement(self_travelling, 'category')
    region_new = ET.SubElement(self_travelling, 'region')
    num_new = ET.SubElement(self_travelling, 'num')
    num_new.text = num

    category_new.text = category_old
    region_new.text = region_old
    tree = ET.ElementTree(root)
    tree.write('Data/' + str(id) + '.xml')


def manageDataCreate(id):
    root = ET.Element('root')
    self_travelling = ET.SubElement(root, 'self_travelling')
    category_new = ET.SubElement(self_travelling, 'category')
    region_new = ET.SubElement(self_travelling, 'region')
    num_new = ET.SubElement(self_travelling, 'num')
    category_new.text = 'history'
    region_new.text = 'minsk'
    num_new.text = '1'
    tree = ET.ElementTree(root)
    tree.write('Data/' + str(id) + '.xml')


def getCategory(id):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    category_old = root.find('self_travelling').find('category').text
    return category_old


def getRegion(id):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    region_old = root.find('self_travelling').find('region').text
    return region_old


def getNum(id):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    num_old = root.find('self_travelling').find('num').text
    return num_old
