import json
import os
import logging
from qbits.annotations import catch
from qbits.places import Places
from qbits.publisher import Publisher
from decimalencoder import DecimalEncoder

db_places = Places()
publisher = Publisher()

logger = logging.getLogger()


def function_handler(event, context):
    for record in event.get('Records', []):
        body = record.get('body', None) or None
        print(body)
        sale = json.loads(body)
        if sale is not None:
            request_assigment(sale)


@catch
def request_assigment(order):
    address = order.get('address', None)
    place = order.get('place', None)
    customer = order.get('customer', None)
    delivery_id = order.get('deliveryId', 'delivery-service')
    if address is not None and place is not None and customer is not None and delivery_id == 'delivery-service':
        geolocation_place = place.get('geolocation', None)
        geolocation_customer = address.get('geolocation', None)
        if geolocation_customer is not None and geolocation_place is not None:
            origin_order_type = customer.get('originOrderType', None)
            email = customer.get('originOrderType', None)
            jid = customer.get('jid', None)
            notification = {
                "externalId": order.get('placeId'),
                "transactionId": order.get('transactionId'),
                "transNum": order.get('folio'),
                "startLat": geolocation_place.get('latitude'),
                "startLng": geolocation_place.get('longitude'),
                "destinationLat": geolocation_customer.get('latitude'),
                "destinationLng": geolocation_customer.get('longitude'),
                "jid": jid if origin_order_type != 'StoreWeb' else None,
                "orderPaid": order.get('statusPayment') == 'complete',
                "clientName": customer.get('name', None),
                "email": email if origin_order_type == 'StoreWeb' else None,
                "additionalPlacesIdList": db_places.get_external_places(order.get('placeId')),
                "manualAssignment": db_places.get_manual_assignment(order.get('placeId')),
                "webhookUrl": os.environ['WEBHOOK_URL'],
                "place": place,
            }
            print(json.dumps(notification, cls=DecimalEncoder))
            publisher.to_sqs_webhook(notification)
    else:
        logger.error("Datos incompletos para notificar a rutas")
