from websockets import ConnectionClosed
from dashboard.notification.models import Notification, Penalty
import asyncio
import datetime
import json
import logging
import uuid
import websockets


# Variables for get_all data from table in RDM
GET_ALL = '/get_all'
GET_ALL_RADAR_DB = 'RADAR'
GET_ALL_NOTIFY_DB = 'NOTIFY'
GET_ALL_INFRACTION_TABLE = 'infraction'
GET_ALL_STATUS_TABLE = 'status'
GET_ALL_FEASIBLE_TABLE = 'feasability'


# RDM WS Server Address
WS_SERVER = 'ws://www.radop.ml:8765'

# RaDop API Server Address
RADOP_API = 'http://www.radop.ml:3333'


def save_notifications(feasible_notifications, infraction_notifications):
    notifications = Notification.objects.all()
    if len(notifications) is 0:
        for item in feasible_notifications:
            obj = Notification(
                notification_type='POSSIVEL',
                crash_feasability=item['crash_feasability'],
                infraction_identifier=item['infraction_id'],
                identifier=item['id']
            )
            obj.save()

        for item in infraction_notifications:
            penalty = Penalty.objects.filter(points=item['penalty']['points'])
            obj = Notification(
                notification_type='INFRACAO',
                allowed_track_speed=item['allowed_track_speed'],
                considered_speed=item['considered_speed'],
                date=item['date'],
                identifier=item['id'],
                infraction_identifier=item['infraction_identifier'],
                read_speed=item['read_speed'],
                time=item['time'],
                vehicle_brand=item['vehicle_brand'],
                vehicle_chassi=item['vehicle_chassi'],
                vehicle_city=item['vehicle_city'],
                vehicle_color=item['vehicle_color'],
                vehicle_model=item['vehicle_model'],
                vehicle_plate=item['vehicle_plate'],
                vehicle_state=item['vehicle_state'],
                vehicle_status=item['vehicle_status'],
                vehicle_year=item['vehicle_year'],
                penalty_id=penalty[0].id
            )
            obj.save()
    else:
        feasible_ids = [a.identifier for a in notifications if a.notification_type == 'POSSIVEL']
        infraction_ids = [a.identifier for a in notifications if a.notification_type == 'INFRACAO']

        feasibles = []
        infractions = []

        for notification in feasible_notifications:
            if not notification['id'] in feasible_ids:
                feasibles.append(notification)

        for notification in infraction_notifications:
            if not notification['id'] in infraction_ids:
                infractions.append(notification)

        for item in feasibles:
            obj = Notification(
                notification_type='POSSIVEL',
                crash_feasability=item['crash_feasability'],
                infraction_identifier=item['infraction_id'],
                identifier=item['id']
            )
            obj.save()

        for item in infractions:
            penalty = Penalty.objects.filter(points=item['penalty']['points'])
            obj = Notification(
                notification_type='INFRACAO',
                allowed_track_speed=item['allowed_track_speed'],
                considered_speed=item['considered_speed'],
                date=item['date'],
                identifier=item['id'],
                infraction_identifier=item['infraction_identifier'],
                read_speed=item['read_speed'],
                time=item['time'],
                vehicle_brand=item['vehicle_brand'],
                vehicle_chassi=item['vehicle_chassi'],
                vehicle_city=item['vehicle_city'],
                vehicle_color=item['vehicle_color'],
                vehicle_model=item['vehicle_model'],
                vehicle_plate=item['vehicle_plate'],
                vehicle_state=item['vehicle_state'],
                vehicle_status=item['vehicle_status'],
                vehicle_year=item['vehicle_year'],
                penalty_id=penalty[0].id
            )
            obj.save()
    return True


async def get_all_infractions():
    try:
        async with websockets.connect(
            f'{WS_SERVER}{GET_ALL}'
        ) as websocket:

            payload = {
                'database': GET_ALL_RADAR_DB,
                'table': GET_ALL_INFRACTION_TABLE
            }

            identifier = str(uuid.uuid4())

            time = datetime.datetime.utcnow()
            time = str(time.isoformat('T'))
            time = time.rsplit('.')[0] + 'Z'

            request = 'rethink-manager-call'

            data = {
                'id': identifier,
                'type': request,
                'payload': payload,
                'time': time
            }

            await websocket.send(json.dumps(data))

            logging.info(f'[INFO] Data sent: {data}')

            response = await asyncio.wait_for(websocket.recv(), timeout=20)

            if response is None:
                raise Exception('No data received from RDM')
            else:
                response = json.loads(response)
                return response
    except (asyncio.TimeoutError, ConnectionRefusedError) as err:
        print(err)
    except ConnectionClosed as err:
        print(err)
    except RuntimeError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        pass


async def get_all_statuses():
    try:
        async with websockets.connect(
            f'{WS_SERVER}{GET_ALL}'
        ) as websocket:

            payload = {
                'database': GET_ALL_RADAR_DB,
                'table': GET_ALL_STATUS_TABLE
            }

            identifier = str(uuid.uuid4())

            time = datetime.datetime.utcnow()
            time = str(time.isoformat('T'))
            time = time.rsplit('.')[0] + 'Z'

            request = 'rethink-manager-call'

            data = {
                'id': identifier,
                'type': request,
                'payload': payload,
                'time': time
            }

            await websocket.send(json.dumps(data))

            logging.info(f'[INFO] Data sent: {data}')

            response = await asyncio.wait_for(websocket.recv(), timeout=20)

            if response is None:
                raise Exception('No data received from RDM')
            else:
                response = json.loads(response)
                return response
    except (asyncio.TimeoutError, ConnectionRefusedError) as err:
        print(err)
    except ConnectionClosed as err:
        print(err)
    except RuntimeError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        pass


async def get_all_infraction_notifications():
    try:
        async with websockets.connect(
            f'{WS_SERVER}{GET_ALL}'
        ) as websocket:

            payload = {
                'database': GET_ALL_NOTIFY_DB,
                'table': GET_ALL_INFRACTION_TABLE
            }

            identifier = str(uuid.uuid4())

            time = datetime.datetime.utcnow()
            time = str(time.isoformat('T'))
            time = time.rsplit('.')[0] + 'Z'

            request = 'rethink-manager-call'

            data = {
                'id': identifier,
                'type': request,
                'payload': payload,
                'time': time
            }

            await websocket.send(json.dumps(data))

            logging.info(f'[INFO] Data sent: {data}')

            response = await asyncio.wait_for(websocket.recv(), timeout=20)

            if response is None:
                raise Exception('No data received from RDM')
            else:
                infraction = json.loads(response)

            return infraction['response_message']

    except (asyncio.TimeoutError, ConnectionRefusedError) as err:
        print(err)
    except ConnectionClosed as err:
        print(err)
    except RuntimeError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        pass


async def get_all_feasible_notifications():
    try:
        async with websockets.connect(
            f'{WS_SERVER}{GET_ALL}'
        ) as websocket:

            payload = {
                'database': GET_ALL_NOTIFY_DB,
                'table': GET_ALL_FEASIBLE_TABLE
            }

            identifier = str(uuid.uuid4())

            time = datetime.datetime.utcnow()
            time = str(time.isoformat('T'))
            time = time.rsplit('.')[0] + 'Z'

            request = 'rethink-manager-call'

            data = {
                'id': identifier,
                'type': request,
                'payload': payload,
                'time': time
            }

            await websocket.send(json.dumps(data))

            logging.info(f'[INFO] Data sent: {data}')

            response = await asyncio.wait_for(websocket.recv(), timeout=20)

            if response is None:
                raise Exception('No data received from RDM')
            else:
                feasible = json.loads(response)

            return feasible['response_message']

    except (asyncio.TimeoutError, ConnectionRefusedError) as err:
        print(err)
    except ConnectionClosed as err:
        print(err)
    except RuntimeError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        pass


def get_websocket_data():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        infractions = loop.run_until_complete(get_all_infractions())
        statuses = loop.run_until_complete(get_all_statuses())
        notify_infraction = loop.run_until_complete(get_all_infraction_notifications())
        notify_feasible = loop.run_until_complete(get_all_feasible_notifications())
        loop.close()
    except (asyncio.TimeoutError, ConnectionRefusedError) as err:
        print(err)
        asyncio.get_event_loop().stop()
    except ConnectionClosed as err:
        print(err)
        asyncio.get_event_loop().stop()
    except RuntimeError as err:
        print(err)
        asyncio.get_event_loop().stop()
    except Exception as err:
        print(err)
        asyncio.get_event_loop().stop()
    else:
        asyncio.get_event_loop().stop()
        save_notifications(notify_feasible, notify_infraction)
        return infractions, statuses, notify_infraction, notify_feasible
