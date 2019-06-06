from websockets import ConnectionClosed

import asyncio
import datetime
import json
import logging
import uuid
import websockets


# Variables for get_all data from table in RDM
GET_ALL = '/get_all'
GET_ALL_DB = 'RADAR'
GET_ALL_INFRACTION_TABLE = 'infraction'


# RDM WS Server Address
WS_SERVER = 'ws://www.radop.ml:8765'


async def get_all():
    try:
        async with websockets.connect(
            f'{WS_SERVER}{GET_ALL}'
        ) as websocket:

            payload = {
                'database': GET_ALL_DB,
                'table': GET_ALL_INFRACTION_TABLE
            }

            identifier = str(uuid.uuid4())

            time = datetime.datetime.utcnow()
            time = str(time.isoformat('T') + 'Z')

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
                print(response)
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


def get_websocket_data():
    try:
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(get_all())
        return response
    except (asyncio.TimeoutError, ConnectionRefusedError) as err:
        print(err)
    except ConnectionClosed as err:
        print(err)
    except RuntimeError as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        asyncio.get_event_loop().stop()
