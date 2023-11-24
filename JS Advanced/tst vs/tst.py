import re

pattern = r'[a-zA-z0-9_]+'
username_valid = re.findall(pattern, 'mirai123M')