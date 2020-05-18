from thrift import Thrift
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport

from Person import PersonService
from PersonServiceImpl import PersonServiceImpl

try:
    peronServerHandler = PersonServiceImpl()
    processor = PersonService.Processor(peronServerHandler)

    serverSocket = TSocket.TServerSocket(port=8899)
    transportFactor = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TSimpleServer(processor, serverSocket,transportFactor,protocolFactory)
    server.serve()

except Thrift.TException as ex:
    print(ex.message)
