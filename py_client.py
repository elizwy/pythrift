# _*_ coding:utf-8 _*_

from Person import PersonService
from Person import ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

try:
    tSocket = TSocket.TSocket("localhost", 8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)

    transport.open()
    person = client.getPersonByUserName("zwy")
    print(person.username)
    print(person.age)
    print(person.married)

    print("--------------")
    newPerson = ttypes.Person()
    newPerson.username = "zcc"
    newPerson.age = 26
    newPerson.married = False

    client.savePerson(newPerson)
    transport.close()

except Thrift.TException as tx:
    print('%s' % tx.message)
