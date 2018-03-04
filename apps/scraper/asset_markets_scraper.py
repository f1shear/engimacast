import logging

import lxml.etree
import requests

ASSET_MARKETS_PAGE = 'https://coinmarketcap.com/currencies/%s/#markets'


def get_page(asset):
    url = ASSET_MARKETS_PAGE % asset
    response = requests.get(url)

    if response.status_code == 200:
        page = response.text
        return page
    raise Exception("CMC unavailable: [%s] %s" % (response.status_code, url))


def get_node(el):
    """ find better way to do this """
    el_html = lxml.etree.tostring(el)
    el_doc = lxml.etree.HTML(el_html)
    return el_doc


def get_text(el, xpath):
    if len(el.xpath(xpath)) > 0:
        return el.xpath(xpath)[0].text
    else:
        return ''


def get_link(el, xpath):
    if len(el.xpath(xpath)) > 0:
        links = el.xpath(xpath)
        for link in links:
            if 'http://' in link or 'https://' in link:
                return link
    return ''


def extract_markets(asset):
    page = get_page(asset)
    doc = lxml.etree.HTML(page)

    # other information for asset

    website = get_link(doc, '//a[contains(text(), "Website")]/@href')
    explorer = get_link(doc, '//a[contains(text(), "Explorer")]/@href')
    coin = get_text(doc, "//span[contains(@class, 'label') and text() = 'Coin']")
    token = get_text(doc, "//span[contains(@class, 'label') and text() = 'Token']")

    extra_info = {
        'website': website,
        'explorer': explorer,
        'asset_type': coin or token
    }

    markets = []

    for el_row in doc.xpath('//table[@id="markets-table"]/tbody/tr'):

        row_doc = get_node(el_row)

        row = []
        for index, el_cell in enumerate(row_doc.xpath('//td')):
            cell_doc = get_node(el_cell)
            value = ''
            if index == 1 or index == 2:
                value = get_text(cell_doc, '//a')
            elif index == 0 or index == 6:
                value = get_text(cell_doc, '//td')
            else:
                value = get_text(cell_doc, '//span')
            row.append(value.strip())
        market = {
            'name': row[1],
            'pair': row[2],
            'volume_usd': row[3],
            'price': row[4],
            'volume_percent': row[5],
            'updated': row[6]
        }
        markets.append(market)
    return extra_info, markets


if __name__ == '__main__':
    rows = extract_markets('bitcoin')
    for item in rows:
        logging.error(item)

    rows = extract_markets('ethereum')
    for item in rows:
        logging.error(item)
