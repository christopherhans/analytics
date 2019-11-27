# import libraries.
import os
import sys
from optparse import OptionParser
from analytics_project import analytics_run

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--inventory", help="path to csv file", action="store", dest="inventory")
    parser.add_option("-s", "--scope", help="columns", action="append", dest="scope")
    parser.add_option("-y", "--result", help="column you want to predict", action="store", dest="result")
    parser.add_option("-k", "--knn", help="k nearest neighbor", action="store", dest="knn")
    parser.add_option("-l", "--linear_regression", help="linear regression", action="store", dest="lr")
    parser.add_option("-d", "--debug", help="enable debug", action="store_true", dest="debug", default=False)
    parser.add_option("-r", "--report", help="enable report", action="store_true", dest="report", default=False)
    parser.add_option("-S", "--scaled", help="use scaled values", action="store_true", dest="scaled", default=False)
    parser.add_option("-D", "--drop_first", help="drop first one hot encoding", action="store_true", dest="drop", default=False)
    (options, args) = parser.parse_args()

    if options.inventory:
        os.environ['INVENTORY'] = options.inventory
    if options.result:
        os.environ['RESULT'] = options.result
    if options.knn:
        os.environ['KNN'] = options.knn
    if options.lr:
        os.environ['LINEAR_REGRESSION'] = options.lr
    if options.debug:
        os.environ['DEBUG'] = '1'
    else:
        os.environ['DEBUG'] = '0'
    if options.report:
        os.environ['REPORT'] = '1'
    else:
        os.environ['REPORT'] = '0'
    if options.scaled:
        os.environ['SCALED'] = '1'
    else:
        os.environ['SCALED'] = '0'
    if options.drop:
        os.environ['DROP'] = '1'
    else:
        os.environ['DROP'] = '0'

    if "INVENTORY" not in os.environ and not options.inventory:
        print('Cannot start, please specify inventory with -i')
        sys.exit(0)

    if "RESULT" not in os.environ and not options.result:
        print('Cannot start, please specify target y/f(x) with -y')
        sys.exit(0)

    if options.scope:
        analytics_run(options.scope)
    else:
        analytics_run()
