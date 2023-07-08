import os
import zipfile
import xml.etree.ElementTree as ET


def searchinnode(root,path):
    # Найти узел Locations 
    nodeslist = root.findall(path) 
    if nodeslist: 
        for node in nodeslist: 
            # Рекурсивно перебрать все дочерние узлы 
            def recursive_search(node): 
                for child_node in node: 
                    # Если в значении дочернего узла содержится srchtext, вывести его значение
                    if child_node.text is not None:
                        if srchtext.upper() in child_node.text.upper():
                            print(f'**** {zip_file} ****')
                            print(f'{child_node.tag}: ', child_node.text) 
                    recursive_search(child_node)                         
            recursive_search(node)


# Запрос ввода текста
srchtext = input("Введите текст для поиска: ")

search_nodes = ['.//ParentCadastralNumbers','.//PrevCadastralNumbers','.//Clients','.//Locations']

# Получение списка файлов *.zip в текущей директории
zip_files = [f for f in os.listdir('.') if f.endswith('.zip')]

# Поиск файлов с расширением xml внутри zip-архивов
for zip_file in zip_files:
    with zipfile.ZipFile(zip_file, 'r') as zf:
        xml_files = [f for f in zf.namelist() if f.endswith('.xml')]
        
        # Чтение xml-файлов и поиск необходимых узлов
        for xml_file in xml_files:
            with zf.open(xml_file) as f:
                tree = ET.parse(f)
                root = tree.getroot()

                for path in search_nodes:
                    searchinnode(root,path)

input('Press any key')
