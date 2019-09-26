import os, re, sys

header = '''
[appendix]
== Command reference
'''

lib = sys.argv[1]

def get_jar(pattern):
  cmd = "find {} -print | grep '{}'".format(lib, pattern)
  s = os.popen(cmd).read().splitlines()
  if len(s) != 1:
    print('ERROR: '+pattern+' did not have a unique match')
    print('> '+cmd)
    print('\n'.join(s))
    sys.exit(1)
  return s[0]

fjar = get_jar('fjage')

def get_shell_extensions(jar):
  cmd = "jar -tf {} | grep ShellExt.class | sed 's/\.class$//' | sed 's/\//./g'".format(jar)
  return os.popen(cmd).read().splitlines()

def get_doc(cp, clazz):
  cmd = "groovy -cp {} -e 'println {}.__doc__;'".format(':'.join(cp), clazz)
  return os.popen(cmd).read().splitlines()

def doc_to_adoc(clazz, doc, name):
  out = []
  out.append('=== '+name+' commands')
  brk = True
  for s in doc:
    if brk and s != '':
      out.append('')
    m1 = re.match(r'^(#+) +([^ ]+) \- (.*)$', s)
    m2 = re.match(r'^(#*) *(.+):$', s)
    if m1:
      s = '`' + m1.group(2) + '` -- ' + m1.group(3)
      if len(m1.group(1)) > 1:
        s = '- '+s
      else:
        s = '*'+s+'*'
        out.append("'''\n")
      brk = True
    elif m2:
      s = m2.group(2)+':'
      if len(m2.group(1)) > 0:
        s = '*'+s+'*'
      brk = True
    else:
      brk = False
    out.append(s)
  return '\n'.join(out)

def mkname(clazz):
  m = re.match(r'^.*\.([^\.]+)ShellExt$', clazz)
  if m:
    return m.group(1)
  return clazz

def process(jar, exts=None, name=None):
  if exts is None:
    exts = get_shell_extensions(jar)
  for ext in exts:
    doc = get_doc([jar, fjar], ext)
    print(doc_to_adoc(ext, doc, mkname(ext) if name is None else name))

print(header)
process(fjar, ['org.arl.fjage.shell.ShellDoc'], name='fjåge')
process(get_jar('unet-framework'))
process(get_jar('unet-basic'))
process(get_jar('unet-premium'))
process(get_jar('unet-yoda'), name='Unet audio')
