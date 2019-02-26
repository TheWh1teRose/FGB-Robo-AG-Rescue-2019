import logging
import time
import datetime
import ModellTests

def main():
    #inital stuff
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
    logging.basicConfig(filename='flightlogs/flightlog'+st+'.log',level=logging.DEBUG, format='%(asctime)s; %(levelname)s; %(message)s', datefmt='%m/%d/%Y %I:%M:%S')

    #loding for tests
    ModellTests.start()

if __name__ == '__main__':
    main()
