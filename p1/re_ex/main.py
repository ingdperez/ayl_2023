import re


def bookshelf():
    with open(r"bookshelf.txt", "r") as f:
        string = f.read()
        print(string, end="\n\n\n")

        pattern_matching = r".+?;(.+p);.+?"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        pattern_matching = r".+? (B.+?);.+;.+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        pattern_matching = r"^.+?;(.+?);19[89]\d$"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # # Books with name length lower than 25
        # pattern_matching = r"^.+?;(.{1,25}?);.+?$"
        # result = re.findall(pattern_matching, string, re.M)
        # for name in result:
        #     print(name)
        #
        # pattern_matching = r"^(.+?);.+?;20\d\d?$"
        # result = re.findall(pattern_matching, string, re.M)
        # for name in result:
        #     print(name)


def phone():
    with open(r"phone.txt", "r") as f:
        string = f.read()
        print(string, end="\n\n\n")
        # last name for code area ending with 0
        pattern_matching = r".+ (.+)\t\(\d\d0\)\s(.+)"
        result = re.findall(pattern_matching, string, re.M)
        print(result)
        # last name for code area for number ending with 7
        pattern_matching = r".+\t\((\d{3})\)\s.{7}7"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern that will match all the persons (first and last name)
        # in the file whose phone number starts with an odd digit (1, 3, 5, 7, 9).
        pattern_matching = r"(.+)\t\(\d{3}\)\s[13579]\d{2}-\d{4}"
        # pattern_matching = r"(.+)\t\(\d{3}\) [13579].{7}"
        result = re.findall(pattern_matching, string, re.M)
        print(result)
        # Write a pattern that will match all the persons (first name only) in
        # the file whose area code is a number less than 300.
        pattern_matching = r"(.+) .+\t\([0-2]\d\d\)\s.+"
        # pattern_matching = r"(.+) .+\t\([0-2]\d\d\) .{8}"
        result = re.findall(pattern_matching, string, re.M)
        print(result)
        # Write a pattern that will match all the persons (first name only) in
        # the file whose last name ends in a vowel (aeiou) and phone number ends in either 0, 7 or 9.
        pattern_matching = r"(.+) .+[aeiou]\t\(\d+\)\s\d+-\d{3}[079]"
        pattern_matching = r"(.+) .+[aeiou]\t\(\d{3}\) .{7}[079]"
        result = re.findall(pattern_matching, string, re.M)
        print(result)


def log():
    with open(r"logs.txt", "r") as f:
        string = f.read()
        print(string, end="\n\n\n")
        # last name for code area ending with 0
        pattern_matching = r"Critical 1/1[1-6]/2020 .+ [A-Z]{2} (.+?) \d+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern that will match the Source substring of all the log entries that were
        # generated after 12 PM and before 4 PM, regardless of the severity
        # level and the date
        pattern_matching = r".+ .+/.+/.+ (?:(?:12|1|2|3):.+) PM (.+?) \d+"
        # pattern_matching = r".+/2020 (?:12|[1-3]):\d\d:\d\d PM (.+?) \d+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern that will match the Date of all the log entries that have TPM as the
        # Source of the log message.
        pattern_matching = r".+ (.+) .+ [A-Z]{2} TPM \d+"
        # pattern_matching = r".+ (.+?) \d+:\d+:\d+ [A-Z]{2} TPM \d+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern, that will match the Date and Time of all the log entries that have been generated between
        # 24 and 27 of January 2020 and between 8:00:00 and 8:59:59 AM.
        pattern_matching = r".+ (1/2[4567]/2020 8:\d{2}:\d{2}) [A-Z]{2} .+? \d+"
        # pattern_matching = r".+ (1/2[4-7]/2020 8:\d+:\d+) "
        result = re.findall(pattern_matching, string, re.M)
        print(result)


def url():
    with open(r"web.txt", "r") as f:
        string = f.read()
        print(string, end="\n\n\n")
        # last name for code area ending with 0
        pattern_matching = r".+\s+(http.*://.+\.\w{2,})\s.+Online shopping.+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern on line 7, in between the double quotes, that will
        # match the Site name (e.g. Google, Facebook etc.) of all the websites
        # in the file that are based in China and have a 3-letter URL extension
        # (e.g. .com, .org etc.).
        pattern_matching = r"(.+)\s+http.*://.+\.\w{3}\s.+China"
        # pattern_matching = r"(.+)\s+http.*://.+\.\w{3}\s.+China.+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern on line 7, in between the double quotes, that will
        # match the URL and country of all the Social networking websites in
        # the file whose domain name (excluding the extension) is less than 5
        # characters long
        pattern_matching = r".+\s+(http.*://.{1,4}\.\w{2,})\s.+Social networking\t(.+) .+"
        # pattern_matching = r".+\s+(http.*://.{1,4}\.\w{2,})\s.+Social networking\s(.+?)\s.+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)

        # Write a pattern on line 7, in between the double quotes, that will
        # match the Site name (e.g. Google, Facebook etc.) and the web
        # protocol of all the websites whose URLs contain subdomains (e.g.
        # http://something.website.abc).
        pattern_matching = r"(.+)\s+(http.*)://.+\.\w+\.\w{2,}\s.+"
        # pattern_matching = r"(.+)\s+(http.*)://.+\..+\.\w{2,}\s.+"
        result = re.findall(pattern_matching, string, re.M)
        print(result)


if __name__ == '__main__':
    # bookshelf()
    # phone()
    # log()
    url()

