let x = true;
function edit(){
	let el = document.getElementsByClassName("paragrafo");
	if(x){
		for (let i = 0; i < el.length; i++) {
			el[i].style.color = "blue";
		}
		x = false;
	}
	else{
		for (let i = 0; i < el.length; i++) {
			el[i].style.color = "purple";
		}
		x = true;
	}
}
