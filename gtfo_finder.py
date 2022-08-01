#! /bin/python
import sys
from lxml import html
import requests
import argparse


def main(txt_file):

    Bins_all = []
	ok_status = []
    all_status = []

    try:
        with open(txt_file, "r") as bins:
            for lines in bins.readlines():
                b = lines.split(' ')[-1].split('/')[-1].strip('\n')
                Bins_all.append(b)

        
    except Exception:
        print(FileNotFoundError)
        sys.exit()



    for bins in Bins_all:

        try:
            status = requests.get(f"https://gtfobins.github.io/gtfobins/{bins}/")
            site_content = status.text
            site_content = html.document_fromstring(site_content)
            id = [e.text_content() for e in site_content.xpath("//h2[@id = 'suid']")]
            all_status.append(status)

            if status.status_code == 200 and len(id) > 0:
                ok_status.append(bins)

        except Exception:
            print("Unexpected issue, try again")
            sys.exit()


    if len(ok_status) >0:
        print("[+] Following Bins are available, Check GTFObins for exploitations [+]")
        for b in ok_status:
            print(f'> {b}')
    else:
        print("[-] No matching bins found [-]")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=print(main.__doc__))
    parser.add_argument('-f', type=str, required=True, metavar='string_value')
    args = parser.parse_args()
    bin_file = args.f
    if bin_file.endswith('.txt'):
        main(bin_file)
    else:
        print("Script accepts only .txt files")