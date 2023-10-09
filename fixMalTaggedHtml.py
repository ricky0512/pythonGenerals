# fix NOT closed html tags by lists
# 修復非標準的、未關閉的 html 標籤格式
def replaceMultiple(input_string, replacements):
    for old, new in replacements:
        input_string = input_string.replace(old, new)
    return input_string

replacements = [
    ('</div><td field=', '</div></td><td field='),
    ('</div><tr id=row', '</div></td></tr><tr id=row'),
    ('</table></div><div class=footer', '</td></tr></tbody></table></div><div class=footer')
]

result = replaceMultiple(file_contents, replacements)
