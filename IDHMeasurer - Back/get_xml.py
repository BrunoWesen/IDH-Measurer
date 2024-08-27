import requests as re
import xmltodict
from lxml import html, etree

response = re.get(
    "https://sistemas.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?p=13230607179667000738650200000443221230252641|2|1|1|"
    "7394991e4497a229e37d6995c6e464d13dd05179")

print(response.headers)

# htmldoc = html.fromstring(response.content)
# xmldoc = etree.tostring(htmldoc)
# xmldict = xmltodict.parse(xmldoc)
#
# print(xmldict['html']['body']['table']['tr']['td']['div'][1]['div'])