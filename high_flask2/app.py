from flask import Flask,redirect,url_for,Response,jsonify,make_response

app = Flask(__name__)

# 返回响应的时候将字典转换为 json 格式的数据返回,重新改写之前的默认方法
# 第一步定义类
class JSONResponse(Response):
    """
    这个方法只有视图函数返回非字符，非元组，非Response对象才会调用
    response 视图函数的返回值
    """
    @classmethod
    def force_type(cls, response, environ=None):

        # 如果是字典的话返回 josn
        if isinstance(response, dict):
            # flask 中将字典转换为 json 的方法：jsonify
            response = jsonify(response)
            # return super(JSONResponse, cls).force_type(response, environ)
            return response
        # 非字典的话返回 'hello'
        else:
            return Response('ok')

#第二步注册类
app.response_class = JSONResponse


# 第三步 进行调用
# 返回字典
@app.route('/allin/')
def allin():
    return {'allin':'gongzhuang'}


# 返回字符串
@app.route('/list/')
def mylist():
    #下面的 return 等价于 Response('Hello  go to mylist!',status = 200,mimetype='text/html')
    return 'Hello  go to mylist!'



# 返回 Response 对象
@app.route('/list1/')
def list1():
    return make_response('list1')



# 返回 Response 对象,并设置 cookie
@app.route('/list2/')
def list2():
    resp = make_response('list2')
    resp.set_cookie('country','china')
    return resp


# 返回元组，设置响应头
@app.route('/reshead/')
def reshead():
    return 'reshead',200,{'x-name':'dawang'}




if __name__ == '__main__':

    app.run(debug=True)
