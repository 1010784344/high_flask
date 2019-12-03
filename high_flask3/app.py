from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/myworld/')
def hello_world():
    # 模板传递多个参数的技巧：统一放在一个字典里传递进去
    context={
        'country':'china',
        'age':'18',
        'destory':'haha',
        'zuhe':{'name1':'baibai','name2':'pangpang'}
    }

    return render_template('index.html',context=context)


# 过滤器(取绝对值)的使用
@app.route('/position/')
def position():
    return render_template('position.html',position=-9)




# default 过滤器的使用
@app.route('/signup/')
def signup():
    context = {
        'name': 'china',
        'signature': None
    }
    return render_template('signup.html',**context)


# escape/safe 过滤器的使用
@app.route('/escape/')
def escape():
    context = {
        'name': 'china',
        'signature': "<script>alert('hello world')</script>",
        'person':[3,2,1],
        'field':'hello world',
        'create_time1':datetime(2019,12,3,10,40,0),
        'create_time2':datetime(2019,12,2,10,40,0),
        'create_time3':datetime(2019,10,2,10,40,0)
    }
    return render_template('escape.html',**context)


# 自定义过滤器,并在模板进行注册
@app.template_filter('cut')
def cut(value):
    value = value.replace('hello','')
    return value


# 自定义时间过滤器,并在模板进行注册
@app.template_filter('handle_time')
def handle_time(time):
    """
    time 距离现在的时间间隔
    1.如果时间间隔小于 1 分钟以内，那么就显示刚刚
    2.如果是大于1分钟小于1小时，那么就显示‘XX分钟前’
    3.如果是大于1小时小于24小时，那么就显示‘XX小时前’
    4.如果是大于24小时小于30天以内，那么就显示‘XX天前’
    5.否则就显示具体的时间 2017/10/10 17:20
    :param time:
    :return:
    """
    if isinstance(time,datetime):
        now = datetime.now()
        # 获取秒数差
        timestamp = (now-time).total_seconds()

        if timestamp < 60:
            return '刚刚'
        elif timestamp > 60 and timestamp < 60 * 60:
            minnutes = timestamp/60
            return '%s 分钟前'%int(minnutes)
        elif timestamp > 60 * 60 and timestamp < 60 * 60 * 24:
            hours = timestamp/(60 * 60)
            return '%s 小时前'%int(hours)
        elif timestamp > 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
            days = timestamp/(60 * 60 * 24)
            return '%s 天前'%int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time





if __name__ == '__main__':
    app.run(debug=True)
