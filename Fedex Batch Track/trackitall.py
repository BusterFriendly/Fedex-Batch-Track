from track import evaluate
import xlrd
import os

def get_list(name, tracking_column):
	dirname, filename = os.path.split(os.path.abspath(__file__))

	name_of_file = dirname + '/'+str(name) + '.xls'

	book = xlrd.open_workbook(name_of_file)
	sheet = book.sheet_by_index(0)
	tracklist = []
	for x in sheet.col_values(tracking_column):
		tracklist.append(x)
		trackingnumber = x
	return tracklist


def evaluate_excel(name, tracking_column,outputfile):

	dirname, filename = os.path.split(os.path.abspath(__file__))

	name_of_file = dirname + '/'+str(name) + '.xls'
	outputfile = str(outputfile)+'.txt'


	book = xlrd.open_workbook(name_of_file)
	sheet = book.sheet_by_index(0)
	tracklist = []
	for x in sheet.col_values(tracking_column):
		tracklist.append(x)
		trackingnumber = x

	with open(outputfile, "wt") as text_file:
		#os.chmod(name, 0600)
		print 'trackingnumber\tShipped\tArrived\tDelivered'

		text_file.write('trackingnumber\tShipped\tArrived\tDelivered\t')

		for x in tracklist:
			y = x
			a,b,c = evaluate(x)
			if a != "":
				text_file.write('\n'+str(y) + "\t" +str(a)+"\t"+str(b) + "\t" + str(c)+'\t')
				print str(y) + "\t" +str(a)+"\t"+str(b) + "\t" + str(c)+'\t'

			else:
				print str(y) + "\t" + 'None'
				text_file.write('\n'+str(y) + "\t" + 'None')
