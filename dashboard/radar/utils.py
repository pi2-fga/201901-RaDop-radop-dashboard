from websockets import ConnectionClosed

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


async def get_all_notifications():
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

            data = {
                'infraction': infraction['response_message'],
                'feasible': feasible['response_message']
            }

            return data
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
        infractions = {} # loop.run_until_complete(get_all_infractions())
        statuses = loop.run_until_complete(get_all_statuses())
        notifications = loop.run_until_complete(get_all_notifications())
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
        return infractions, statuses, notifications
