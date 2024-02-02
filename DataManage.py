import xml.etree.ElementTree as ET

from constants import category_tag, regions_tag, organized_category_tag, organized_extra_tag


def manageDataCategory(id, category):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    root.find('self_travelling').find('category').text = category
    tree.write('Data/' + str(id) + '.xml')


def manageDataRegion(id, region):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    root.find('self_travelling').find('region').text = region
    tree.write('Data/' + str(id) + '.xml')


def manageDataNum(id, num):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    root.find('self_travelling').find('num').text = num
    tree.write('Data/' + str(id) + '.xml')


def manageDataCategoryOrg(id, category):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    root.find('org_travelling').find('category').text = category
    tree.write('Data/' + str(id) + '.xml')


def manageDataExtra(id, extra):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    root.find('org_travelling').find('extra').text = extra
    tree.write('Data/' + str(id) + '.xml')


def manageDataNumOrg(id, num):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    root.find('org_travelling').find('num').text = num
    tree.write('Data/' + str(id) + '.xml')


def manageDataCreate(id):
    root = ET.Element('root')
    self_travelling = ET.SubElement(root, 'self_travelling')
    org_travelling = ET.SubElement(root, 'org_travelling')

    category_new = ET.SubElement(self_travelling, 'category')
    region_new = ET.SubElement(self_travelling, 'region')
    num_new = ET.SubElement(self_travelling, 'num')

    org_category_new = ET.SubElement(org_travelling, 'category')
    org_extra_new = ET.SubElement(org_travelling, 'extra')
    org_num_new = ET.SubElement(org_travelling, 'num')

    category_new.text = category_tag[0]
    region_new.text = regions_tag[0]
    num_new.text = '1'

    org_category_new.text = organized_category_tag[0]
    org_extra_new.text = organized_extra_tag[0]
    org_num_new.text = '1'

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


def getCategoryOrg(id):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    category_old = root.find('org_travelling').find('category').text
    return category_old


def getExtra(id):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    region_old = root.find('org_travelling').find('extra').text
    return region_old


def getNumOrg(id):
    tree = ET.ElementTree(file='Data/' + str(id) + '.xml')
    root = tree.getroot()
    num_old = root.find('org_travelling').find('num').text
    return num_old
