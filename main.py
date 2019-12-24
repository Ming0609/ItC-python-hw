from crawler import Crawler
from args import get_args
import csv
import time

if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    contents = crawler.crawl(args.start_date, args.end_date)
    with open(args.output,'w') as f:
        for date,title,content in contents:
            output_str = f'{str(date)},"{title}","{content}"\n'
            f.write(output_str)
