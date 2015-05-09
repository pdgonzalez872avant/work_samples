import numpy as np
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import xhtml2pdf
from xhtml2pdf import pisa
import StringIO
import weasyprint


print "Haha\n"

df = pd.read_csv(r"C:\Users\Paulo\PycharmProjects\work_samples\reporting_samples\example_data.csv")

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("my_report.html")

template_vars = {"title": "Sales Funnel Report - National",
                 "national_pivot_table": df.to_html()}

html_out = template.render(template_vars)

pdf_name = r"C:\Users\Paulo\PycharmProjects\work_samples\reporting_samples\pdf_created.pdf"


# pdf = StringIO(html_out)
#
# print(pdf)

# pisa.CreatePDF(StringIO(html_out), pdf)


# x = xhtml2pdf.document(html_out, pdf_name)

# pisa.CreatePDF(html_out)

# print df.head()

