# 405 error fixed, route wasn't accepting any url methods
# fixed by adding 'methods = ['GET', 'POST']' to route parameters
# fixed View function did not return a response error
# fixed by replacing print with return on line 21
from flask import Flask, request, render_template
import csv

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def input():
    # set an empty list for our csv to fill
    dataType = []
    dataValue = []
    # open csv file
    with open('lines.csv', 'rt') as csvfile:
        # fieldnames = ['item']
        # each row read from ths csv is returned as a list of strings
        fieldnames = ['Month', 'commits']
        readInfo = csv.DictReader(csvfile, fieldnames=fieldnames)
        # add a row
        for row in readInfo:
            dataType.append(row['Month'])
            dataValue.append(row['commits'])

    return render_template('output3.html', dataType=dataType, dataValue=dataValue)


# else:
# 	return ('ERROR')
#  experimental

# @app.route('/display', methods = ['GET', 'POST'])
# def display_csv():
#     with open(data, 'rb') as csvfile:
# 			fieldnames = ['item', 'value']
# 			readInfo = csv.DictReader(csvfile, fieldnames=fieldnames)
# 			for row in readInfo:
# 				return (row['item'], row['value'])
# 	else:
# 		return ('ERROR')

if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0')
