import asyncio

from loguru import logger
from synapse_p2p import Server

from bitcoin_node_crawler.crawler import Crawler

DNS_SEEDS = [
    ("amsterdam.firo.org", 53),
    ("japan.firo.org", 53),
]

server = Server()
crawler = Crawler()


@server.background(60 * 60)
async def get_dns_hosts():
    """
    Check for new DNS hosts every hour
    """
    await crawler.get_dns_hosts(DNS_SEEDS)


@server.background(60)
async def report_total_hosts():
    """
    Reports number of hosts every 60s
    """
    logger.info(f"Total hosts: {len(crawler.all_hosts)}")
    await asyncio.sleep(0)


server.run()
