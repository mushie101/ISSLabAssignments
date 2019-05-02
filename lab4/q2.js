function altSpaceToUnderscore (inp)
{
	var ar = inp.trim();
	ar = ar.split("");
	var n = inp.length;
	var fl = 1;
	for (var i = 0; i < n; i++)
	{
		if (ar[i] == " ")
		{
			if (fl == 0)
			{
				ar[i] = "_";
				fl = 1;
			}
			else if (fl == 1)
				fl = 0;
		}
	}
	ar = ar.join("");
	console.log(ar);
}

altSpaceToUnderscore("Heyya, how are you !!");
