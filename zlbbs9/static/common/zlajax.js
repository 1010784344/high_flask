
// 对jquery的ajax的头部设置 X-CSRFtoken 的封装
//以后有任何表单提交的相关请求，引用这个 js 文件可以直接拿来用

'use strict';
var zlajax = {
	'get':function(args) {
		args['method'] = 'get';
		this.ajax(args);
	},
	'post':function(args) {
		args['method'] = 'post';
		this.ajax(args);
	},
	'ajax':function(args) {
		// 设置csrftoken
		this._ajaxSetup();
		$.ajax(args);
	},
	'_ajaxSetup': function() {
		$.ajaxSetup({
			'beforeSend':function(xhr,settings) {
				if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    //第二步：在ajax 请求的头部中给 X-CSRFtoken 这个变量赋值
					var csrftoken = $('meta[name=csrf-token]').attr('content');
                    // console.log(csrftoken);
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
			}
		});
	}
};