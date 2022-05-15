import detection.expression as ex
from flask import Flask
from flask import request
from flask import jsonify, make_response
import numpy as np
import asyncio
import cv2

loop = asyncio.get_event_loop()
app = Flask(__name__)


@app.route("/getExpression", methods=['POST'])
async def get_expression():
    response = await handle_pic_get_expression(request)
    return response


async def handle_pic_get_expression(request):
    try:
        f = request.files['file']
        img = cv2.imdecode(np.frombuffer(f.stream.read(), np.uint8), cv2.IMREAD_COLOR)
        res = ex.getExpression(img)
    except Exception as e:
        print(e)
        return make_response(jsonify({'data': None, 'status': 0, 'error': 'Something is wrong'}), 0)

    return make_response(jsonify({'data': res, 'status': 200, 'error': None}), 200)


app.run(host='0.0.0.0', port=81)
