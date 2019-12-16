from crawler import Crawler
from args import get_args


if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    content = crawler.crawl(2019-11-10,2019-12-10 )
#    content = crawler.crawl(args.start_date, args.end_date)
    # TODO: write content to file according to spec