import requests
import json

daysdict = {1:31,2:28,3:31,4:31,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def days_in_month(month):
    for key, value in daysdict.iteritems():
        if key == month:
            number_of_days = value
    return number_of_days




def build_output(tracking_number):

    data = requests.post('https://www.fedex.com/trackingCal/track', data={
        'data': json.dumps({
            'TrackPackagesRequest': {
                'appType': 'wtrk',
                'uniqueKey': '',
                'processingParameters': {
                    'anonymousTransaction': True,
                    'clientId': 'WTRK',
                    'returnDetailedErrors': True,
                    'returnLocalizedDateTime': False
                },
                'trackingInfoList': [{
                    'trackNumberInfo': {
                        'trackingNumber': tracking_number,
                        'trackingQualifier': '',
                        'trackingCarrier': ''
                    }
                }]
            }
        }),
        'action': 'trackpackages',
        'locale': 'en_US',
        'format': 'json',
        'version': 99
    }).json()

    return data

# finds delivery date info

ship_arrival_key = 'displayActDeliveryDateTime'
ship_time_key = 'displayShipDt'
total_weight_key =  'displayTotalLbsWgt'


def track(tracking_number):
    total_weight_value = 0

    data = build_output(tracking_number)
     #narrowing down dictionary and lists to objects needed (ship day,arrival)
    #SHIPMENT SUMMARY
    for key, value in data.iteritems():
        stage_1 = value

    for key, value in stage_1.iteritems():
        if key == 'packageList':
            pkg = value
            status = True
            pkg = pkg[0]
    
    if status:
        return pkg
    else:
        return False

    

def evaluate(pkg, delivered = False):
    if pkg:
        pkg = track(pkg)
        for key, value in pkg.iteritems():
            if key == 'displayShipDt':
                ship_date = value
            elif key == 'displayEstDeliveryDt':
                estimated_delivery = value
            elif key == 'displayActDeliveryDt':
                actual_delivery = value
        if actual_delivery != "":
            delivered = True
        if estimated_delivery == "":
            return ship_date, actual_delivery, delivered
        elif actual_delivery == "":
            return ship_date, estimated_delivery, delivered

    else:
        return 'None'

def print_evaluate(pkg):
    pkg = track(pkg)
    for key, value in pkg.iteritems():
        if key == 'displayShipDt':
            ship_date = value
        elif key == 'displayEstDeliveryDt':
            estimated_delivery = value
        elif key == 'displayActDeliveryDt':
            actual_delivery = value

    dicta = {}
    if estimated_delivery != '':
        dicta.update({'Estimated Delivery':estimated_delivery})
        est = True

    if ship_date !='':
        dicta.update({'Ship Date':ship_date})
        ship = True
    
    if actual_delivery != '':
        act = True 
        dicta.update({'Actual Delivery':actual_delivery})
    return dicta







#print evaluate(499552081013948)
#print evaluate(3016898791)  