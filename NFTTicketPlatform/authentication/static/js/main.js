		$(function(){


			$('#feee').val(parseFloat(($('#ticket_cost1').val()*0.03)));

			$('#total_cost1').val(parseFloat($('#ticket_cost1').val())+parseFloat($('#feee').val()));

		});

