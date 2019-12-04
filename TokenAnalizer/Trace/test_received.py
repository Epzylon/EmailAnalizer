from unittest import TestCase
# From cases could contain or not:
#  from, by, via, with, id, for
wanted_ip = {'ip':'1.2.3.4'}
wanted_ip_others = {'ip':'1.2.3.4', 'others': 'someoption=xxx.xxx.com'}
wanted_ip_port = {'ip':'1.2.3.4', 'port':'999'}
wanted_domain = {'domain': 'xxxx.xxx.com','ip': '', 'port':'', 'others': ''}
wanted_domain_ip = {'domain': 'xxxx.xxx.com','ip': '1.2.3.4', 'port':'', 'others': ''}
wanted_domain_ip_port = {'domain': 'xxxx.xxx.com','ip': '1.2.3.4', 'port':'999', 'others': ''}
wanted_domain_ip_port_other = {'domain': 'xxxx.xxx.com','ip': '1.2.3.4', 'port': '999', 'others': 'something=option'}

from_clauses = [
    {'test': 'from xxx.xxx.com', 'name': 'Simple', 'comment': 'Just from with domain',
     'wanted': wanted_domain},
    {'test': 'from xxx.xxx.com (1.2.3.4)', 'name': 'SimpleIP', 'comment': 'from domain ip',
     'wanted': wanted_domain_ip},
    {'test': 'from xxx.xxx.com (1.2.3.4:999)', 'name': 'SimpleIP:Port', 'comment': 'from domain ip port',
     'wanted': wanted_domain_ip_port},
    {'test': 'from xxx.xxx.com ([1.2.3.4])', 'name': 'Simple[IP]', 'comment': 'from domain ([ip])',
     'wanted': wanted_domain_ip},
    {'test': 'from xxx.xxx.com ([1.2.3.4:999])', 'name': 'Simple[IP:PORT]', 'comment': 'from domain [ip:port]',
     'wanted': wanted_domain_ip_port},
    {'test': 'from xxx.xxx.com (xxx.xxx.com. [1.2.3.4])', 'name': 'Simple(domain[ip])', 'comment': 'from domain (domain [ip])',
     'wanted': wanted_domain_ip_port},
    {'test': 'from xxx.xxx.com (xxx.xxx.com. [1.2.3.4:999])', 'name': 'Simple(FQDN[IP:PORT]', 'comment': 'from domain (fqdn [ip:port])',
     'wanted': wanted_domain_ip_port},
    {'test': 'from [1.2.3.4] ([1.2.3.4])', 'name':'from[ip][ip]', 'comment': 'from [ip] ([ip])',
     'wanted': wanted_domain_ip},
    {'test': 'from [1.2.3.4] ([1.2.3.4:999])', 'name': 'from[ip]([ip:port])', 'comment': 'from [ip] [ip:port]',
     'wanted': wanted_ip_port},
    {'test': 'from [1.2.3.4:999] ([1.2.3.4])', 'name': 'from[ip:port]([ip])', 'comment': 'from [ip:port] ([ip])',
     'wanted': wanted_ip_port},
    {'test': 'from [1.2.3.4:999] ([1.2.3.4:999])', 'name': 'from[ip:port]([ip:port])', 'comment': 'from [ip:port] ([ip:port])',
     'wanted': wanted_domain_ip},
    {'test': 'from [1.2.3.4] (xxx.xxx.com. [1.2.3.4])', 'name': 'from[ip](dom[ip])', 'comment': 'from [ip] (fqdn [ip])',
     'wanted': wanted_domain_ip_port},
    {'test': 'from [1.2.3.4] (xxx.xxx.com. [1.2.3.4:999])', 'name': 'from[ip](dom[ip])', 'comment': 'from [ip] (fqdn [ip:port])',
     'wanted': wanted_domain_ip_port},
    {'test': 'from [1.2.3.4:999] (xxx.xxx.com. [1.2.3.4:999])', 'name': 'from[ip:port](fqdn[ip:port])', 'comment': 'from [ip:port] (fqdn [ip:port])',
     'wanted': wanted_domain_ip_port},
    {'test': 'from [1.2.3.4] ([1.2.3.4] someoption=xxx.xxx.com)', 'name': 'from[ip]([ip]option)', 'comment': 'from [ip] ([ip] option',
     'wanted': wanted_ip_others},
    {'test': 'from [1.2.3.4] ([1.2.3.4:999] someoption=xxx.xxx.com xxx.xxx.com)', 'name': 'from[ip]([ip:port])option', 'comment': 'from [ip] ([ip:port]) option',
     'wanted': wanted_ip_others},
    {'test': 'from [1.2.3.4:999] ([1.2.3.4:999] someoption=xxx.xxx.com xxx.xxx.com)', 'name': 'from[ip:port]([ip:port])option', 'comment': 'from [ip:port] ([ip:port]) option',
     wanted_ip_others}
]

class TestReceived(TestCase):
    def test__parse_rec_string(self):
        self.fail()
