/*
 * On this script are all the functions used on the homepage like
 * form animations and validations, behaviour of the elements, etc. 
 */

//Global variables used to check if the register box is filled OK
var emailOK=false;
var passOK=false;

function login(e)
{
	
	e.preventDefault();
	
	if (typeof(REQUEST) != "undefined" && REQUEST)
		return;
	
	var data = {
		"user_login-email":$('#username').val(),
		"user_login-password":$('#password').val(),
		"user_login-remember_me":$('#remember').val(),
		};
	if ($('#next').val() != "") {
		data["next"] = $('#next').val();
	}
	
	$("#wait-mask").show();
	
	REQUEST = $.ajax({
				url: AJAX_URL+"login/",
				dataType:"json",
				data: data,
				success: function(data){
					
					if (data.error)
					{
						$('#signinMenu .msgNoOK:first').html(data.error).show();
						$("#wait-mask").hide();
					}
					else
					{
						$('#signinMenu .msgNoOK:first').html("");
						if (typeof(data._redirect)!='undefined' && data._redirect)
						{
							REDIRECT = data._redirect;
							setTimeout(function(){window.location = REDIRECT}, 1000);
						}
					}
					
					REQUEST=null;
					},
				error: function(data){ $("#wait-mask").hide();REQUEST=null;},
				type:"POST",
				async:true
				});
}

//This function disable or enable the button checking the global variables
function renderStartBtn(){
	if(emailOK & passOK){
		$('#startBtn').removeClass('disabled');
		$('#startBtn').addClass('enabled');
		$('#startBtn').removeAttr('disabled');
		$('#startBtn').attr('title','Empezar el registro');
	}else{
		$('#startBtn').removeClass('enabled');
		$('#startBtn').addClass('disabled');
		$('#startBtn').attr('disabled', 'disabled');
		$('#startBtn').attr('title','Por favor completa correctamente el formulario');
	}
}


//This function checks if an string corresponds to an email
function echeck(email) {
	var regexp  = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	
	return (regexp.test(email));				
}

function checkEmail(event)
{
	
	$('#imgEmailLogin').attr('src','/media/img/icons/mailInactive.png');
	if ($(this).val()=="") {
		$(this).val('email');
		$('#txtMsgRegisterEmail').html('');
	}
	else{
		if(echeck($(this).val())==false){
			
			$('#msgRegisterEmail').removeClass('msgOK');
			$('#msgRegisterEmail').addClass('msgNoOK');
			$('#txtMsgRegisterEmail').html('El email no es válido, por favor revíselo');
			
			emailOK=false;
			renderStartBtn();
		}else{
			
			
			//Enviamos peticion y vemos si está en uso
			
			var used = false;
			
			$.ajax({
				url:AJAX_URL+"exists/",
				type:'post',
				dataType:'json',
				data: {email:$('#registerEmail').val()},
				async:"true",
				success: function(data){ 
			
					if(data.result){
						$('#msgRegisterEmail').removeClass('msgOK');
						$('#msgRegisterEmail').addClass('msgNoOK');
						$('#msgRegisterEmail').html('<span id="txtMsgRegisterEmail">Ya estas registrado. Puedes identificarte y acceder.</span>');
						emailOK=false;
						renderStartBtn();
					}
					else
					{
						$('#msgRegisterEmail').removeClass('msgNoOK');
						$('#msgRegisterEmail').addClass('msgOK');
						$('#msgRegisterEmail').html('<span id="txtMsgRegisterEmail">Todavía no estas registrado</span>');
						emailOK=true;
						renderStartBtn();
					}
				}
			});
		}
	}
}


//Here we add the behaviours to all the elements
$(document).ready(function(){
	
	//Starting with the start button
	renderStartBtn();
	

	//Then the login button
    $("#signinBtn").click(function(e){
		e.preventDefault();
		e.stopPropagation();
		
		if ($('#signinMenu').is(":visible")){
			$('#signinMenu').hide();
			$('#signinBtn').removeClass('openedLoginBtn');
			$('#signinBtn').addClass('closedLoginBtn');
			
		}
		else{
			
			$('#signinMenu').show();
			$('#signinBtn').removeClass('closedLoginBtn');
			$('#signinBtn').addClass('openedLoginBtn');
			$('#username').focus();
		}
	});
    
    IN_SIGNIN = false;
    $('#signinMenu').mouseover(function(){IN_SIGNIN = true;});
    $('#signinMenu').mouseout(function(){IN_SIGNIN = false;});
        
    $(document).children().click(function(e){
        if (IN_SIGNIN) return;
        $('#signinMenu').hide();
		$('#signinBtn').removeClass('openedLoginBtn');
		$('#signinBtn').addClass('closedLoginBtn');
	});
    

	$('#username').focus(function(){
			$('.loginMail').css('background-image','url("/media/img/icons/mailActive.png")');
		})
		.one('focus',function(){$(this).val('');})
		.blur(function(){
			$('.loginMail').css('background-image','url("/media/img/icons/mailInactive.png")');
			if($(this).val().length>0 && !echeck($(this).val())){
					$('#msgLoginEmail').removeClass('msgOK');
					$('#msgLoginEmail').addClass('msgNoOK');
					$('#txtMsgLoginEmail').html('El email no es válido, por favor revíselo');
					
				}else{
					
					$('#msgLoginEmail').html('');
					$('#msgLoginEmail').hide();
				}
		});
		
	$('#password').focus(function(){
			$('.loginPassword').css('background-image','url("/media/img/icons/passIconActive.png")');
		})
		.one('focus',function(){$(this).val('');})
		.blur(function(){
			$('.loginPassword').css('background-image','url("/media/img/icons/passIconInactive.png")');
		})		
		.keypress(function(e)
		{
			var code = (e.keyCode ? e.keyCode : e.which);
			if (code == 13) $("#signin_submit").click();
			
		});
	
	//~ $('#signin_submit').click(login);
	
	$.preload([ 'passIconInactive', 'passIconActive', 'mailInactive', 'mailActive','loginBtn' ], {
		base:'/media/img/icons/',
		ext:'.png'
	});
	
	AJAX_URL = "/ajax/"
	
	/*$('#signin').submit(function(){alert("submit");});*/
	
	$(document).placeholder();
});
