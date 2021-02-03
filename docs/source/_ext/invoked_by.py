import os, re, collections, pprint, shutil

# path = os.path.abspath('../application/public/javascripts')
path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '../../../../application/public/javascripts')

read_invokes = False
read_function_name = False
has_invoked_by = False
has_at = False
temp_array = []
invoked_by_dict = collections.defaultdict(list)
function = []

for file in os.scandir(path):
  if (file.name.endswith('.js')) and ("min" not in file.name) and ("temp" not in file.name):
    with open(file, 'r') as js:
      for line_no, line in enumerate(js):
        
        if read_invokes:
          read_invokes = False
          read_function_name = True
          for func in line.split():
            if ":func:" in func:
              temp_array.append(func.split('`')[1])
              
        elif read_function_name and (") => {" in line or "= function" in line):
          function_name = line.split()[0]

          function.append({
            'function_name': function_name,
            'line_number': (has_at - 1) if has_at else ((line_no - 1) if (line_no - 1) >= 0 else 0),
            'file_name': file.name,
            'has_invoked_by': has_invoked_by
            })

          for invokation in temp_array:
            invoked_by_dict[invokation].append(function_name)
          temp_array = []
          read_function_name = False
          has_invoked_by = False
          has_at = False

        elif "Invokes" in line:
          read_invokes = True
        elif "Invoked by" in line:
          has_invoked_by = True
        elif "@" in line and not has_at:
          has_at = line_no
        elif line.strip() == "/**":
          read_function_name = True

skip_this = False

for file in os.scandir(path):
  if (file.name.endswith('.js')) and ("min" not in file.name) and ("temp" not in file.name):
    with open(file, 'r') as js:
      with open('temp.js', 'w') as output:
        for line_no, line in enumerate(js):
          
          if function and line_no == function[0]['line_number'] and file.name == function[0]['file_name']:

            if function[0]['function_name'] in invoked_by_dict:

              if function[0]['has_invoked_by']:
                new_line = " * | **Invoked by**\n * |"
              else:
                new_line = " *\n * | **Invoked by**\n * |"

              for invoked_func in invoked_by_dict[function[0]['function_name']]:
                new_line += " :func:`" + invoked_func + "`"
              output.write(new_line + "\n")

            function.pop(0)

          if "Invoked by" in line:
            skip_this = True
            continue
          elif skip_this:
            skip_this = False
            continue

          output.write(line)

    shutil.move(path + '/' + file.name, path + '/archive/' + file.name)
    shutil.move('temp.js', path + '/' + file.name)


def setup(app):

    return {
        'version': '0.1',
        'parallel_read_safe': False,
        'parallel_write_safe': False,
    }