import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from typing import List


class XmlHandler:
    @staticmethod
    def xml_to_string(xml_element: Element) -> str:
        """Перетворює XML-об'єкт в рядок."""
        return ET.tostring(xml_element, encoding="unicode")

    @staticmethod
    def string_to_xml(string_xml: str) -> Element:
        """Перетворює рядок назад в XML-об'єкт."""
        return ET.fromstring(string_xml)

    @staticmethod
    def find_elements(xml_element: Element, tag: str) -> List[Element]:
        """Знаходить всі елементи за заданим тегом."""
        return xml_element.findall(tag)

    @staticmethod
    def add_element(parent: Element, tag: str, text: str) -> None:
        """Додає новий елемент до вказаного батьківського елемента."""
        new_element = ET.Element(tag)
        new_element.text = text
        parent.append(new_element)

    @staticmethod
    def remove_element(parent: Element, tag: str) -> None:
        """Видаляє елемент за заданим тегом."""
        for element in parent.findall(tag):
            parent.remove(element)


# Приклад використання
handler = XmlHandler()

sample_xml = ET.Element("Root")
sample_xml.text = "Це приклад XML"

xml_string_example = handler.xml_to_string(sample_xml)
print(f"XML у рядок: {xml_string_example}")

restored_xml = handler.string_to_xml(xml_string_example)
print(f"Відновлений XML: {ET.tostring(restored_xml, encoding='unicode')}")

handler.add_element(restored_xml, "Child", "Це дочірній елемент")
print(f"Змінений XML: {ET.tostring(restored_xml, encoding='unicode')}")

found_elements = handler.find_elements(restored_xml, "Child")
for elem in found_elements:
    print(f"Знайдений елемент: {ET.tostring(elem, encoding='unicode')}")

handler.remove_element(restored_xml, "Child")
print(f"XML після видалення елемента: {ET.tostring(restored_xml, encoding='unicode')}")
