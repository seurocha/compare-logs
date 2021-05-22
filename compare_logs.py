import argparse

parser = argparse.ArgumentParser(
    prog="compare_logs",
    description="Compare log files to identify corret correlation between client and server",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

parser.add_argument(
    "search",
    type=str,
    help="Search keyword",
)

args = parser.parse_args()

client_log = open("client_log.log", "r")
server_log = open("server_log.log", "r")

client_list = [(line.strip()).split() for line in client_log]
server_list = [(line.strip()).split() for line in server_log]

client_log.close()
server_log.close()


def check_client_log():
    matches = []
    with open("filtered_client.log", "w") as f:
        try:
            print("\n\nCLIENT")
            for match in client_list:
                if args.search in match:
                    matches.append(match)
                    print(match)
                    f.write('%s\n' % match)
            
        except:
            print("No results found for your search !!!")

def check_server_log():
    matches = []
    with open("filtered_server.log", "w") as f:
        try:
            print("\n\nSERVER")
            for match in server_list:
                if args.search in match:
                    matches.append(match)
                    print(match)
                    f.write('%s\n' % match)
            
        except:
            print("No results found for your search !!!")

check_client_log()
check_server_log()