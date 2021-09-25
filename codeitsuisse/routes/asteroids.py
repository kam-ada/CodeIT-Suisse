import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])


def evaluateAsteroid():
    data = request.get_json('[...]')
    logging.info("data sent for evaluation {}".format(data))
    input = data.get("test_cases")
    result = []
    for line in input:
        score = algorithm(line) 
        temp = {}
        temp.update({"input": line})
        temp.update({"score": score[0]})
        temp.update({"origin": score[1]})
        result.append(temp)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def algorithm (text):
    origin = 0
    final_origin = 0
    final_score = 0
    sub_ttl = 1
    total = 0
    for position in text:
        left = 1
        right = 1
        while (origin - left >= 0 or origin + right < len(text)):
            left_prev = text[origin - left + 1]
            right_prev = text[origin + right - 1]
            if (origin - left < 0):
                right_cur = text[origin + right]
                if (right_cur == right_prev):
                    sub_ttl += 1
                    right += 1
                else:
                    break
            elif (origin + right >= len(text)):
                left_cur = text[origin - left]
                if (left_cur == left_prev):
                    sub_ttl += 1
                    left += 1
                else:
                    break
            else:
                left_cur = text[origin - left]
                right_cur = text[origin + right]
                if (left_cur == right_cur):
                    if (left_cur != left_prev):
                        total += calc (sub_ttl)
                        sub_ttl = 0
                    sub_ttl += 2
                    left += 1
                    right += 1
                else:
                    if (left_cur == left_prev):
                        sub_ttl += 1
                        left += 1
                    elif (right_cur == right_prev):
                        sub_ttl += 1
                        right += 1
                    else:
                        break
        total += calc(sub_ttl)
        sub_ttl = 1
        if (total > final_score):
            final_score = total
            final_origin = origin
        origin += 1
        total = 0


    if (final_score - int(final_score) == 0):
        final_score = int(final_score)
    return final_score, final_origin

def calc (num):
    if num >= 10:
        return num * 2
    elif num >= 7:
        return num * 1.5
    else:
        return num