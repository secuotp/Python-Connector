from com.secuotp.model.xml import XMLTag as moduleList

__author__ = 'zenology'

a = moduleList.XMLTag("secuotp", None)

a.add_child_value("a", "20")
good_tag = a.add_child_tag("good")
good_tag.add_child_value("w", "30")

print(a.get_child_tag(1).get_child_tag(0).value)