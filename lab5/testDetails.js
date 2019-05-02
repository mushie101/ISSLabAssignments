require('./data.js');


function getHighestMarks ()
{
	var total, anstot = (-1), ans;
	for (name in file)
	{
		total = 0;
		for (var i = 0; i < 5; i++)
		{
			total += file[name][i];
//			console.log(file[name]);
		}
		if (total > anstot)
		{
			anstot = total;
			ans = name;
		}
	}
	return ans;
}

console.log(getHighestMarks());

function getSubject2Toppers ()
{
	var ar = [ ["", 0] ];
	for (name in file)
		ar.push( [name, file[name][1]] );
	var n = ar.length;
	// Bubble Sort for the array
	for (var i = 0; i < n; i++)
	{
		for (var j = 1; j < n; j++)
		{
			if (ar[j-1][1] < ar[j][1])
			{
				var temp = ar[j];
				ar[j] = ar[j-1];
				ar[j-1] = temp;
			}
		}
	}
	
	console.log("ar[1] = ", ar[1][1]);
	var ans = [];
	for (var i = 0; i < n; i++)
		ans.push(ar[i][0]);
	return ans
}

console.log(getSubject2Toppers());
