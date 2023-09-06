import re

with open("file.html", "r") as i:
    test_str = "".join(i.readlines())
    regex = r"<tr>.*\n.*<td>(?P<Company>.*)</td>\n.*<td>(?P<Contact>.*)</td>.*\n.*<td>(?P<Country>.*)</td>"
    matches = re.finditer(regex, test_str)

    with open("output_file_path.csv", "w") as o:
        for m in matches:
            d = m.groupdict()
            o.write(f"{d['Company']},{d['Contact']},{d['Country']}\n")
