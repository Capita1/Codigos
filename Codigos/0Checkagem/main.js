var id = 0
//DEFINE BOTAO ADD
var add = document.createElement("input");
add.setAttribute("type", "button");
add.setAttribute("value", "+");

//DEFINE TEXTO	
var txtarea = document.createElement("input");
txtarea.setAttribute("type", "textarea");

//ADICIONA CAIXA DE TEXTO NO BODY
document.getElementById('area').appendChild(txtarea);
//ADICIONA O BOTAO NO BODY
document.getElementById('area').appendChild(add)

add.onclick = function(){
	//DEFINE DIV
	var div = document.createElement('div');
	div.setAttribute("id",'d' + id);
	document.body.appendChild(div);	//ADICIONA DIV NO BODY
	console.log(div.id);

	//DEFINE CHECKBOX
	var chkbox = document.createElement("input");
	chkbox.setAttribute("type", "checkbox");
	document.getElementById('d' + id).appendChild(chkbox);	//ADICIONA CHECKBOX NA DIV

	var txt = document.createElement("span");
	txt.textContent=(txtarea.value);
	document.getElementById('d' + id).appendChild(txt);
	id++
};
