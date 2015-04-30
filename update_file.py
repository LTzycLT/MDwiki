import os
import codecs


def gen(s1, s2, s3):
    r = '- [\'' + s1 + '\', \'' + s2 + '\', \'' + s3 + '\']'
    return r
def filter(s):
    for i in range(len(s)):
        if ord(s[i]) >= 128 or (s[i] in [' ', '*', "~"]):
            return 0
    extension = os.path.splitext(s)[1]
    valid_ext = ["", ".cpp", ".java", ".txt", ".py", ".md", ".markdown"]
    if extension not in valid_ext:
        return 0
    return 1

print("site_name: My Docs")
print("pages:")
print("- ['index.md', 'Home']")


init_dir = os.getcwd() + "/docs"

for d1 in os.listdir(init_dir):
    first_dir = init_dir + "/" + d1
    if os.path.isdir(first_dir):
        for d2 in os.listdir(first_dir):
            this_file = first_dir + "/" + d2
            if os.path.isfile(this_file) and filter(d2) and filter(d1):
                print(gen(d1 + "/" + d2, d1, d2))
print("theme: flatly")
