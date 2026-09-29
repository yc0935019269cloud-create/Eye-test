import base64, pathlib
root = pathlib.Path(__file__).parent
s = (root/'src/template.html').read_text()
for f in ['spec60','sag_bot','sag_top','topview','lateral']:
    s = s.replace('{{%s}}' % f, base64.b64encode((root/f'src/img/{f}.jpg').read_bytes()).decode())
(root/'artifact.html').write_text(s)
head = '<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
i = s.index('<div class="wrap">')
(root/'index.html').write_text(head + s[:i] + '</head>\n<body>\n' + s[i:] + '\n</body>\n</html>\n')
print('built', len(s)//1024, 'KB')
