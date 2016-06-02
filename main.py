import sys
import auth
import testList
import testServer

def main(argv):
  # testList.novaList()
  # testList.glanceList()

  serverName = "will_test"
  testServer.createServer(serverName)
  testServer.deleteServer(serverName)

if __name__ == "__main__":
    main(sys.argv[1:])
