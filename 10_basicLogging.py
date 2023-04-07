"""##Levels of Logging ##
The default level is WARNING

1. DEBUG: Detailed information, typically of interest only when diagnosing problems.

2. INFO : Confirmation that things are working as expected.

3. WARNING : An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

4. ERROR : Due to a more serious problem, the software has not been able to perform some function.

5. CRITICAL : A serious error, indicating that the program itself may be unable to continue running.

Ex:
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

OR
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

OR:
import logging

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
######

https://docs.python.org/3/howto/logging.html
"""
import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')