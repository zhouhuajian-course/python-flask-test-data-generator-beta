"""


@author  : zhouhuajian
@version : v1.0
"""
import random

from flask import Blueprint, render_template, redirect, request
from db.test import db, TestData

bp = Blueprint('api_test', __name__)

chars="0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz共决压争划列则光先阶那关再动军农会众传价件任全华产交论设许达过导并年当合各后名同向问安好如她江红级约场地在回团因多式存成观老机权收次有此百而米色西行至自乓乒乔丢买兴冰冲厌创刚刘刑兆亚匠防邪阳阴阵网劣企伞仰伐仿伏伙伤似伟伪伍休优协充亦访讽讲延芒芝巡州迈迁迅寺寻夺夹夸巩异庆庄帆师吃吊吓吉吗吐吸驰闭闯守宇宅妇奸妈妄岂岁屿尽壮扛扣扩扫托扬执池汗汤污纪纤圾尘尖忙孙字负贞毕轨死危爷戏灯灰考朵朴杀朽杂朱欢旬早旨曲肌臣虫耳齐肉舌羽舟竹页衣血羊份"

@bp.route('/api/test/text', methods=['POST'])
def text():
    size = int(request.form['size'])
    data = ''.join(random.sample(chars, size))
    db.session.add(TestData(type="text", size=size, data=data))
    db.session.commit()
    return redirect('/test/data')

@bp.route('/api/test/file', methods=['POST'])
def file():
    size = int(request.form['size'])
    filename = request.form['filename']
    data = filename
    db.session.add(TestData(type="file", size=size, data=data))
    db.session.commit()
    return redirect('/test/data')

