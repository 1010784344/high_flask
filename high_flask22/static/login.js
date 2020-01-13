console.log('1111')


$(function () {

    $('#submit').click(function (event) {


        event.preventDefault();
        var username = $('input[name=username]').val();
        var password = $('input[name=password]').val();
        var csrf_token = $('input[name=csrf_token]').val();

        $.post({
            'url':'/regist/',
            'data':{
                'username':username,
                'password':password,
                'csrf_token':csrf_token
            },
            'success':function (data) {
                console.log(data);
                
            },
            'fail':function (error) {
                console.log(error);

            }


        });


        
    });


    
});