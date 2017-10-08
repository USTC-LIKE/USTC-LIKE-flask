from jinja2 import Environment  
from jinja2 import FileSystemLoader
import jinja2
  
env = Environment(loader=jinja2.PackageLoader('/path/to/templates', 'utf-8'))  
template = env.get_template('mytemplate.html')  
template.render(the='variables', go='here')  
