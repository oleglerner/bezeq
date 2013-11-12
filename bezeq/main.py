#from Html_parser import Html_parser
from web_surfing import web_surfing

my_web = web_surfing()

#my_web.get_next_page("https://mybill.kvish6.co.il/Login.do")
my_web.get_next_page("https://my.bezeq.co.il/default.aspx")

#my_web.login(["racheli10","511247298","meravz53"])
my_web.login(["ophir159", "tours15"])