import random
import re
import sys
import urllib.parse

base_url = 'https://img.shields.io/badge/'

styles = ['plastic', 'flat', 'flat-square', 'for-the-badge', 'social']
links = ['http://kimballleavitt.com', 'https://www.linkedin.com/in/kimballleavitt/', 'https://twitter.com/kimballleavitt', 'https://github.com/byu-imaal/dohjs',
'https://stackoverflow.com/users/9638991/kimbo', 'https://kimballleavitt.com/odd-go/', 'https://kimballleavitt.com/running/', 'https://github.com/kimbo/spoofer',
'https://github.com/kimbo/bluesnarfer', 'https://github.com/kimbo/l2ping-flood', 'https://github.com/kimbo/emo', 'https://github.com/kimbo/vim-python']

# lines starting with these special characters will not be shielderized...
# UNLESS you change it to something like:
# special = []
special = ['#', '-', '<', '[', '!']

def r_color():
    return '{:06x}'.format(random.randint(0, 0xffffff))

def r_style():
    return random.choice(styles)

def r_style_not_social():
    s = styles[:]
    s.remove('social')
    return random.choice(s)

def r_link():
    return random.choice(links)

def r_shield(first_part, second_part):
    params = {}
    f_p = urllib.parse.quote(first_part)
    if second_part is None:
        params['style'] = r_style_not_social() # social looks strange without both parts
        s_p = ''
    else:
        params['style'] = r_style()
        params['labelColor'] = r_color()
        s_p = '-' + urllib.parse.quote(second_part)
    encoded_params = urllib.parse.urlencode(params)
    return '{}{}{}-{}?{}'.format(base_url, f_p, s_p, r_color(), encoded_params)

def segment_generator(text):
    html_fmt = '<img src="{}" alt="shield">'
    mkdwn_fmt = '![]({})'
    lines = text.splitlines(True)
    code_block = False
    html_depth = 0
    fmt = mkdwn_fmt
    for line in lines:
        if len(line) == 0:
            continue
        if len(line.strip()) == 0:
            yield '\n', None
            continue
        if line[:3] == '```':
            code_block = not code_block
            if not code_block:
                yield line, None
                continue
        if code_block:
            yield line, None
            continue
        if line[:2] == '</':
            html_depth -= 1
        elif line[0] == '<':
            html_depth += 1
        if line.strip()[0] in special:
            yield line, None
            continue
        i = 0
        if html_depth > 0:
            fmt = html_fmt
        else:
            fmt = mkdwn_fmt
        split = line.split()
        while True:
            if i >= len(split):
                break
            n = random.randrange(1, 7)
            if i + n >= len(split):
                yield split[i:], fmt
                break
            yield split[i:i+n], fmt
            i += n
        yield '\n', None
    return

def shielderize(text):
    output = []
    for text_segment, format_str in segment_generator(text):
        if isinstance(text_segment, str):
            output.append(text_segment)
            continue
        if len(text_segment) == 0:
            break
        if len(text_segment) == 1:
            badge = r_shield(text_segment[0], None)
            output.append(format_str.format(badge))
            continue
        msg_len = random.randrange(1, len(text_segment) + 1)
        label_len = len(text_segment) - msg_len
        msg = ' '.join(text_segment[:msg_len])
        label = None if label_len == 0 else ' '.join(text_segment[msg_len:])
        badge = r_shield(msg, label)
        output.append(format_str.format(badge))
    return ' '.join(output)

def main():

    with open(sys.argv[1], 'r') if len(sys.argv) == 2 else sys.stdin as fp:
        text = fp.read()

    print(shielderize(text))

if __name__ == '__main__':
    main()