function getMeNextFirst (inp)
{
	var ar = inp.trim();
	ar = ar.split(" ");
	var n = ar.length;
	var prev = "";
	for (var i = n-1; i >= 0; i--)
	{
		if (ar[i] != "")
		{
//			console.log(ar[i][0]);
			ar[i] = ar[i] + prev;
//			console.log(prev);
			prev = ar[i][0];
			if (i > 0)
				ar[i] = ar[i].substr(1);
		}
	}
	ar = ar.join(" ");
	console.log(ar);
}

getMeNextFirst("  Hello World !!  ");
