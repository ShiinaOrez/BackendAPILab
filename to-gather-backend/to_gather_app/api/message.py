import datetime
from flask import jsonify, request, current_app
from . import api
from .. import db
from ..models import User, Activity, Message, Picker2Activity
from ..exceptions import ActivityError
from .._internal import _get_records

@api.route("/user/<string:unum>/message/<int:mid>/", methods=["GET"], endpoint="MessageEntity")
@User.check
def message_entity(info, unum, mid):
    usr = User.query.filter_by(std_num=unum).first()
    if usr is None:
        return jsonify({"msg": "user student number invalid"}), 401
    if usr.id != info.get("id"):
        return jsonify({"msg": "please check your self information"}), 407
    msg = Message.query.filter_by(id=mid).first()
    if msg is None:
        return jsonify({"msg": "message is not existed"}), 406
    act = Activity.query.filter_by(id=msg.aid).first()
    if act is None:
        return jsonify({"msg": "activity is not existed"}), 406
    info = act.info
    _data = {
        "datetime": info["date"] + " " + info["time"],
        "location": info["location"],
        "event": info["event"],
        "question": info["question"],
        "answer": msg.answer,
        "picker_id": msg.picker_id,
        "qq": info["qq"],
        "tel": info["tel"],
        "time": msg.time,
        "readed": msg.readed
    }
#    msg.readed = True
    db.session.add(msg)
    db.session.commit()
    return jsonify(_data), 200

@api.route("/user/<string:unum>/activity/<int:aid>/message/list/", methods=["GET"], endpoint="MessageList")
@User.check
def message_list(info, unum, aid):
    if info["unum"] != unum:
        return jsonify({"msg": "please check your self information"}), 407
    act = Activity.query.filter_by(id=aid).first()
    if act is None:
        return jsonify({"msg": "activity is not existed"}), 406
    if act.poster_id != info.get("id"):
        return jsonify({"msg": "please check your self information"}), 407
    _data = Message.query.filter_by(aid=aid, readed=False).all()
    if act.close or (not act.pickable):
        msg = Message.query.filter_by(aid=act.id, picker_id=act.picker_id).first()
        try:
            for m in _data:
                if m is msg:
                    continue
                record = Picker2Activity.query.filter_by(aid=act.id, picker_id=m.picker_id).first()
                if record is not None:
                    record.FAIL = True
        except:
            pass
        if msg is not None:
            _data = []
            _data.append(msg)
    msgList = [a.id for a in _data]
    if len(msgList) == 0:
        return jsonify({"msg": "none messages"}), 201
    return jsonify({
        "messageList": msgList,
        "messageCount": len(msgList)}), 200
