function fifthDay ()
{
	var days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]
	var dat = new Date();
	return days[((dat.getDay())+5)%7];
}

console.log(fifthDay());
